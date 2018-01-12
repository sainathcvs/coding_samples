from collections import defaultdict
def getReco(followGraph_edges,likeGraph_edges,targetuser,minLikeThreshold):
	target_followers=[]
	tweets=[]
	for (target,frnd) in followGraph_edges:
		if target==targetuser and frnd not in target_followers:
			target_followers.append(frnd)
	for liker,tweet in likeGraph_edges:
		if tweet not in tweets:
			tweets.append(tweet)
	'''
	tweets_likes=[0 for i in range(len(tweets))]
	for liker,tweet in likeGraph_edges:
		index=tweets.index(tweet)
		if liker in target_followers:
			tweets_likes[index]+=1
	print tweets_likes
	fin_arr=[]
	for i in range(len(tweets_likes)):
		if tweets_likes[i]>=minLikeThreshold:
			fin_arr.append(tweets[i])

	'''
	tweets_likes=defaultdict(lambda:0)
	for liker,tweet in likeGraph_edges:
		index=tweets.index(tweet)
		if liker in target_followers:
			tweets_likes[tweet]+=1
	# print tweets_likes
	fin_arr=[]
	for tweet in sorted(tweets_likes,key=tweets_likes.get,reverse=True):
		if tweets_likes.get>minLikeThreshold:
			fin_arr.append(tweet)
	# '''
	return fin_arr

likeGraph_edges=[('A','T1'),('B','T2'),('B','T1'),('C','T3'),('E','T2'),('E','T3')]
minLikeThreshold=1
followGraph_edges=[('A','B'),('B','C'),('A','C'),('C','E')]
targetuser='A'
tweet_reco=getReco(followGraph_edges,likeGraph_edges,targetuser,minLikeThreshold)
print tweet_reco