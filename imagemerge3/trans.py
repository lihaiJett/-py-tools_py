#!/usr/bin/python
 
from PIL import Image
import os
import re

# 当前目录
# 后缀需为png

arr = []
p1 = "1.png"
p2 = "2.png"
p3 = "3.png"

for s in os.listdir("."):   
    #newDir=os.path.join(dir,s)
    #GetFileList(newDir, fileList)
    temp = re.findall(r'(.*)'+p1+'$',s)
    if(temp):
        temp = temp[0]
        print (temp+"开始检测")
        if(os.path.exists("./"+temp+p2)):            
            if(os.path.exists("./"+temp+p3)):
                arr.append(temp)
            else:
                print ("缺少文件"+"./"+temp+p3);
        else:
            print ("缺少文件"+"./"+temp+p2);

#创建文件夹
if(os.path.exists("./out")==False):
    os.mkdir(r"./out");

for name in arr:
    print ("开始处理"+name)
    fromImage = ["","",""]
    fromImage[0] = Image.open(name+p1)
    fromImage[1] = Image.open(name+p2)
    fromImage[2] = Image.open(name+p3)
    # 检查3张图片是否尺寸一致    
    if(fromImage[0].size != fromImage[1].size or fromImage[1].size != fromImage[2].size):
        print("三张图片尺寸不一致")
        continue

    toImage = Image.new('RGBA',(fromImage[0].size[0]*3,fromImage[0].size[1]))
    for i in range(3):
        loc = (i * fromImage[0].size[0], 0)
        #print(loc)
        toImage.paste(fromImage[i], loc)

    outPath = "out"+"/"+name+'.png'
    toImage.save(outPath)
    print("合并完成"+outPath)

