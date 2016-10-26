import os
import sys
import cv2
import numpy as np

PYCAFFE_DIR = ''


def _create_net(specfile, modelfile):
    if not PYCAFFE_DIR in sys.path:
        sys.path.insert(0, PYCAFFE_DIR)
    import caffe
    return caffe.Net(specfile, modelfile, caffe.TEST)
    
def find_scale_to_fit(im, shape):
    w, h = im.shape[1], im.shape[0]
    target_w, target_h = shape[1], shape[0]
    scale = 1.0
    if target_w is not None:
        scale = min(scale, target_w / float(w))
    if target_h is not None:
        scale = min(scale, target_h / float(h))
    return scale

class SalNet(object):
    input_layer = 'data1'
    input_layer_b = 'data1_b'
    output_layer = 'deconv1'
    default_model_path = os.path.join(os.path.dirname(__file__), 'model')
    
    def __init__(self, 
        specfile=None, 
        modelfile=None, 
        input_size=None,
        max_input_size=(512, 512),
        channel_swap=(2,1,0),
        mean_value=(100,110,118),
        input_scale=0.0078431372549,
        saliency_mean=127,
        blur_size=5,
        stretch_output=True,
        interpolation=cv2.INTER_CUBIC):
        
        if not specfile:
            specfile = os.path.join(self.default_model_path, 'deploy.prototxt')
            
        if not modelfile:
            modelfile = os.path.join(self.default_model_path, 'model.caffemodel')
        
        self.input_size = input_size
        self.max_input_size = max_input_size
        self.channel_swap = channel_swap
        self.mean_value = mean_value
        self.input_scale = input_scale
        self.saliency_mean = saliency_mean
        self.blur_size = blur_size
        self.net = _create_net(specfile, modelfile)
        self.stretch_output = stretch_output
        self.interpolation = interpolation
        
    def scale_input(self, im):
        if self.input_size:
            h, w = self.input_size
            im = cv2.resize(im, (w, h), interpolation=cv2.INTER_AREA)
        elif self.max_input_size:
            scale = find_scale_to_fit(im, self.max_input_size)
            im = cv2.resize(im, None, fx=scale, fy=scale)
        return im
        
    def preprocess_input(self, input_image):
        im = self.scale_input(input_image)
        if self.channel_swap:
            im = im[:,:,self.channel_swap]
        im = im.astype(np.float32)
        im -= np.array(self.mean_value)
        im *= self.input_scale
        im = im.transpose((2,0,1))
        return np.ascontiguousarray(im[np.newaxis,...], dtype=np.float32)
    
    def postprocess_output(self, net_output, map_shape):
        p = np.squeeze(np.array(net_output))
        p *= 128
        p += self.saliency_mean 
        p = np.clip(p, 0, 255)

        if map_shape:
            h, w = map_shape
            p = cv2.resize(p, (w, h), interpolation=self.interpolation)

        if self.blur_size:
            p = cv2.GaussianBlur(p, (self.blur_size, self.blur_size), 0)

        p = np.clip(p, 0, 255)

        if self.stretch_output:
            if p.max() > 0:
                p = (p / p.max()) * 255.0

        return p.astype(np.uint8)
    
    def get_saliency(self, image):

        image_b = image

        net_input = self.preprocess_input(image)
        net_input_b = self.preprocess_input(image_b)
        
        self.net.blobs[self.input_layer].reshape(*net_input.shape)
        self.net.blobs[self.input_layer_b].reshape(*net_input_b.shape)

        self.net.blobs[self.input_layer].data[...] = net_input
        self.net.blobs[self.input_layer_b].data[...] = net_input_b

        self.net.forward()
        
        net_output = self.net.blobs[self.output_layer].data[0,0]

        return self.postprocess_output(net_output, image.shape[:2])