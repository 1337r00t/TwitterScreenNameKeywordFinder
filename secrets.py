import requests
USERNAME = 'REPLACE_ME'
PASSWORD = 'REPLACE_ME'
login = lambda u,p: requests.post("https://api.twitter.com/auth/1/xauth_password.json",data={'x_auth_identifier':u,'x_auth_password':p},headers={'Authorization':'Bearer AAAAAAAAAAAAAAAAAAAAAFXzAwAAAAAAMHCxpeSDG1gLNLghVe8d74hl6k4%3DRUMF4xAQLsbeBhTSRrCiQpJtxoGWeyHrDb5te2jpGskWDFW82F','X-Guest-Token':requests.post("https://api.twitter.com/1.1/guest/activate.json",headers={"Authorization":"Bearer AAAAAAAAAAAAAAAAAAAAAFXzAwAAAAAAMHCxpeSDG1gLNLghVe8d74hl6k4%3DRUMF4xAQLsbeBhTSRrCiQpJtxoGWeyHrDb5te2jpGskWDFW82F"}).json()['guest_token']}).json()
auth = login(USERNAME,PASSWORD)
###########################################################
# https://gist.github.com/shobotch/5160017
consumer_key = '3nVuSoBZnx6U4vzUxf5w'
consumer_secret = 'Bcs59EFbbsdF6Sl9Ng71smgStWEGwXXKSjYvPVt7qys'
access_token = auth['oauth_token']
access_secret = auth['oauth_token_secret']
