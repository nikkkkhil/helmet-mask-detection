# Helmet-Mask-detection
Detecting mask and helmet on people using computer vision technology [YOLO(v3) and Tensorflow object detection API]

I labeled classes has 
a. Helmet Mask
b. Helmet No Mask!!
c. No Helmet!! Mask
d. No Helmet!! No Mask!!
### 
# Data preprocessing

### Download data from here[https://drive.google.com/file/d/1sZMkg0iQRd7z7LsvYRJPxxDlHH3o_hqW/view]
1. First parse xml data containing only Head labelling section.
2. For TF object detection API we need to generate xml files in PASCAL VOC format and for Yolo it should be in .txt format containing labeling dimension details.You need to generate additional txt file containing img file path only for YOLO.
3. You need to delete some of the images which doesn't contain any labelling class before conversion or else this will leads to bias in model .

# Training
For training,data must be in  TFrecord format , edit the configuration file for describing number of classes , type of  pretrained model used and data augmentation setup.

For training with Yolo you need to download darknet model. Edit configuration file for specifying no of classes  and cfg file path.for more details on training check notebook.

# Result 
First I tried with using Tensorflow object detection API. Tensorflow API failed to generalize very well even after a day full of training  with augmented data. 

![img](https://i.imgur.com/mmBOSgx.png)

Yolo generalizes very well only with few iterations of training. It was able to predict bounding box and classes very accurately, its inference and training speeds are very fast. Training for aroung 20k weights suffecient enough for average performance. For better performance iterate to few more weights and do data augmentation. 

![yolo1](https://i.imgur.com/d9x0zYQ.png)
![yolo2](https://i.imgur.com/OabPoDv.png)

As you can see TF obj detection fails to locate object  also class prediction are not accurate. Where as Yolo outperforms both in prediction of class and localization . Yolo is so far best object detection model architecture available. Its faster and accurate than R-CNN variance architectures. 

