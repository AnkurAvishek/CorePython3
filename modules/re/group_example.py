#!/usr/bin/python
import re

data = "Python is better then java"

matchObj = re.match( r'(.*) is (.*?) .*', data, re.M|re.I)

if matchObj:
   print("matchObj.group() : ", matchObj.group())
   print("matchObj.group(1) : ", matchObj.group(1))
   print("matchObj.group(2) : ", matchObj.group(2))
else:
   print("No match!!")