import re

txt = input("nhập email cần tìm : ")
x = re.findall("([\w]+@[\w]+[\w][+.][\w]+[+.][\w]+)",txt)
if x:
  print(x,"")
else:
  x = re.findall("([\w]+@[\w]+[+.][\w]+)",txt)
  print(x,"")