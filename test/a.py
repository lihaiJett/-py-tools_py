import os, sys
import subprocess
import shutil

with open(os.path.join('runscenesdk/', 'build.gradle'), 'r', encoding='utf-8') as r:
    lines = r.readlines()
with open(os.path.join('runscenesdk/', 'build.gradle'), 'w', encoding='utf-8') as w:
    b = 0
    for l in lines:
        if b == 0:
            w.write(l)
        if l.find("//#dependencies start#//") > 0:
            b = 1
            w.write('''     api project(':runscene')
     api project(':runsceneinterface')
     api project(':runscenekeyboard')
     api project(dependencies_ext["vrsdk"]) \n''')
        if l.find("//#dependencies stop#//") > 0:
            b = 0
            w.write(l)

