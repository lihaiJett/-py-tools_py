import os
path =r'C:\Users\lihai\Desktop\失踪的小松糕\压缩'
index = 0
for file in os.listdir(path):
    if os.path.isfile(os.path.join(path,file))==True:
        if file.find('.jpg')>0:
            newname = "c"+ str(index) +'.jpg'
            os.rename(os.path.join(path,file),os.path.join(path,newname))
            index += 1
            print( file,'ok')
