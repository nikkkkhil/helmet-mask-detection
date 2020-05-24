#!/usr/bin/env python
# coding: utf-8

# In[1]:


import xml.etree.ElementTree as ET
from lxml.etree import Element, SubElement, tostring
from lxml import etree
import pprint
from xml.dom.minidom import parseString
from tqdm import tqdm


# In[2]:


tree = ET.parse('/home/nikhil/Desktop/practice/helmet_detection/idata/annotations.xml')


# In[3]:


root = tree.getroot()


# In[4]:


obj_cls = ['Helmet Mask','No Helmet!! Mask','Helmet No Mask!!','No Helmet!! No Mask!!']


# In[5]:


store = {}


# In[6]:


import os
os.getcwd()


# In[7]:


for x in tqdm(root.findall('image')):
    file_name = x.attrib['id'] + '.jpg'
    file_path = '/home/nikhil/Desktop/practice/interview/interview_data/images/train/'+x.attrib['id'] + '.jpg'
    file_save = '/home/nikhil/Desktop/practice/helmet_detection/images/train/'+x.attrib['id'] + '.xml'
    w = x.attrib['width']
    h = x.attrib['height']
    d = str(3)
    print(file_name, w, h, d)
     
    node_root = Element('annotation')

    node_folder = SubElement(node_root, 'folder')
    node_folder.text = "train"
    node_filename = SubElement(node_root, 'filename')
    node_filename.text = file_name
    node_filepath = SubElement(node_root, 'path')
    node_filepath.text = file_path
    node_source = SubElement(node_root, 'source')
    node_database = SubElement(node_source, 'database')
    node_database.text = 'Unknown'

    node_size = SubElement(node_root, 'size')
    node_width = SubElement(node_size, 'width')
    node_width.text = w


    node_height = SubElement(node_size, 'height')
    node_height.text = h

    node_depth = SubElement(node_size, 'depth')
    node_depth.text = d
    
    node_segment = SubElement(node_root, 'segmented')
    node_segment.text ='0'
 
    for y in x.findall('box'):
        if y.attrib['label'] == 'head':
            lab = y.attrib
            x_min = lab['xtl'] 
            y_min = lab['ytl']
            x_max = lab['xbr']
            y_max = lab['ybr']
            for z in y.findall('attribute'):
                obj = z.attrib
                obj_check = z.text
                store[obj['name']] = obj_check                
            if store['has_safety_helmet'] == 'yes' and store['mask'] == 'yes':
                obj_name  = obj_cls[0]
            elif store['has_safety_helmet'] == 'no' and store['mask'] == 'yes':
                obj_name  = obj_cls[1]
            elif store['has_safety_helmet'] == 'yes' and store['mask'] == 'no':
                obj_name  = obj_cls[2]
            elif store['has_safety_helmet'] == 'no' and store['mask'] == 'no':
                obj_name  = obj_cls[3]
            node_object = SubElement(node_root, 'object')
            node_name = SubElement(node_object, 'name')
            node_name.text = obj_name
            node_pose = SubElement(node_object, 'pose')
            node_pose.text = 'Unspecified'
            node_truncated = SubElement(node_object, 'truncated')
            node_truncated.text = '0'
            node_difficult = SubElement(node_object, 'difficult')
            node_difficult.text = '0'
            node_bndbox = SubElement(node_object, 'bndbox')
            node_xmin = SubElement(node_bndbox, 'xmin')
            node_xmin.text = x_min
            node_ymin = SubElement(node_bndbox, 'ymin')
            node_ymin.text = y_min
            node_xmax = SubElement(node_bndbox, 'xmax')
            node_xmax.text = x_max
            node_ymax = SubElement(node_bndbox, 'ymax')
            node_ymax.text = y_max
            with open(file_save,'wb') as f:
                f.write(etree.tostring(node_root, pretty_print = True))
                f.close
            print(obj_name)
            store = {}


# In[ ]:




