# -*- coding: utf-8 -*-
import cv2
import os
import numpy as np
from PIL import ImageFont, Image, ImageDraw


# 生成一张图片
def create_pic():
    width = 300
    height = 300
    img = np.zeros([width, height, 3], dtype=np.uint8)
    # 遍历每个像素点，并进行赋值
    for i in range(width):
        for j in range(height):
            img[i, j, :] = [i % 512, j % 512, 50]

    # 展示图片
    # cv2.namedWindow('image', cv2.WINDOW_NORMAL)
    # cv2.imshow('image', img)
    cv2.imwrite("image.jpg", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


# 在图片中写入文字
def write_pic(number):
    bk_img = cv2.imread("image.jpg")
    # 设置需要显示的字体
    fontpath = "font/simsun.ttc"
    font = ImageFont.truetype(fontpath, 20)
    img_pil = Image.fromarray(bk_img)
    draw = ImageDraw.Draw(img_pil)
    # 绘制文字信息
    draw.text((0, 50), number, font=font, fill=(255, 255, 255))
    bk_img = np.array(img_pil)
    cv2.waitKey()
    createName = "keyprint.jpg"
    cv2.imwrite(createName, bk_img)


def remove():
    path = 'image.jpg'  # 文件路径
    os.remove(path)


def gen(SK_A):
    create_pic()
    write_pic("SKA_Diffie_Hellman is " + str(SK_A))
    remove()


