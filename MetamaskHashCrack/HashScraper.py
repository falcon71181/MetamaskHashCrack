
from pickletools import long1
import re

from numpy import longcomplex

s = input("Enter : ")
result = re.search('data":"(.*)","iv', s)
result1 = re.search('iv":"(.*)","salt', s)
result2 = re.search('salt":"(.*)"}', s)
data = result.group(1)
iv = result1.group(1)
salt = result2.group(1)
print("$metamask$"+salt+"$"+iv+"$"+data)