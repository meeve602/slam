import argparse
import glob
import numpy as np
import os
import time

import cv2
import torch
import torch.nn as nn

class SuperPointNet(torch.nn.Module):
  """ Pytorch definition of SuperPoint Network. """
  def __init__(self,model_dict):
    super(SuperPointNet, self).__init__()
    self.quant = torch.quantization.QuantStub()
    self.encoder = model_dict['block_encoder']# key and value
    self.detector = model_dict['block_detector']
    self.descriptor = model_dict['block_descriptor']
    self.dequant = torch.quantization.DeQuantStub()

  def forward(self, x):
    """ Forward pass that jointly computes unprocessed point and descriptor
    tensors.
    Input
      x: Image pytorch tensor shaped N x 1 x H x W.
    Output
      semi: Output point pytorch tensor shaped N x 65 x H/8 x W/8.
      desc: Output descriptor pytorch tensor shaped N x 256 x H/8 x W/8.
    """
    # Shared Encoder.
    x= self.quant(x)
    out1 = self.encoder(x)
    semi = self.detector(out1)
    semi = self.dequant(semi)
    
    desc = self.descriptor(out1)
    desc = self.dequant(desc)
    dn = torch.norm(desc, p=2, dim=1) # Compute the norm.
    
    desc = desc.div(torch.unsqueeze(dn, 1)) # Divide by norm to normalize.
    return semi, desc

def get_sp_model():
    blocks = {}
    block_encoder =[{'conv1a':[1,64,3,1,1]},{'conv1b':[64,64,3,1,1]},{'pool1':[2,2]},
                    {'conv2a':[64,64,3,1,1]},{'conv2b':[64,64,3,1,1]},{'pool2':[2,2]},
                    {'conv3a':[64,128,3,1,1]},{'conv3b':[128,128,3,1,1]},{'pool3':[2,2]},
                    {'conv4a':[128,128,3,1,1]},{'conv4b':[128,128,3,1,1]}]
    block_detector=[{'convPa':[128,256,3,1,1]},{'convPb':[256,65,1,1,0]}]
    block_descriptor=[{'convDa':[128,256,3,1,1]},{'convDb':[256,256,1,1,0]}]
    layers = []
    for block in block_encoder:
        for key in block:
            v = block[key]
            if 'pool' in key:
                layers += [nn.MaxPool2d(kernel_size=v[0], stride=v[1])]
            else:
                conv2d = nn.Conv2d(in_channels=v[0], out_channels=v[1], kernel_size=v[2], stride=v[3], padding=v[4])
                layers += [conv2d, nn.ReLU(inplace=True)]

    layers_p = []
    conv2d = nn.Conv2d(128, 256,kernel_size = 3, stride = 1,padding=1)
    layers_p += [conv2d, nn.ReLU(inplace=True)]
    layers_p += [nn.Conv2d(256, 65,kernel_size = 1, stride = 1,padding=0)]

    layers_d = []
    conv2d = nn.Conv2d(128, 256,kernel_size = 3, stride = 1,padding=1)
    layers_d += [conv2d, nn.ReLU(inplace=True)]
    layers_d += [nn.Conv2d(256, 256,kernel_size = 1, stride = 1,padding=0)]

    models ={
        'block_encoder': nn.Sequential(*layers),
        'block_detector': nn.Sequential(*layers_p),
        'block_descriptor': nn.Sequential(*layers_d)
    }
    return SuperPointNet(models)

