import tweepy
import time

def classify(user_id, api):
	"""Takes a user's id name and returns their classification as stipulated"""
	if api.get_user(user_id).followers_count > 1000: return 'celebrity'
	if api.get_user(user_id).followers_count >= 100: return 'expert'
	return 'layman'
def highest(users, kind, api):
	"""Takes id and requested statistic, returns name with the highest value"""
	userDict = {}
	for name in users:
		not_done = True
		while not_done:
			try:
				tmp_user = api.get_user(name)
				if kind == 'active': userDict[name] = tmp_user.statuses_count
				if kind == 'popular': userDict[name] = tmp_user.followers_count
				not_done = False
			except tweepy.error.RateLimitError: time.sleep(1)
			except tweepy.TweepError:
				print name
				not_done = False
	return api.get_user(userDict.keys()[userDict.values().index(max(userDict.values()))]).screen_name.encode('utf-8')
def active(users, api):
	"""Takes a list of users, uses 'highest' to return most active user"""
	return highest(users, 'active', api)

def popular(users, api):
	"""Takes a list of users, uses 'highest' to return most active user"""
	return highest(users, 'popular', api)

def get_dict_of_people(user, kind, api):
	"""Given a user, classifies friends and followers in a dictionary """
	if type(user) != tweepy.models.User: user = api.get_user(user)
	if kind == 'friends': peopledict = {'Celebrities':[],'Experts':[],'Laymen':[],'All':api.friends_ids(user.id)}
	if kind == 'followers': peopledict = {'Celebrities':[],'Experts':[],'Laymen':[],'All':api.followers_ids(user.id)}
	for person in peopledict['All']:
		not_done = True
		while not_done:
			try:
				status = classify(person, api)
				if status == 'celebrity': peopledict['Celebrities'].append(person)
				if status == 'expert': peopledict['Experts'].append(person)
				if status == 'layman': peopledict['Laymen'].append(person)
				not_done = False
			except tweepy.RateLimitError: time.sleep(1)
			except tweepy.TweepError:
				print person
				not_done = False
	return peopledict

def more(population, kind, api):
	"""Given a dictionary, obtains list of second degree contacts """
	extended_list = []
	for person in (population['Laymen'] + population['Experts']):
		not_done = True
		while not_done:
			try:
				if kind == 'friends': extended_list.extend(api.friends_ids(person))
				if kind == 'followers': extended_list.extend(api.followers_ids(person))
				not_done = False
			except tweepy.RateLimitError: time.sleep(1)
			except tweepy.TweepError:
				print person
				not_done = False
	return extended_list

def get_data(target):
	"""Takes a string of a user name and returns the stipulated statistics"""

	auth = tweepy.OAuthHandler(input('Please provide your consumer key: '),input('Please provide your consumer secret: '))
	auth.set_access_token(input('Please provide your access token: '),input('Please provide your access token secret: '))
	api = tweepy.API(auth)
	target = api.get_user(target)
	target_friends = get_dict_of_people(target, 'friends', api)
	target_followers = get_dict_of_people(target, 'followers', api)
	followers_followers = more(target_followers, 'followers', api)
	friends_friends = more(target_friends, 'friends', api)
	info_list = [active(target_followers['All'], api), popular(target_followers['All'], api), active(target_friends['Laymen'], api), active(target_friends['Experts'], api), active(target_friends['Celebrities'], api), popular(target_friends['All'], api), active(followers_followers, api), active(friends_friends, api)]
	return "The target's most active follower is %s, most popular follower is %s, most active layman friend is %s, most active expert friend is %s, most active celebrity friend is %s, most popular friend is %s, most active extended follower is %s, and most active extended friend is %s." %(info_list[0],info_list[1],info_list[2],info_list[3],info_list[4],info_list[5],info_list[6],info_list[7])

#Ran this to test
#get_data("SamBoyea")
