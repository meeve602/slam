import argparse
import glob
import random

import numpy as np
import os
import time

import cv2
import torch



def Calculate(pts, vs, last_pts, nm, img):
  after = pts[:2]
  count, offset, x_distance, y_distance, th, bigest, percentage = 0, 0, 0, 0, 4, 0, 0
  one = np.ones(1)
  before = last_pts[:2]
  covert = np.zeros([len(img[0:]), len(img.T[0:])])

  #test data
  test, t_x, t_y= [], [], []

  retvalue, retvalue_x, retvalue_y, retvalue_v, y_x, y_y = [], [], [], [], [], []
  i = np.size(pts[1]) - 1
  l = np.size(last_pts[1]) - 1

  if l <= i:
    i = l

  if nm:
    # read file
    H = np.array(vs.transform_extract())

    for j in range(0, i):
      k = 0
      x = after[..., j]
      y = before[..., j]
      x = np.append(x, values=one)
      y = np.append(y, values=one)
      z = np.matmul(H, x.T)
      calculate_x = round(z[0])
      calculate_y = round(z[1])

      # test output datas
      t_x = np.append(t_x, calculate_x)
      t_y = np.append(t_y, calculate_y)

    #precalculate to set the offset value
    # for j in range(0, i):
    #   x = after[..., j]
    #   # y = before[..., m]
    #   x = np.append(x, values=one)
    #   # y = np.append(y, values=one)
    #   z = np.matmul(H, x.T)
    #   calculate_x = round(z[0])
    #   calculate_y = round(z[1])

    for search in before.T:
      count_p = -1
      for p in t_x:
        count_p = count_p + 1
        x_distance = t_x[count_p] - search[0]
        y_distance = t_y[count_p] - search[1]
        x = np.add(before[:1], x_distance)
        y = np.add(before[1:], y_distance)
        offset = 0
        for n in range(0, i):
          x_x = x[0, n]
          x_y = y[0, n]
          for o in range(0, np.size(t_x)-1):
            if (t_x[o] + th > x_x) and (t_x[o] - th < x_x) and (t_y[o] +th > x_y) and (t_y[o] - th < x_y):
              offset = offset + 1
              # print(offset)
              break
          if bigest < offset:
            bigest = offset




    #percentage
    for j in range(0, i):
      k = 0
      x = after[..., j]
      # y = np.add(before[..., j], np.vstack(x_distance, y_distance))
      x = np.append(x, values=one)
      y = np.append(y, values=one)
      z = np.matmul(H, x.T)
      calculate_x = round(z[0])
      calculate_y = round(z[1])

      # test output datas
      t_x = np.append(t_x, calculate_x)
      t_y = np.append(t_y, calculate_y)

      for search in before.T:
        k = k + 1
        if (search[0] == calculate_x) and (search[1] == calculate_y):
          count = count + 1
          retvalue_x = np.append(retvalue_x, search[0])
          retvalue_y = np.append(retvalue_y, search[1])
          y_x = np.append(y_x, x[0])
          y_y = np.append(y_y, x[1])

    retvalue = np.vstack((retvalue_x, retvalue_y))  #left
    retvalue_v = np.vstack((y_x, y_y))              #right
    percentage = bigest / np.size(pts[1])
    print(percentage)

    fo = open("result.txt", "a+")
    line = str(percentage) + " "
    fo.write(line)
    fo.close()

    #test datas
    test = np.vstack((t_x, t_y))

    # convert img to
    width = len(img.T[0:])
    high = len(img[0:])
    for j in range(0, width-1):
      for k in range(0, high-1):
        tempory_coodinate = [j, k]
        tempory_coodinate = np.append(tempory_coodinate, values=one)

        #nomal
        # store_coodinate = np.matmul(H, tempory_coodinate.T)

        #inv
        store_coodinate = np.matmul(H, tempory_coodinate.T)


        img_cx = round(store_coodinate[0])
        img_cy = round(store_coodinate[1])
        if (img_cx < width and img_cy < high) and (img_cx >= 0 and img_cy >= 0):
          covert[img_cy, img_cx] = img[k, j]

  return  retvalue, retvalue_v, test, covert, percentage


