#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-07-21 18:15:11

import os
import tensorflow as tf

se=tf.Session()
node1=tf.constant(3.0,dtype=tf.float32)
node2=tf.constant(4.0)
ret=se.run([node1,node2])
print(ret)