#!/usr/bin/python
# -*- coding: utf-8 -*-

# ( -- IMPORTS -- ) #
import requests
import urllib3
import thread
import time
import json
urllib3.disable_warnings()

# ( -- LOGO * INFO -- ) #
bugs = '''
   ____ _______        _____ _____ _____ _____ ____       ___ _____ _  __
  / __ \_   _\ \      / /_ _|_   _|_   _| ____|  _ \     / _ \_   _| |/ /
 / / _` || |  \ \ /\ / / | |  | |   | | |  _| | |_) |___| (_) || | | ' / 
| | (_| || |   \ V  V /  | |  | |   | | | |___|  _ <_____\__, || | | . \ 
 \ \__,_||_|    \_/\_/  |___| |_|   |_| |_____|_| \_\      /_/ |_| |_|\_\
  \____/                                                                 
\n[$] BUGS TWITTER TOOLKIT TOOL V6.1.
[$] URL = ('https://www.Brazzers.com/').
[$] SCRIPT PROGRAMMED BY BUGS WITH PYTHON2.
'''
#################################
# ( -- PROGRAMMED BY @BUGS -- ) #
#################################

# ( -- FULL API SCRIPT -- ) #

def login(user, passwd):
	log_headers = {
		'Origin': 'https://twitter.com',
		'Upgrade-Insecure-Requests': '1',
		'Content-Type': 'application/x-www-form-urlencoded',
		'User-Agent': 'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
		'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
		'Referer': 'https://twitter.com/login',
		'Cookie': '_ga=GA1.2.1741801804.1516677655; kdt=1GBDqOYqnYDGz81JlSDYcjFH4FDuWFg8G2FdQEj7; remember_checked_on=1; eu_cn=1; tfw_exp=0; csrf_same_site_set=1; csrf_same_site=1; lang=en; ct0=52f94907f7b418398910f8d16abdf3f3; _gid=GA1.2.663121923.1530365541; gt=1013053103594246144; _twitter_sess=BAh7CiIKZmxhc2hJQzonQWN0aW9uQ29udHJvbGxlcjo6Rmxhc2g6OkZsYXNo%250ASGFzaHsABjoKQHVzZWR7ADoPY3JlYXRlZF9hdGwrCJvryVBkAToHaWQiJWFj%250AMTZmOTRiNjJlMzA0YzE1ZTU4Yzg1YmFlMDY4ZGY5Ogxjc3JmX2lkIiVlOTcw%250AMjgwMGZkOGQ0ZTZkODFiMjkwM2JmMTY3MGMwNzoJdXNlcmwrCQKQF%252BuJJk8M--5d9550e3924bc595f8af3f4eaadb79d339e7942b; dnt=1; personalization_id="v1_eq3DN2SFTW7rzO4fGurW/Q=="; guest_id=v1%3A153036659415849053; _gat=1'
	}
	log_data = 'session%5Busername_or_email%5D='+user+'&session%5Bpassword%5D='+passwd+'&authenticity_token=a1c4f26ebdf4f092fe2efa2425273d70f6f3e183&ui_metrics=%7B%22rf%22%3A%7B%22a824aeac96e5632a88665f37fed2714e42e565f160e601db2895d6232f1cae71%22%3A-50%2C%22a4b68b74e433706e01e9c65a5b9f7b67e8ab170b2e35a193fb493084a5ddba0b%22%3A-62%2C%22fb8b4c522f380b881809dbb389e64486c9a69ede9902b8b8acea8181ac86d49a%22%3A-1%2C%22a2466e14241541ad7089c5392f5de2ed39e6e852f7bc1237dee9d2c315a6cc4b%22%3A16%7D%2C%22s%22%3A%22HRkGDLFtywknLQuBzp0PGdsUmSgptx3thG7zFQNthuC1weLWS35g9zYhLLpSdQojZbLXkrhYfmfhpP4uetdVCTKWRbbOm2RyJeF6kQHqL2PD8eTUAu5e93J3-d6LmRsyI-qoAbzSHAV-5kMGB6KeO1wrthGiqRUfmpHD16WHqm4-2yNqYrah9J4WcHg6vDCzL8EkZYeAnjjEtQYUlvJIN4ephJ8h7dA4RnT8PSaVAKf81Cq5mXDnflHx4oL-Ee1BkEK_rNjqvTO649AWOiAi2fo6wujZvyjpBzXG9NGj54N67Sj7x8l5sSi7VKIo2Zj5hQhQeOLZ_cE43j_0CM3AhwAAAWRQ9STz%22%7D&scribe_log=&redirect_after_login=&authenticity_token=a1c4f26ebdf4f092fe2efa2425273d70f6f3e183&remember_me=1'

	req = requests.post('https://twitter.com/sessions', data=log_data, headers=log_headers)
	src = req.content
	#// print src
	global status;
	status = 'NORMAL'
	if 'Add photos or video' in src or 'The username and password you entered did not match our records.' not in src:
		print '[X] LOGGED IN WITH [ '+user+':'+passwd+' ].'
		status = 'SUCCESS'
	else:
		print '[X] FAILED LOGIN WITH [ '+user+':'+passwd+' ].'
		status = 'INVALID'
# ---------------------------------- ## ---------------------------------- ## ---------------------------------- #
def follow(user):
	# //USER URL LIKE : sirbugsbunny
	try:
		user_id = requests.get('https://twitter.com/'+user).content.split('fileNav" role="navigation" data-user-id="')[1].split('"')[0]
	except:
		print '[X] ERROR X> PLEASE CHECK YOUR USERNAMEa.\n>>>'
		time.sleep(10000)
	flw_headers = {
		'Origin': 'https://twitter.com',
		'x-csrf-token': '52f94907f7b418398910f8d16abdf3f3',
		'authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAAPYXBAAAAAAACLXUNDekMxqa8h%2F40K4moUkGsoc%3DTYfbDKbT3jJPCEVnMYqilB28NHfOPqkca3qaAxGfsyKCs0wRbw',
		'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
		'Accept': 'application/json, text/javascript, */*; q=0.01',
		'User-Agent': 'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
		'x-twitter-auth-type': 'OAuth2Session',
		'X-Twitter-Active-User': 'yes',
		'Referer': 'https://twitter.com/'+user,
		'Cookie': '_ga=GA1.2.1741801804.1516677655; kdt=1GBDqOYqnYDGz81JlSDYcjFH4FDuWFg8G2FdQEj7; remember_checked_on=1; eu_cn=1; tfw_exp=0; csrf_same_site_set=1; csrf_same_site=1; ct0=52f94907f7b418398910f8d16abdf3f3; _gid=GA1.2.663121923.1530365541; lang=en; gt=1013053103594246144; _twitter_sess=BAh7CiIKZmxhc2hJQzonQWN0aW9uQ29udHJvbGxlcjo6Rmxhc2g6OkZsYXNo%250ASGFzaHsABjoKQHVzZWR7ADoPY3JlYXRlZF9hdGwrCJvryVBkAToHaWQiJWFj%250AMTZmOTRiNjJlMzA0YzE1ZTU4Yzg1YmFlMDY4ZGY5Ogxjc3JmX2lkIiVlOTcw%250AMjgwMGZkOGQ0ZTZkODFiMjkwM2JmMTY3MGMwNzoJdXNlcmwrCQKQF%252BuJJk8M--5d9550e3924bc595f8af3f4eaadb79d339e7942b; personalization_id="v1_7m2Q33dmYxAzGSYbfYcMeQ=="; guest_id=v1%3A153036696777961505; ads_prefs="HBERAAA="; twid="u=886970025411842050"; auth_token=0bfe39805ef7e689edcba747f4d2c2223d918722'
	}
	flw_data = 'challenges_passed=false&handles_challenges=1&include_blocked_by=true&include_blocking=true&include_can_dm=true&include_followed_by=true&include_mute_edge=true&skip_status=true&user_id='+user_id
	
	flw_req = requests.post('https://api.twitter.com/1.1/friendships/create.json', data=flw_data, headers=flw_headers)
	# //print flw_req.json()
	if '"name"' in flw_req.content or '"url"' in flw_req.content or '"description"' in flw_req.content:
		print '[X] FOLLOWED USER [ '+user+' ].\n'
	else:
		print '[X] UNEXPECTED ERROR HAPPENED [PASSED].\n'
		pass
# ---------------------------------- ## ---------------------------------- ## ---------------------------------- #
def like(tweet_url):
	# //TWEET URL LIKE : https://twitter.com/sirbugsbunny/status/1006208122673823744/
	try:
		user_id = tweet_url.split('https://twitter.com/')[1].split('/')[0]
		tweet_id = tweet_url.split('https://twitter.com/'+user_id+'/status/')[1].split('/')[0]
		# //print '[X] USER ID -> '+user_id
		# //print '[X] TWEET ID -> '+tweet_id
	except:
		print '[X] ERROR X> PLEASE CHECK YOUR TWEET URL.\n>>>'
		time.sleep(10000)
	like_headers = {
		'Origin': 'https://twitter.com',
		'x-csrf-token': '52f94907f7b418398910f8d16abdf3f3',
		'authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAAPYXBAAAAAAACLXUNDekMxqa8h%2F40K4moUkGsoc%3DTYfbDKbT3jJPCEVnMYqilB28NHfOPqkca3qaAxGfsyKCs0wRbw',
		'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
		'Accept': 'application/json, text/javascript, */*; q=0.01',
		'User-Agent': 'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
		'x-twitter-auth-type': 'OAuth2Session',
		'X-Twitter-Active-User': 'yes',
		'Referer': tweet_url,
		'Cookie': '_ga=GA1.2.1741801804.1516677655; kdt=1GBDqOYqnYDGz81JlSDYcjFH4FDuWFg8G2FdQEj7; remember_checked_on=1; eu_cn=1; tfw_exp=0; csrf_same_site_set=1; csrf_same_site=1; ct0=52f94907f7b418398910f8d16abdf3f3; _gid=GA1.2.663121923.1530365541; lang=en; gt=1013053103594246144; _twitter_sess=BAh7CiIKZmxhc2hJQzonQWN0aW9uQ29udHJvbGxlcjo6Rmxhc2g6OkZsYXNo%250ASGFzaHsABjoKQHVzZWR7ADoPY3JlYXRlZF9hdGwrCJvryVBkAToHaWQiJWFj%250AMTZmOTRiNjJlMzA0YzE1ZTU4Yzg1YmFlMDY4ZGY5Ogxjc3JmX2lkIiVlOTcw%250AMjgwMGZkOGQ0ZTZkODFiMjkwM2JmMTY3MGMwNzoJdXNlcmwrCQKQF%252BuJJk8M--5d9550e3924bc595f8af3f4eaadb79d339e7942b; personalization_id="v1_7m2Q33dmYxAzGSYbfYcMeQ=="; guest_id=v1%3A153036696777961505; ads_prefs="HBERAAA="; twid="u=886970025411842050"; auth_token=0bfe39805ef7e689edcba747f4d2c2223d918722'
	}
	like_data = 'id='+tweet_id+'&tweet_stat_count=2'
	
	like_req = requests.post('https://api.twitter.com/1.1/favorites/create.json', data=like_data, headers=like_headers)
	# //print like_req.json()
	if '"name"' in like_req.content or '"id"' in like_req.content or '"description"' in like_req.content:
		print '[X] LIKED TWEET [ '+tweet_id+' ].\n'
	else:
		print '[X] UNEXPECTED ERROR HAPPENED [PASSED].\n'
		pass
# ---------------------------------- ## ---------------------------------- ## ---------------------------------- #
def comment(tweet_url, comment):
	# //TWEET URL LIKE : https://twitter.com/sirbugsbunny/status/1006208122673823744/
	try:
		user_id = tweet_url.split('https://twitter.com/')[1].split('/')[0]
		tweet_id = tweet_url.split('https://twitter.com/'+user_id+'/status/')[1].split('/')[0]
		# //print '[X] USER ID -> '+user_id
		# //print '[X] TWEET ID -> '+tweet_id
	except:
		print '[X] ERROR X> PLEASE CHECK YOUR TWEET URL.\n>>>'
		time.sleep(10000)
	com_headers = {
		'Origin': 'https://twitter.com',
		'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
		'Accept': 'application/json, text/javascript, */*; q=0.01',
		'User-Agent': 'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
		'X-Requested-With': 'XMLHttpRequest',
		'x-twitter-auth-type': 'OAuth2Session',
		'X-Twitter-Active-User': 'yes',
		'Referer': tweet_url,
		'Cookie': '_ga=GA1.2.1741801804.1516677655; kdt=1GBDqOYqnYDGz81JlSDYcjFH4FDuWFg8G2FdQEj7; remember_checked_on=1; eu_cn=1; tfw_exp=0; csrf_same_site_set=1; csrf_same_site=1; ct0=52f94907f7b418398910f8d16abdf3f3; _gid=GA1.2.663121923.1530365541; lang=en; gt=1013053103594246144; _twitter_sess=BAh7CiIKZmxhc2hJQzonQWN0aW9uQ29udHJvbGxlcjo6Rmxhc2g6OkZsYXNo%250ASGFzaHsABjoKQHVzZWR7ADoPY3JlYXRlZF9hdGwrCJvryVBkAToHaWQiJWFj%250AMTZmOTRiNjJlMzA0YzE1ZTU4Yzg1YmFlMDY4ZGY5Ogxjc3JmX2lkIiVlOTcw%250AMjgwMGZkOGQ0ZTZkODFiMjkwM2JmMTY3MGMwNzoJdXNlcmwrCQKQF%252BuJJk8M--5d9550e3924bc595f8af3f4eaadb79d339e7942b; personalization_id="v1_7m2Q33dmYxAzGSYbfYcMeQ=="; guest_id=v1%3A153036696777961505; ads_prefs="HBERAAA="; twid="u=886970025411842050"; auth_token=0bfe39805ef7e689edcba747f4d2c2223d918722'
	}

	com_data = 'authenticity_token=a1c4f26ebdf4f092fe2efa2425273d70f6f3e183&auto_populate_reply_metadata=true&batch_mode=off&in_reply_to_status_id='+tweet_id+'&is_permalink_page=true&page_context=profile&place_id=&status='+comment+'&tagged_users='
	
	com_req = requests.post('https://twitter.com/i/tweet/create', data=com_data, headers=com_headers)
	# //print com_req.json()
	if '"in_reply_to_status_id"' in com_req.content or '"tweet_id"' in com_req.content or '"tweet_html"' in com_req.content:
		print '[X] COMMENTED ON TWEET [ '+tweet_id+' ].\n'
	else:
		print '[X] UNEXPECTED ERROR HAPPENED [PASSED].\n'
		pass
# ---------------------------------- ## ---------------------------------- ## ---------------------------------- #
def retweet(tweet_url, message):
	# //TWEET URL LIKE : https://twitter.com/sirbugsbunny/status/1006208122673823744/
	try:
		user_id = tweet_url.split('https://twitter.com/')[1].split('/')[0]
		tweet_id = tweet_url.split('https://twitter.com/'+user_id+'/status/')[1].split('/')[0]
		# //print '[X] USER ID -> '+user_id
		# //print '[X] TWEET ID -> '+tweet_id
	except:
		print '[X] ERROR X> PLEASE CHECK YOUR TWEET URL.\n>>>'
		time.sleep(10000)
	ret_headers = {
		'Origin': 'https://twitter.com',
		'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
		'Accept': 'application/json, text/javascript, */*; q=0.01',
		'User-Agent': 'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
		'X-Requested-With': 'XMLHttpRequest',
		'x-twitter-auth-type': 'OAuth2Session',
		'X-Twitter-Active-User': 'yes',
		'Referer': tweet_url,
		'Cookie': '_ga=GA1.2.1741801804.1516677655; kdt=1GBDqOYqnYDGz81JlSDYcjFH4FDuWFg8G2FdQEj7; remember_checked_on=1; eu_cn=1; tfw_exp=0; csrf_same_site_set=1; csrf_same_site=1; ct0=52f94907f7b418398910f8d16abdf3f3; _gid=GA1.2.663121923.1530365541; lang=en; gt=1013053103594246144; _twitter_sess=BAh7CiIKZmxhc2hJQzonQWN0aW9uQ29udHJvbGxlcjo6Rmxhc2g6OkZsYXNo%250ASGFzaHsABjoKQHVzZWR7ADoPY3JlYXRlZF9hdGwrCJvryVBkAToHaWQiJWFj%250AMTZmOTRiNjJlMzA0YzE1ZTU4Yzg1YmFlMDY4ZGY5Ogxjc3JmX2lkIiVlOTcw%250AMjgwMGZkOGQ0ZTZkODFiMjkwM2JmMTY3MGMwNzoJdXNlcmwrCQKQF%252BuJJk8M--5d9550e3924bc595f8af3f4eaadb79d339e7942b; personalization_id="v1_7m2Q33dmYxAzGSYbfYcMeQ=="; guest_id=v1%3A153036696777961505; ads_prefs="HBERAAA="; twid="u=886970025411842050"; auth_token=0bfe39805ef7e689edcba747f4d2c2223d918722'
	}

	ret_data = 'attachment_url='+tweet_url+'&authenticity_token=a1c4f26ebdf4f092fe2efa2425273d70f6f3e183&status='+message
	
	ret_req = requests.post('https://twitter.com/i/tweet/create', data=ret_data, headers=ret_headers)
	# //print ret_req.json()
	if '"in_reply_to_status_id"' in ret_req.content or '"tweet_id"' in ret_req.content or '"tweet_html"' in ret_req.content:
		print '[X] RETWEETED ON TWEET [ '+tweet_id+' ].'
	elif 'You have already sent this Tweet' in ret_req.content:
		print '[X] RETWEETED BEFORE/AGAIN [PASSED].\n'
		pass
	else:
		print '[X] UNEXPECTED ERROR HAPPENED [PASSED].\n'
		pass
# ---------------------------------- ## ---------------------------------- ## ---------------------------------- #
def mute(user):
	# //USER LIKE : sirbugsbunny
	try:
		user_id = requests.get('https://twitter.com/'+user).content.split('fileNav" role="navigation" data-user-id="')[1].split('"')[0]
		# //print '[X] USER ID -> '+user_id
	except:
		print '[X] ERROR X> PLEASE CHECK YOUR USER URL.\n>>>'
		time.sleep(10000)
	mute_headers = {
		'Origin': 'https://twitter.com',
		'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
		'Accept': 'application/json, text/javascript, */*; q=0.01',
		'User-Agent': 'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
		'X-Requested-With': 'XMLHttpRequest',
		'x-twitter-auth-type': 'OAuth2Session',
		'X-Twitter-Active-User': 'yes',
		'Referer': 'https://twitter.com/'+user,
		'Cookie': '_ga=GA1.2.1741801804.1516677655; kdt=1GBDqOYqnYDGz81JlSDYcjFH4FDuWFg8G2FdQEj7; remember_checked_on=1; eu_cn=1; tfw_exp=0; csrf_same_site_set=1; csrf_same_site=1; ct0=52f94907f7b418398910f8d16abdf3f3; _gid=GA1.2.663121923.1530365541; lang=en; gt=1013053103594246144; _twitter_sess=BAh7CiIKZmxhc2hJQzonQWN0aW9uQ29udHJvbGxlcjo6Rmxhc2g6OkZsYXNo%250ASGFzaHsABjoKQHVzZWR7ADoPY3JlYXRlZF9hdGwrCJvryVBkAToHaWQiJWFj%250AMTZmOTRiNjJlMzA0YzE1ZTU4Yzg1YmFlMDY4ZGY5Ogxjc3JmX2lkIiVlOTcw%250AMjgwMGZkOGQ0ZTZkODFiMjkwM2JmMTY3MGMwNzoJdXNlcmwrCQKQF%252BuJJk8M--5d9550e3924bc595f8af3f4eaadb79d339e7942b; personalization_id="v1_7m2Q33dmYxAzGSYbfYcMeQ=="; guest_id=v1%3A153036696777961505; ads_prefs="HBERAAA="; twid="u=886970025411842050"; auth_token=0bfe39805ef7e689edcba747f4d2c2223d918722'
	}
	mute_data = 'authenticity_token=a1c4f26ebdf4f092fe2efa2425273d70f6f3e183&user_id='+user_id
	
	mute_req = requests.post('https://twitter.com/i/user/mute', data=mute_data, headers=mute_headers)
	# //print mute_req.json()
	if 'You will no longer receive notifications from' in mute_req.content or '"notifications":false,"' in mute_req.content or '"following":false,"' in mute_req.content:
		print '[X] MUTED USER [ '+user+' ].\n'
	else:
		print '[X] UNEXPECTED ERROR HAPPENED [PASSED].\n'
		pass
# ---------------------------------- ## ---------------------------------- ## ---------------------------------- #
def block(user):
	# //USER LIKE : sirbugsbunny
	try:
		user_id = requests.get('https://twitter.com/'+user).content.split('fileNav" role="navigation" data-user-id="')[1].split('"')[0]
		# //print '[X] USER ID -> '+user_id
	except:
		print '[X] ERROR X> PLEASE CHECK YOUR USERNAME.\n>>>'
		time.sleep(10000)
	block_headers = {
		'Origin': 'https://twitter.com',
		'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
		'Accept': 'application/json, text/javascript, */*; q=0.01',
		'User-Agent': 'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
		'X-Requested-With': 'XMLHttpRequest',
		'x-twitter-auth-type': 'OAuth2Session',
		'X-Twitter-Active-User': 'yes',
		'Referer': 'https://twitter.com/'+user,
		'Cookie': '_ga=GA1.2.1741801804.1516677655; kdt=1GBDqOYqnYDGz81JlSDYcjFH4FDuWFg8G2FdQEj7; remember_checked_on=1; eu_cn=1; tfw_exp=0; csrf_same_site_set=1; csrf_same_site=1; ct0=52f94907f7b418398910f8d16abdf3f3; _gid=GA1.2.663121923.1530365541; lang=en; gt=1013053103594246144; _twitter_sess=BAh7CiIKZmxhc2hJQzonQWN0aW9uQ29udHJvbGxlcjo6Rmxhc2g6OkZsYXNo%250ASGFzaHsABjoKQHVzZWR7ADoPY3JlYXRlZF9hdGwrCJvryVBkAToHaWQiJWFj%250AMTZmOTRiNjJlMzA0YzE1ZTU4Yzg1YmFlMDY4ZGY5Ogxjc3JmX2lkIiVlOTcw%250AMjgwMGZkOGQ0ZTZkODFiMjkwM2JmMTY3MGMwNzoJdXNlcmwrCQKQF%252BuJJk8M--5d9550e3924bc595f8af3f4eaadb79d339e7942b; personalization_id="v1_7m2Q33dmYxAzGSYbfYcMeQ=="; guest_id=v1%3A153036696777961505; ads_prefs="HBERAAA="; twid="u=886970025411842050"; auth_token=0bfe39805ef7e689edcba747f4d2c2223d918722'
	}
	block_data = 'authenticity_token=a1c4f26ebdf4f092fe2efa2425273d70f6f3e183&challenges_passed=false&handles_challenges=1&user_id='+user_id
	
	block_req = requests.post('https://twitter.com/i/user/block', data=block_data, headers=block_headers)
	# //print block_req.json()
	if 'BlockUnblock' in block_req.content or '"new_state":"blocked"' in block_req.content or 'has been blocked.' in block_req.content:
		print '[X] BLOCKED USER [ '+user+' ].\n'
	else:
		print '[X] UNEXPECTED ERROR HAPPENED [PASSED].\n'
		pass
# ---------------------------------- ## ---------------------------------- ## ---------------------------------- #

def start():
	if int(type) == 1:
		# FOLLOW
		try:
			accs_file = open(raw_input('[X] ENTER YOUR ACCOUNTS PATH FILE NAME [USER:PASS] X> ')+'.txt', 'r')
			username = raw_input('[X] ENTER YOUR USERNAME TO SEND FOLLOWERS X> ')
		except:
			print '[X] ERROR X> PLEASE CHECK YOUR PATH FILE NAME.'
		for line in accs_file:
			email, passwd = line.strip().split(':')
			print ''
			login(email, passwd)
			if status == 'SUCCESS':
				follow(username)
			else:
				pass
	elif int(type) == 2:
		# BLOCK
		try:
			accs_file = open(raw_input('[X] ENTER YOUR ACCOUNTS PATH FILE NAME [USER:PASS] X> ')+'.txt', 'r')
			username = raw_input('[X] ENTER YOUR USERNAME TO BLOCK X> ')
		except:
			print '[X] ERROR X> PLEASE CHECK YOUR PATH FILE NAME.'
		for line in accs_file:
			email, passwd = line.strip().split(':')
			print ''
			login(email, passwd)
			if status == 'SUCCESS':
				block(username)
			else:
				pass
	elif int(type) == 3:
		# MUTE
		try:
			accs_file = open(raw_input('[X] ENTER YOUR ACCOUNTS PATH FILE NAME [USER:PASS] X> ')+'.txt', 'r')
			username = raw_input('[X] ENTER YOUR USERNAME TO MUTE X> ')
		except:
			print '[X] ERROR X> PLEASE CHECK YOUR PATH FILE NAME.'
		for line in accs_file:
			email, passwd = line.strip().split(':')
			print ''
			login(email, passwd)
			if status == 'SUCCESS':
				mute(username)
			else:
				pass
	elif int(type) == 4:
		# LIKE
		try:
			accs_file = open(raw_input('[X] ENTER YOUR ACCOUNTS PATH FILE NAME [USER:PASS] X> ')+'.txt', 'r')
			tweet_url = raw_input('[X] ENTER YOUR TWEET URL TO LIKE [/ IN THE END] X> ')
		except:
			print '[X] ERROR X> PLEASE CHECK YOUR PATH FILE NAME.'
		for line in accs_file:
			email, passwd = line.strip().split(':')
			print ''
			login(email, passwd)
			if status == 'SUCCESS':
				like(tweet_url)
			else:
				pass
	elif int(type) == 5:
		# COMMENT
		try:
			accs_file = open(raw_input('[X] ENTER YOUR ACCOUNTS PATH FILE NAME [USER:PASS] X> ')+'.txt', 'r')
			tweet_url = raw_input('[X] ENTER YOUR TWEET URL TO COMMENT [/ IN THE END] X> ')
		except:
			print '[X] ERROR X> PLEASE CHECK YOUR PATH FILE NAME.'
		for line in accs_file:
			email, passwd = line.strip().split(':')
			com = raw_input('[X] ENTER YOUR COMMENT MESSAGE X> ')
			print ''
			login(email, passwd)
			if status == 'SUCCESS':
				comment(tweet_url, com)
			else:
				pass
	elif int(type) == 6:
		# RETWEET
		try:
			accs_file = open(raw_input('[X] ENTER YOUR ACCOUNTS PATH FILE NAME [USER:PASS] X> ')+'.txt', 'r')
			tweet_url = raw_input('[X] ENTER YOUR TWEET URL TO RETWEET [/ IN THE END] X> ')
		except:
			print '[X] ERROR X> PLEASE CHECK YOUR PATH FILE NAME.'
		for line in accs_file:
			email, passwd = line.strip().split(':')
			com = raw_input('[X] ENTER YOUR RETWEET MESSAGE X> ')
			print ''
			login(email, passwd)
			if status == 'SUCCESS':
				retweet(tweet_url, com)
			else:
				pass
		else:
			print '[X] ERROR X> PLEASE CHOOSE A CORRECT NUMBER.'

# ---------------------------------- ## ---------------------------------- ## ---------------------------------- #

# ---------------------------------- ## ---------------------------------- #
print bugs
# ---------------------------------- ## ---------------------------------- #
print '[+1] TWITTER ACCOUNT FOLLLOW [UESR ID].'
print '[+2] TWITTER ACCOUNT BLOCK [USER ID].'
print '[+3] TWITTER ACCOUNT MUTE [USER ID].'
print '[+4] TWITTER TWEETS LIKE [TWEET URL].'
print '[+5] TWITTER TWEETS COMMENT [TWEET URL, COMMENT].'
print '[+6] TWITTER TWEETS RETWEETS [TWEET URL, MESSAGE].'
# ---------------------------------- ## ---------------------------------- #
print '\n'
# ---------------------------------- ## ---------------------------------- #

# ---------------------------------- ## ---------------------------------- ## ---------------------------------- #
type = raw_input('[X] CHOOSE YOUR TOOLKIT TOOL NUM X> ')
if __name__ == '__main__':
	start()