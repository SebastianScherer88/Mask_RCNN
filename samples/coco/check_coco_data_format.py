# -*- coding: utf-8 -*-
"""
Created on Mon Jun  1 22:06:08 2020

@author: bettmensch
"""

import json

with open(r'C:\Users\bettmensch\Downloads\annotations/instances_val2014.json','r') as an_val_file:
    dataset = json.load(an_val_file)
    
type(dataset)

dataset.keys()

type(dataset['info']) # list
len(dataset['info']) # 6

type(dataset['licenses']) # list
len(dataset['licenses']) # 8

dataset['licenses'][2]

# =============================================================================
# {'url': 'http://creativecommons.org/licenses/by-nc-nd/2.0/',
#  'id': 3,
#  'name': 'Attribution-NonCommercial-NoDerivs License'}
# =============================================================================

type(dataset['categories']) # list
len(dataset['categories']) # 80

dataset['categories'][0]

# =============================================================================
# {'supercategory': 'person', 'id': 1, 'name': 'person'}
# =============================================================================

type(dataset['images']) # list
len(dataset['images']) # 40504

dataset['images'][0]

# =============================================================================
# {'license': 3,
#  'file_name': 'COCO_val2014_000000391895.jpg',
#  'coco_url': 'http://images.cocodataset.org/val2014/COCO_val2014_000000391895.jpg',
#  'height': 360,
#  'width': 640,
#  'date_captured': '2013-11-14 11:18:45',
#  'flickr_url': 'http://farm9.staticflickr.com/8186/8119368305_4e622c8349_z.jpg',
#  'id': 391895}
# =============================================================================

type(dataset['annotations']) # list
len(dataset['annotations']) # 291875

dataset['annotations'][2]

# {'segmentation': [[274.58,
#
#    405.68,
#    298.32,
#    405.68,
#    302.45,
#    402.58,
#    333.42,
#    404.65,
#    356.13,
#    397.42,
#    386.06,
#    386.06,
#    398.45,
#    367.48,
#    399.48,
#    356.13,
#    392.26,
#    347.87,
#    382.97,
#    350.97,
#    339.61,
#    357.16,
#    283.87,
#    365.42,
#    269.42,
#    367.48,
#    243.61,
#    362.32,
#    239.48,
#    368.52,
#    241.55,
#    374.71,
#    253.94,
#    381.94,
#    267.35,
#    385.03,
#    271.48,
#    394.32,
#    271.48,
#    399.48,
#    272.52,
#    400.52,
#    281.81,
#    404.65]],
#  'area': 5607.661349999996,
#  'iscrowd': 0,
#  'image_id': 200365,
#  'bbox': [239.48, 347.87, 160.0, 57.81],
#  'category_id': 58,
#  'id': 603}
# =============================================================================

