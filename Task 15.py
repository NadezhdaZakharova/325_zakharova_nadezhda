import os

tree = list(os.walk('C:\dir'))

for i in tree:
    print(i)