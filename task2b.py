#! /usr/bin/python
def display(lines):
   for line in lines:
      print(line)
def count(fil):
   task={"what","when","how","why"}
   cortana_t=[]
   cortana_s=[]
   siri_t=[]
   siri_s=[]
   talk=open(fil,'r')
   text=talk.read()
   text_str=str(text)
   lines=text_str.split("\n")
   for line in lines:
      if "cortana" in line:
         if any(x in line for x in task) :
            cortana_t.append(line)
         else:
            cortana_s.append(line)
      elif "siri" in line:
         if any(x in line for x in task):
            siri_t.append(line)
         else:
            siri_s.append(line)
   talk.close()
   print("cortana:")
   print("task:")
   display(cortana_t)
   print("statement:")
   display(cortana_s)
   print("siri:")
   print("task:")
   display(siri_t)
   print("statement:")
   display(siri_s)


count('data_set.txt')
