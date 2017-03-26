#! /usr/bin/python
def display(lines):
   for line in lines:
      print(line)
def count(fil):
   cortana=[]
   siri=[]
   talk=open(fil,'r')
   text=talk.read()
   text_str=str(text)
   lines=text_str.split("\n")
   for line in lines:
      if "cortana" in line:
         line=line.replace("cortana","")
         cortana.append(line)
      elif "siri" in line:
         line=line.replace("siri","")
         siri.append(line)
   talk.close()
   print("cortana:")
   display(cortana)
   print("siri:")
   display(siri)


count('data_set.txt')
