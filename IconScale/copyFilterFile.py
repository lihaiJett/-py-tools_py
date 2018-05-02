import shutil  
import os
pngpath = input("输入路径")
pngList = []
optList = []

for i in os.listdir(pngpath):
    if os.path.splitext(i)[1] == ".jpg":
        pngList.append(os.path.join(pngpath,i))
        opt = pngpath + 'JpgFile'
        if not os.path.exists(opt):
            os.makedirs(opt)
        optList.append(os.path.join(opt,i))
pngSum = len(pngList)

i = 0
for srcPath in pngList:
    print(srcPath + '__' + optList[i])
    shutil.copyfile(srcPath,optList[i])
    i += 1
    percent = i/pngSum *100
    #print('complete percent:%10.8s%s' % (str(percent), '%'), end='\r')

