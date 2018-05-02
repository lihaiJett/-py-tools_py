import tinify  
import os
tinify.key='zJjT9Yzo5xFbGwYLweVlh1nwxfwmi4Ek'  
pngpath = input("输入路径")
pngList = []
optList = []

for i in os.listdir(pngpath):
    if os.path.splitext(i)[1] == ".png":
        pngList.append(os.path.join(pngpath,i))
        opt = pngpath + 'optimize'
        if not os.path.exists(opt):
            os.makedirs(opt)
        optList.append(os.path.join(opt,i))
pngSum = len(pngList)

i = 0
for srcPath in pngList:
    source = tinify.from_file(srcPath)
    source.to_file(optList[i])
    i += 1
    percent = i/pngSum *100
    print('complete percent:%10.8s%s' % (str(percent), '%'), end='\r')

# for i in os.listdir(pngpath):
#     if os.path.splitext(i)[1]==".png":
#         source=tinify.from_file(os.path.join(pngpath,i))
#         opt=pngpath+'optimize'
#     if not os.path.exists(opt):
#         os.makedirs(opt)
#     source.to_file(os.path.join(opt,i))
# print('over')
