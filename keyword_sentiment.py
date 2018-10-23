import re
import tweepy
from textblob import TextBlob
import matplotlib.pyplot as plt
import numpy as np

class TwitterClient():
	def __init__(self):
		consumer_key='*******************'
		consumer_secret='**********************'

		access_token='***************************'
		access_token_secret='**********************'

		#log-in the app way
		self.auth= tweepy.OAuthHandler(consumer_key,consumer_secret)
		self.auth.set_access_token(access_token,access_token_secret)

		self.api=tweepy.API(self.auth)
	def get_tweets(self,query,count=10):
		#empty list to store parsed tweets
		tweets=[]

		#fetch tweets
		fetched_tweets=self.api.search(q=query,count=count)

		#parsing tweet one by one
		for tweet in fetched_tweets:
			#to save sentiment and text
			

			clean_tweet=re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t]) |(\w+:\/\/\S+)", " ", str(tweet))

			if tweet.retweet_count>0:
					
				if tweet not in tweets:
					tweets.append(clean_tweet)

				else:
					tweets.append(clean_tweet)
		return tweets



def main():
	api= TwitterClient()


	#create a variable that stores are the tweets having that word
	#for i in range(10000):
	public_tweetsb=api.get_tweets(query="bjp",count=2000)
	public_tweetsc=api.get_tweets(query="congress",count=2000)

	countb=0
	countc=0
	polb=0
	polc=0
	subb=0
	subc=0
	for tweet in public_tweetsb:
		print(tweet)
		analysis= TextBlob(tweet)
		print(analysis.sentiment.polarity)
		print(analysis.sentiment.subjectivity)
		countb+=1
		polb+=analysis.sentiment.polarity
		subb+=analysis.sentiment.subjectivity

	for tweet in public_tweetsc:
		print(tweet)
		analysis= TextBlob(tweet)
		print(analysis.sentiment.polarity)
		print(analysis.sentiment.subjectivity)
		countc+=1
		polc+=analysis.sentiment.polarity
		subc+=analysis.sentiment.subjectivity


	print("overall polarity of bjp =")
	print(polb/countb)
	polbp=(polb/countb)
	print("overall polarity of congress =")
	print(polc/countc)
	polcp=(polc/countc)


	print("overall subjectivity of bjp =")
	print(subb/countb)
	subbp=(subb/countb)
	print("overall subjectivity of congress =")
	print(subc/countc)
	subcp=(subc/countc)

	print("number of tweets analyzed having bjp as keyword=")
	print(countb)
	print("number of tweets analyzed having congress as keyword=")
	print(countc)

	objects=('BJP-SENTIMANT','CONGRESS-SENTIMENT','BJP-SUBJECTIVITY','CONGRESS-SUBJECTIVITY')
	values=[polbp,polcp,subbp,subcp]
	y_pos=np.arange(len(objects))

	barlist=plt.bar(y_pos,values,align='center',alpha=0.5)
	barlist[0].set_color('darkorange')
	barlist[1].set_color('blue')
	barlist[2].set_color('darkorange')
	barlist[3].set_color('blue')
	plt.xticks(y_pos,objects)
	plt.title('TWITTER POLITICS-INDIA')
	plt.show()


if __name__=="__main__":
		main()
