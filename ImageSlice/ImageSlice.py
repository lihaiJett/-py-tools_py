import shutil  
import os
from PIL import Image
path =r'C:\Users\lihai\Desktop\ChooseMyself'
dstpath = r'C:\Users\lihai\Desktop\ChooseMyself\out'

def splitimage(src, rownum, colnum, dstpath):
    img = Image.open(src)
    w, h = img.size
    if rownum <= h and colnum <= w:
        print('Original image info: %sx%s, %s, %s' % (w, h, img.format, img.mode))
        print('开始处理图片切割, 请稍候...')

        s = os.path.split(src)
        if dstpath == '':
            dstpath = s[0]
        fn = s[1].split('.')
        basename = fn[0]
        ext = fn[-1]

        num = 0
        rowheight = h // rownum
        colwidth = w // colnum
        for r in range(rownum):
            for c in range(colnum):
                box = (c * colwidth, r * rowheight, (c + 1) * colwidth, (r + 1) * rowheight)
                img.crop(box).save(os.path.join(dstpath, basename + '_' + str(num) + '.' + ext))
                num = num + 1

        print('图片切割完毕，共生成 %s 张小图片。' % num)
    else:
        print('不合法的行列切割参数！')

index = 0
       
for file in os.listdir(path):
    if os.path.isfile(os.path.join(path,file))==True:
        if file.find('.jpg')>0:
            img = Image.open(os.path.join(path,file))
            w, h = img.size
            if w > h:
                splitimage(os.path.join(path,file),1,2,dstpath)
            index += 1
            print( file,'ok')
