import os

path = r'C:\Users\lihai\Desktop\9787564538132_boast'
index = 0
for file in os.listdir(path):
    if os.path.isfile(os.path.join(path, file)) == True:
        if file.find('.meta') > 0:
            os.remove(os.path.join(path, file))
            index += 1
            print(file, 'ok')
