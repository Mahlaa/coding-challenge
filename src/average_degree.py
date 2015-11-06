# example of program that calculates the average degree of hashtags
import json, sys


ft2 = open("ft2.txt" , 'w')
count = 0
tweets = {}
my_queue_key = []
my_queue_val = []
my_graph = {}
tweetss = []
data = [{}]
month = {'jan' : '01' , 'feb' : '02' , 'march' : '03' , 'april' : '04' , 'may' : '05' , 'june' : '06' , 'july' : '07' , 'aug' : '08' , 'sep' : '09' ,  'oct' : '10' , 'nov' : '11' , 'dec' : '12'}

def update_graph(my_graph , my_queue_val):
	my_graph = {}
	for item in my_queue_val:
		for i in range(0,len(item)):
			for j in range(0,len(item)):
				if i != j:
					if item[i] not in my_graph:
						my_graph[item[i]] = []
					my_graph[item[i]].append(item[j])
	return my_graph



for line in open('tweets.txt'):
  try: 
    tweetss.append(json.loads(line))
  except:
    pass


for data in tweetss:
	hashtags = []
	if 'text' in data:
		for item in data['text'].encode('ascii', 'ignore').split():
			if item[0] == '#' and len(item) > 2:
				hashtags.append(item.lower())
		if  'created_at' in data:
			date = data['created_at']
			parts = []
			for item in date.split():
				parts.append(item)
			new_date = parts[5]+parts[2]+month[parts[1].lower()]+parts[3][0:2]+parts[3][3:5]+parts[3][6:]
	if len(hashtags) > 1:
		tweets[int(new_date)] = hashtags

#sort tweets according to its keys

for key , val in tweets.iteritems():

	# tweets in less than 60 minutes
	if(len(my_queue_key) > 0):
		while key - my_queue_key[0] > 60:
			my_queue_key = my_queue_key[1:]
			my_queue_val = my_queue_val[1:]
			if (len(my_queue_key) < 1):
				break

	my_queue_key.append(key)
	my_queue_val.append(val)
	my_graph = update_graph(my_graph , my_queue_val)
	summ = 0.00
	cnt = 0.00
	for ed , vert in my_graph.iteritems():
		summ += len(vert)
		cnt += 1
	ft2.write(str("{0:.2f}".format(summ/cnt)) + '\n')

