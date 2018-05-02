#!/usr/bin/python

from PIL import Image
import os
import re

# 当前目录
# 后缀需为png

arr = []
p1 = "icon.png"

class OSize:
    def __init__(self, _w):
        self.w = _w
        self.h = _w
        self.o = (_w, _w)
        self.filename = str(_w)+"x"+str(_w)+".png"

out_size = [
    OSize(1024),
    OSize(120),
	OSize(180),
	OSize(80),
	OSize(87),
	OSize(58),
	OSize(40),
	OSize(60),
	OSize(76),
	OSize(167),
	OSize(152),
	OSize(20),
	OSize(29),
]

# 创建文件夹
if not os.path.exists("./out"):
    os.mkdir(r"./out");


print("开始处理")
fromImage = Image.open(p1)
for osize in out_size:

    outimage = fromImage.resize(osize.o, Image.ANTIALIAS)
    outPath = "out" + "/" +osize.filename
    outimage.save(outPath)

print("完成")