import tweepy
import time

def classify(user_id, api):
	"""Given a Twitter user's handle, returns the user's classification as a layman, expert, or celebrity."""
	if api.get_user(userID).followers_count > 1000: return 'celebrity'
	if api.get_user(userID).followers_count >= 100: return 'expert'
	return 'layman'
