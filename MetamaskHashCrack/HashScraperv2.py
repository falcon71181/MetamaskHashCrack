from pickletools import long1
import re
from numpy import longcomplex

with open("hash.txt", "r") as input_file, open("result.txt", "w") as output_file:
    for line in input_file:
        s = line.strip()  # Remove any trailing whitespace or newline characters
        
        result = re.search('data":"(.*)","iv', s)
        result1 = re.search('iv":"(.*)","salt', s)
        result2 = re.search('salt":"(.*)"}', s)
        
        if result and result1 and result2:
            data = result.group(1)
            iv = result1.group(1)
            salt = result2.group(1)  
            output_file.write("$metamask$" + salt + "$" + iv + "$" + data + "\n")
            
print("Data extraction complete. Results written to result.txt.")
