# -*- coding: utf-8 -*-

import argparse
from PIL import Image


def mod(x, y):
    return x % y


def toasc(strr):
    return int(strr, 2)


# le为所要提取的信息的长度，str1为加密载体图片的路径，str2为提取文件的保存路径
def get(len_info, path_img, path_flag, index_start_pixel):
    b = ""
    im = Image.open(path_img)
    lenth = len_info * 8
    width, height = im.size[0], im.size[1]
    index_current_pixel = 0
    count = 0
    for h in range(height):
        for w in range(width):
            index_current_pixel = index_current_pixel + 1
            if index_current_pixel >= index_start_pixel:
                # 获得(w,h)点像素的值
                pixel = im.getpixel((w, h))
                # 此处余3，依次从R、G、B三个颜色通道获得最低位的隐藏信息
                if count % 3 == 0:
                    count += 1
                    b = b + str((mod(int(pixel[0]), 2)))
                    if count == lenth:
                        break
                if count % 3 == 1:
                    count += 1
                    b = b + str((mod(int(pixel[1]), 2)))
                    if count == lenth:
                        break
                if count % 3 == 2:
                    count += 1
                    b = b + str((mod(int(pixel[2]), 2)))
                    if count == lenth:
                        break
        if count == lenth:
            break

    with open(path_flag, "w", encoding='utf-8') as f:
        for i in range(0, len(b), 8):
            # 以每8位为一组二进制，转换为十进制
            stra = toasc(b[i:i + 8])
            # 将转换后的十进制数视为ascii码，再转换为字符串写入到文件中
            # print((stra))
            f.write(chr(stra))
    print("完成信息提取！")


def main():
    parser = argparse.ArgumentParser(description='Get the info from the Diffie-Hellman LSB.')
    parser.add_argument('-path_img', action='store', help='The path of the image')
    parser.add_argument('-path_flag', action='store', help='The path of the flag')
    parser.add_argument('-index_start_pixel', action='store', help='The index of the start pixel', type=int)

    path_img = parser.parse_args().path_img
    path_flag = parser.parse_args().path_flag
    index_start_pixel = parser.parse_args().index_start_pixel

    if path_flag is None:
        path_flag = 'flag.txt'
    if path_img is None:
        path_img = "new.png"
    # 文件长度
    len_info = 30
    get(len_info, path_img, path_flag, index_start_pixel)


if __name__ == '__main__':
    main()
