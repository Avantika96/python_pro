#! /usr/bin/python
import redis
redis_db = redis.StrictRedis(host='localhost', port=6379, db=0)
def count(fil): 
   #redis_db = redis.StrictRedis(host='localhost', port=6379, db=0)   
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
   redis_db.rpush('cor_t', cotana_t)
   redis_db.rpush('cor_s', cotana_s)
   redis_db.rpush('sir_t', siri_t)
   redis_db.rpush('sir_t', siri_s)
   keys = redis_.keys('*')
   for key in keys:
       type = redis_db.type(key)
       if type == KV:
          val = redis_db.get(key)
       if type == HASH:
          vals = redis_db.hgetall(key)
       if type == ZSET:
          vals = redis_db.zrange(key, 0, -1)

count('data_set.txt')
