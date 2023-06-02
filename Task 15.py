import os
path_dir = 'C:\dir'
images = []
def print_docs(path_dir):
    cont = os.listdir(path_dir)
    for file in cont:
        print (file)
        if os.path.isdir(os.path.join(path_dir, file)):
            images.append(file)
    return
print_docs(path_dir)

print ('h')
import os

tree = list(os.walk('C:\dir'))

for i in tree:
    print(i)