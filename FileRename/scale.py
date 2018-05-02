import os
from PIL import Image
import re

path =r'C:\Users\lihai\Desktop\图片素材'

index = 0
    
def fixed_size(cls, width, height):  
    """按照固定尺寸处理图片"""  
    im = Image.open(cls)  
    out = im.resize((width, height),Image.ANTIALIAS)  
    out.save(cls)        
for file in os.listdir(path):
    if os.path.isfile(os.path.join(path,file))==True:
        if file.find('.jpg')>0:
            #newname = "t"+ str(index) +'.jpg'
            #os.rename(os.path.join(path,file),os.path.join(path,newname))
            fixed_size(os.path.join(path,file),680,454)
            index += 1
            print( file,'ok')
