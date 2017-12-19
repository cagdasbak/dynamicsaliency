![logo](https://raw.githubusercontent.com/cagdasbak/dynamicsaliency/master/img/main.png)

This repository is an open source [caffe](http://caffe.berkeleyvision.org/) implementation of Two-Stream Convolutional Networks for Dynamic Saliency Prediction.

### Abstract

In recent years, visual saliency estimation in images has attracted much attention in the computer vision community.
However, predicting saliency in videos has received relatively little attention. Inspired by the recent success of deep
convolutional neural networks based static saliency models, in this work, we study two different two-stream convolutional
networks for dynamic saliency prediction. To improve the generalization capability of our models, we also
introduce a novel, empirically grounded data augmentation technique for this task. We test our models on DIEM
dataset and report superior results against the existing models. Moreover, we perform transfer learning experiments on
SALICON, a recently proposed static saliency dataset, by finetuning our models on the optical flows estimated from static images. Our experiments show that taking motion into account in this way can be helpful for static saliency estimation.

![results](https://raw.githubusercontent.com/cagdasbak/dynamicsaliency/master/img/saliency-networks.gif)

### Proposed Two-Stream Network Architectures

![late_fusion](https://raw.githubusercontent.com/cagdasbak/dynamicsaliency/master/img/late.png)
![early_fusion](https://raw.githubusercontent.com/cagdasbak/dynamicsaliency/master/img/early.png)

    
### Using instructions

./models/   : Pretrained caffe models (\w data augmentation) on DIEM dataset.

./prototxt/ : Caffe prototxt network architectures.

./scripts/  : Python scripts to generate saliency maps and to train networks.  

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

### Authors

![Cagdas Bak][CagdasBak-photo]  | ![Aysun Kocak][AysunKocak-photo]  | ![Erkut Erdem][ErkutErdem-photo]  | ![Aykut Erdem][AykutErdem-photo] |
|:-:|:-:|:-:|:-:|
| [Cagdas Bak][CagdasBak-web]  | [Aysun Kocak][AysunKocak-web]  |  [Erkut Erdem][ErkutErdem-web] | [Aykut Erdem][AykutErdem-web]   |

[CagdasBak-web]: https://vision.cs.hacettepe.edu.tr/people-detail.php?id=37
[AysunKocak-web]: https://vision.cs.hacettepe.edu.tr/people-detail.php?id=10
[ErkutErdem-web]: https://vision.cs.hacettepe.edu.tr/people-detail.php?id=5
[AykutErdem-web]: https://vision.cs.hacettepe.edu.tr/people-detail.php?id=4

[CagdasBak-photo]: https://raw.githubusercontent.com/cagdasbak/dynamicsaliency/master/img/CagdasBak-photo.jpg "Cagdas Bak"
[AysunKocak-photo]: https://raw.githubusercontent.com/cagdasbak/dynamicsaliency/master/img/AysunKocak-photo.png "Aysun Kocak"
[ErkutErdem-photo]: https://raw.githubusercontent.com/cagdasbak/dynamicsaliency/master/img/ErkutErdem-photo.jpg "Erkut Erdem"
[AykutErdem-photo]: https://raw.githubusercontent.com/cagdasbak/dynamicsaliency/master/img/AykutErdem-photo.jpg "Aykut Erdem"

If you have any question, send an e-mail at cagdasbak@hotmail.com
