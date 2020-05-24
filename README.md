# Helmet-Mask-detection
Detecting mask and helmet on people using computer vision technology [YOLO(v3) and Tensorflow object detection API]

I labeled classes has 
a. Helmet Mask
b. Helmet No Mask!!
c. No Helmet!! Mask
d. No Helmet!! No Mask!!
### 
# Data preprocessing
for more details check on Notebook
### Download data from here[https://drive.google.com/file/d/1sZMkg0iQRd7z7LsvYRJPxxDlHH3o_hqW/view]
1. I parsed xml data containing only Head labelling section
2. For TF object detection API we need to generate xml files in PASCAL VOC format and for Yolo it should be in .txt format.
3. You need to delete some of the images which doesn't contain any labelling data before conversion or else this will leads to bias in model .
# Training
For training data must be in  TFrecord format , edit the configuration file for describing number of classes , type of  pretrained model and data augmentation. 
For training with Yolo you need to download darknet model. Edit configuration file for specifying no of classes  and cfg file path.
# Result 
First I tried with using Tensorflow object detection API. Tensorflow API failed to generalize well even after a day full of training even with augmented data. I passed xml file of no labeled images this might have caused bias while training. 
![img](https://i.imgur.com/mmBOSgx.png)
Yolo generalizes very well only with few iterations of training. It is able to predict bounding box and classes very accurately and its inference and training speed is very fast. I did training for aroung 20k steps with few more steps and with less image
![yolo1](https://i.imgur.com/d9x0zYQ.png)
![yolo2](https://i.imgur.com/OabPoDv.png)
As you can TF obj detection fails to located object  also class prediction are not accurate. Where as Yolo outperform tf API. Yolo is the fastest model available right now for object detection. 


