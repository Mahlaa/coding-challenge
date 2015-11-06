# example of program that calculates the number of tweets cleaned
import json, sys

ft1 = open("ft1.txt" , 'w')
count = 0

tweets = []
data = [{}]


for line in open('tweets.txt'):
  try: 
    tweets.append(json.loads(line))
  except:
    pass


for data in tweets:
	if 'text' in data:
		if(data['text'].encode('ascii', 'ignore') != data['text'].encode("utf8")):	
			count += 1
		ft1.write (data['text'].encode('ascii', 'ignore') + ' (timestamp:'+data['created_at']+')\n')

ft1.write(str(count)+' tweets contained unicode.')
