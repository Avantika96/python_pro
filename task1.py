#! /usr/bin/python
def count(fil):
   x=0
   y=0
   talk=open(fil,'r')
   text=talk.read()
   text_str=str(text)
   lines=text_str.split("\n")
   for line in lines:
      if "cortana" in line:
         x+=1
      elif "siri" in line:
         y+=1
   talk.close()
   print("cortana:")
   print(x)
   print("siri:")
   print(y)
count('data_set.txt')
