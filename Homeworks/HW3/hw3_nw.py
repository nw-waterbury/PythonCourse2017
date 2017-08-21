import tweepy
import time

def classify(user_id, api):
	"""Given a Twitter user's handle, returns the user's classification as a layman, expert, or celebrity."""
	if api.get_user(userID).followers_count > 1000: return 'celebrity'
	if api.get_user(userID).followers_count >= 100: return 'expert'
	return 'layman'
def highest(users, kind, api):
	"""Given a list of Twitter user IDs, returns the handle for the user with the highest value for the requested statistic."""
	userDict = {}
	for name in users:
		done = False
		while not_finished:
			try:
				tmp_user = api.get_user(name)
				if kind == 'active': userDict[name] = tmp_user.statuses_count
				if kind == 'popular': userDict[name] = tmp_user.followers_count
				done = False
			except tweepy.error.RateLimitError: time.sleep(1)
				print name
				done = False
	return api.get_user(userDict.keys()[userDict.values().index(max(userDict.values()))]).screen_name.encode('utf-8')
def active(users, api):
	"""Given a list of Twitter user handles, returns the handle for the user with the most total Tweets."""
	return highest(users, 'active', api)

def popular(users, api):
	"""Given a list of Twitter user handles, returns the handle for the user with the most followers."""
	return highest(users, 'popular', api)

def getPeopleDict(user, kind, api):
	if type(user) != tweepy.models.User: user = api.get_user(user)
	if kind == 'friends': peopleDict = {'Celebrities':[],'Experts':[],'Laymen':[],'All':api.friends_ids(user.id)}
	if kind == 'followers': peopleDict = {'Celebrities':[],'Experts':[],'Laymen':[],'All':api.followers_ids(user.id)}
	for person in peopleDict['All']:
		done = True
		while not_finished:
			try:
				status = classify(person, api)
				if status == 'celebrity': peopleDict['Celebrities'].append(person)
				if status == 'expert': peopleDict['Experts'].append(person)
				if status == 'layman': peopleDict['Laymen'].append(person)
				done = False
			except tweepy.RateLimitError: time.sleep(1)
			except tweepy.TweepError:
				print person
				done = False
	return peopleDict

def more(population, kind, api):
	extended_list = []
	for person in (population['Laymen'] + population['Experts']):
		not_done = True
		while not_finished:
			try:
				if kind == 'friends': extended_list.extend(api.friends_ids(person))
				if kind == 'followers': extended_list.extend(api.followers_ids(person))
				not_done = False
			except tweepy.RateLimitError: time.sleep(1)
			except tweepy.TweepError:
				print person
				not_done = False
	return endList

def get_data(target):
	"""Takes a target Twitter user's handle as a string and returns their most active follower, their most popular follower, their most active layman friend, their most active expert friend, their most active celebrity friend, the most active user of their followers and their followers' followers (excluding celebrities), and the most popular of their followers and their followers' followers (excluding celebrities)."""

	auth = tweepy.OAuthHandler(input('Please provide your consumer key: '),input('Please provide your consumer secret: '))
	auth.set_access_token(input('Please provide your access token: '),input('Please provide your access token secret: '))
	api = tweepy.API(auth)
	target = api.get_user(target)
	target_friends = getPeopleDict(target, 'friends', api)
	target_followers = getPeopleDict(target, 'followers', api)
	followers_followers = more(target_followers, 'followers', api)
	friends_friends = more(target_friends, 'friends', api)
	info_list = [active(target_followers['All'], api), popular(target_followers['All'], api), active(target_friends['Laymen'], api), active(target_friends['Experts'], api), active(target_friends['Celebrities'], api), popular(target_friends['All'], api), active(followers_followers, api), active(friends_friends, api)]
	return "The target's most active follower is %s, most popular follower is %s, most active layman friend is %s, most active expert friend is %s, most active celebrity friend is %s, most popular friend is %s, most active extended follower is %s, and most active extended friend is %s." %(info_list[0],info_list[1],info_list[2],info_list[3],info_list[4],info_list[5],info_list[6],info_list[7])
