"""
遍历文件夹下的文件，按照拼音和数字排序，按顺序修改名称
"""

import os
from pathlib import Path
import re

DIR = r"C:\Users\lihai\Desktop\Desktop\弹药\手榴弹\进攻手榴弹"
R_Name = 'Offensive grenade'

def cmp(x):
    num = re.sub('\D', '', str(x))
    numR = num.zfill(3)
    x = str(x).replace(num,numR)
    return x.encode('gbk')

# 遍历文件夹
a = Path(DIR).rglob('*')
out = sorted(a, key=cmp)
for index,f in enumerate(out):
    target = str(f.parent) +'/'+ R_Name+' -'+str(index+1)+f.suffix
    f.rename(target)
    print(target)

# for root,dirs,files in os.walk(DIR):
#     files.sort()
#     for f in files:
#         print(os.path.join(root, f))