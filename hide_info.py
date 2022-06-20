# -*- coding: utf-8 -*-
import argparse

from PIL import Image
from Diffie_Hellman import get_Diffie_Hellman_key
from DCT.gen_SK_A_img import gen as gen_img_SK_A
from DCT.embed import gen_embedded_img


def plus(string):
    # Python zfill() 方法返回指定长度的字符串，原字符串右对齐，前面填充0。
    return string.zfill(8)


def get_info_to_hide(path):
    # 获取要隐藏的文件内容
    with open(path, "rb")  as f:
        s = f.read()
        string = ""
        for i in range(len(s)):
            # 逐个字节将要隐藏的文件内容转换为二进制，并拼接起来
            # 1.先用ord()函数将s的内容逐个转换为ascii码
            # 2.使用bin()函数将十进制的ascii码转换为二进制
            # 3.由于bin()函数转换二进制后，二进制字符串的前面会有"0b"来表示这个字符串是二进制形式，所以用replace()替换为空
            # 4.又由于ascii码转换二进制后是七位，而正常情况下每个字符由8位二进制组成，所以使用自定义函数plus将其填充为8位
            string = string + "" + plus(bin(s[i]).replace('0b', ''))
    # print(string)
    return string


def mod(x, y):
    return x % y


def hide_on_pixel(channel, count, info):
    # 下面的操作是将信息隐藏进去
    # 分别将每个像素点的RGB值余2，这样可以去掉最低位的值
    # 再从需要隐藏的信息中取出一位，转换为整型
    # 两值相加，就把信息隐藏起来了
    channel = channel - mod(channel, 2) + int(info[count])
    count = count + 1
    return channel, count


def hide(path_img, path_flag, path_img_encoded, key):
    im = Image.open(path_img)
    # 获取图片的宽和高
    width, height = im.size[0], im.size[1]
    index_start_pixel = mod(key, width * height)
    print('index_start_pixel:' + str(index_start_pixel))
    index_current_pixel = 0
    len_hid = 0
    # 获取需要隐藏的信息
    info = get_info_to_hide(path_flag)
    len_info = len(info)
    for h in range(height):
        for w in range(width):
            index_current_pixel = index_current_pixel + 1
            if index_current_pixel >= index_start_pixel:
                pixel = im.getpixel((w, h))
                r = pixel[0]
                g = pixel[1]
                b = pixel[2]
                if len_hid == len_info:
                    break
                r, len_hid = hide_on_pixel(r, len_hid, info)
                if len_hid == len_info:
                    im.putpixel((w, h), (r, g, b))
                    break
                g, len_hid = hide_on_pixel(g, len_hid, info)
                if len_hid == len_info:
                    im.putpixel((w, h), (r, g, b))
                    break
                b, len_hid = hide_on_pixel(b, len_hid, info)
                if len_hid == len_info:
                    im.putpixel((w, h), (r, g, b))
                    break
                if len_hid % 3 == 0:
                    im.putpixel((w, h), (r, g, b))
    im.save(path_img_encoded)


def choose_frame(key, whole_frames):
    return mod(key, whole_frames)


def main():
    # 添加参数
    parser = argparse.ArgumentParser(description='Hide the info into the Diffie-Hellman LSB.')
    parser.add_argument('-path_flag', action='store', help='The path of the flag')
    parser.add_argument('-path_img_encoded', action='store', help='The path of the image after encoded')
    parser.add_argument('-path_SKA_watermark', action='store', help='The path of the image of the watermark of SK_A')
    parser.add_argument('-path_title_watermarked', action='store', help='The path of the title image after watermarked')
    # 给参数赋值
    path_flag = parser.parse_args().path_flag
    path_img_encoded = parser.parse_args().path_img_encoded
    path_SKA_watermark = parser.parse_args().path_SKA_watermark
    path_title_watermarked = parser.parse_args().path_title_watermarked
    # 给参数设定默认值
    if path_flag is None:
        path_flag = 'flag_origin.txt'
    if path_SKA_watermark is None:
        path_SKA_watermark = 'keyprint.jpg'
    if path_img_encoded is None:
        path_img_encoded = "new.png"
    if path_title_watermarked is None:
        path_title_watermarked = 'title.png'
    # 获取dh的参数
    key, SK_A, SK_B = get_Diffie_Hellman_key()
    # 选择LSB的帧
    index_frame = choose_frame(key, 355)
    # 生成SK_A的数字水印原图
    gen_img_SK_A(SK_A)
    # DCT嵌入数字水印
    gen_embedded_img(path_SKA_watermark, path_title_watermarked)
    # 原图
    old_img = "frames/image_" + str(index_frame) + ".png"
    print("加密的图片是" + old_img)
    # 处理后输出的图片路径
    # 需要隐藏的信息
    hide(old_img, path_flag, path_img_encoded, key)


if __name__ == '__main__':
    main()
