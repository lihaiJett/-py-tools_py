import os
import shutil

#这个路径不能用反斜杠
path = r'C:/Users/lihai/Desktop/Unity-iPhone 2018-02-02 20-11-20/Unity-iPhone2018020220'
installHref = 'https://raw.githubusercontent.com/lihaiJett/weseelive/master/test/'
image1 = 'https://raw.githubusercontent.com/lihaiJett/weseelive/master/01.jpg'
image2 = 'https://raw.githubusercontent.com/lihaiJett/weseelive/master/02.jpg'
plistPlaceHolder = '<string>https://<'



folder = path[path.rindex('/')+1: len(path)]
ipaName = ''


for file in os.listdir(path):
    if os.path.isfile(os.path.join(path, file)):
        if file.find('install.html') > 0:
            # 判断inatall文件是否存在，如果不存在则生成，如果存在则先删除
            os.remove(os.path.join(path, file))
        if file.find('.ipa') > 0:
            # 获取ipa文件名
            ipaName = file
shutil.copyfile('install.html', os.path.join(path, 'install.html'))




#替换install.html中的文本
with open(os.path.join(path, 'install.html'), 'r', encoding='utf-8') as r:
    lines = r.readlines()
with open(os.path.join(path, 'install.html'), 'w', encoding='utf-8') as w:
    for l in lines:
        w.write(l.replace('placeholder', installHref+folder+"/manifest.plist"))

#替换manifest.plist中的文字
i = 0
texts = [installHref+folder+'/'+ipaName, image1, image2]
with open(os.path.join(path, 'manifest.plist'), 'r', encoding='utf-8') as r:
    lines = r.readlines()
with open(os.path.join(path, 'manifest.plist'), 'w', encoding='utf-8') as w:
    for l in lines:
        if l.find(plistPlaceHolder) > 0:
            print(l)
            print(i)
            w.write(l.replace(plistPlaceHolder, '<string>'+texts[i]+'<'))
            i += 1
        else:
            w.write(l)

# for file in os.listdir(path):
#     if os.path.isfile(os.path.join(path, file)) == True:
#         if file.find('.jpg') > 0:
#             newname = "t" + str(index) + '.jpg'
#             os.rename(os.path.join(path, file), os.path.join(path, newname))
#             index += 1
#             print(file, 'ok')



