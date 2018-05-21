from TwitterSearch import *
from textblob import TextBlob
import sys
reload(sys)
sys.setdefaultencoding('utf8')

filepath = "2017.txt"
try:
	fp = open("2017.txt","r")
	di = { }
	for line in fp.read().splitlines():
		cnt = 0
		score = 0
		temp = 0;
		#print line
	
		
		tso = TwitterSearchOrder() 
		tso.set_keywords([line]) 
		tso.set_language('en') 
		tso.set_include_entities(False)
		tso.set_count(100)

# it's about time to create a TwitterSearch object with our secret tokens
		ts = TwitterSearch(
				consumer_key = "XXXX",
        		consumer_secret = "YY",
        		access_token = "ZZ",
        		access_token_secret = "MM"
		 )


 # this is where the fun actually starts :)
		for tweet in ts.search_tweets_iterable(tso):
			if(cnt<20):
				analysis = TextBlob(tweet['text'])
				cnt=cnt+1;
				temp = temp+1;
				if analysis.sentiment.polarity > 0:
					#print '1'
					score=score+1
				elif analysis.sentiment.polarity == 0:
					#print '0'
					score = score;
				else:
					score=score-1
			else:
				break
	#F.write(tweet['text'])
			#print(tweet['text'])
		x = float(score)/float(temp)
		#print x
		di.update({line : x})
	d_view = [ (v,k) for k,v in di.iteritems() ]
	d_view.sort(reverse=True) # natively sort tuples by first element
	for v,k in d_view:
			print v, k
		
except TwitterSearchException as e: # take care of all those ugly errors if there are some
	print(e)