import tweepy
import time

def classify(user_id, api):
	"""Given a Twitter user's handle, returns the user's classification as a layman, expert, or celebrity."""
	if api.get_user(userID).followers_count > 1000: return 'celebrity'
	if api.get_user(userID).followers_count >= 100: return 'expert'
	return 'layman'
def highest(userList, kind, api):
	"""Given a list of Twitter user IDs, returns the handle for the user with the highest value for the requested statistic."""
	userDict = {}
	for id in userList:
		error = False
		while not_finished:
			try:
				tmp_user = api.get_user(userID)
				if kind == 'active': userDict[userID] = tmp_user.statuses_count
				if kind == 'popular': userDict[userID] = tmp_user.followers_count
				not_finished = False
			except tweepy.error.RateLimitError: time.sleep(1)
				print userID
				not_finished = False
	return api.get_user(userDict.keys()[userDict.values().index(max(userDict.values()))]).screen_name.encode('utf-8')
