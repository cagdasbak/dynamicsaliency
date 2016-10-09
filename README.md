# Two-Stream Convolutional Networks for Dynamic Saliency Prediction

This repository is an open source implementation of Two-Stream Convolutional Networks for Dynamic Saliency Prediction.

### Abstract
In recent years, visual saliency estimation in images has attracted much attention in the computer vision community.
However, predicting saliency in videos has received relatively little attention. Inspired by the recent success of deep
convolutional neural networks based static saliency models, in this work, we study two different two-stream convolutional
networks for dynamic saliency prediction. To improve the generalization capability of our models, we also
introduce a novel, empirically grounded data augmentation technique for this task. We test our models on DIEM
dataset and report superior results against the existing models. Moreover, we perform transfer learning experiments on
SALICON, a recently proposed static saliency dataset, by finetuning our models on the optical flows estimated from static images. Our experiments show that taking motion into account in this way can be helpful for static saliency estimation.

### Proposed Two-Stream Network Architectures
![late_fusion](https://raw.githubusercontent.com/imatge-upc/saliency-2016-cvpr/master/figs/paper.jpg)
![early_fusion](https://raw.githubusercontent.com/imatge-upc/saliency-2016-cvpr/master/figs/paper.jpg)

    
### Using instructions

##### Basic Demo (producing saliency maps from images)
1. Edit the `Salicon.py` file to include the path to your caffe python install where indicated (i.e. update the line below to the path containing your caffe installation):

    ````python
        sys.path.insert(0, 'caffe/install/python') # PATH TO CAFFE PYTHON INSTALL
    ````
    Additionally, depending on whether you are using a GPU or not, you may need to edit the following two lines:
	
    ````python
    caffe.set_mode_gpu()
    caffe.set_device(1)
    ````
    If you do not have a CPU, be sure to remove the ````set_device(1) ```` line and change the mode selection to ```` caffe.set_mode_cpu() ````. Depending on your setup, you may need to change the device ID from 1 to 0 or some other number depending on your hardware configuration.
2. Download the caffemodel files using **[this link.](http://www.cs.pitt.edu/~chris/files/2016/model_files.tgz)** Place the caffemodel files into the same directory as the code (unless you manually modify the paths to point to the directory containing the caffemodel files).
3. The following commands should allow you to compute the saliency map for an image using the pretrained model. **IMPORTANT:** When using on your own data, ensure that your data is in 256 RGB format. If it is not, you will need to manually do some pre-processing first.
4. Run python and execute the following commands:

    ````python
    from Salicon import Salicon
    sal = Salicon()
    map = sal.compute_saliency('face.jpg')
    # map contains saliency map in double format.
    ````
    ![Original Image](/face.jpg "Original Image")
    ![Resulting Map](/face_out.jpg "Resulting Map")
5. You can then perform thresholding (if you prefer) on the output or use it directly.

##### Training your own model

Use the finetune_salicon.py file to train your own model. See our technical report for more details on how to do this. We provide two solvers ```` solver.prototxt ```` and ```` solver_new.prototxt ```` for this purpose. Solver_new attempts to use ADADELTA to adjust the learning rate dynamically. ````finetune_salicon.prototxt```` provides a model definition file for our implementation in which you can adjust learning rates per layer and more customization. Our ```` finetune_salicon.py```` file provides the basic functionality of reading in the input images and fixation maps, initializing the solver, loading the data in batches, solving the model, and saving the results. You may need to adjust the solver to your particular dataset.

#### Parting Words

OpenSALICON performs on-par with the results produced by the official SALICON demo website when compared using AUC scores to ground truth human fixations. If you have any questions, discover any bugs, or make improvements to this code, please feel free to create an issue or push request.

### Citation

Please cite our [paper](https://arxiv.org/pdf/1607.04730v1.pdf) in your publications if it helps your research:
````
@article{bak2016two,
  title={Two-Stream Convolutional Networks for Dynamic Saliency Prediction},
  author={Bak, {\c{C}}a{\u{g}}da{\c{s}} and Erdem, Aykut and Erdem, Erkut},
  journal={arXiv preprint arXiv:1607.04730},
  year={2016}
}

````
