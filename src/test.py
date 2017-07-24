#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-07-21 18:15:11

import os
import tensorflow as tf
import numpy as np

x_data=np.float32(np.random.rand(2,100))
y_data=np.dot([0.100,0.200],x_data)+0.300

b=tf.Variable()