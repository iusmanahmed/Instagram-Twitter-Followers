import pandas as pd  


data_file=pd.read_csv('/home/usman/Desktop/1.csv')
X =data_file.iloc[:, 3]
line=""
for t in range (2130,len(X)):
  import re
  import requests
  from bs4 import BeautifulSoup
  research_later=str(X[t])
  research_later+= " twitter handle"
  print research_later
  goog_search = "https://www.google.com.pk/search?sclient=psy-ab&client=ubuntu&hs=k5b&channel=fs&biw=1366&bih=648&noj=1&q=" + research_later
  r = requests.get(goog_search)
  soup = BeautifulSoup(r.text, "html.parser")
  #print "Twitter Url:   ",soup.find('cite').text
  s=str(soup.find('cite').text)
  f=".com/"
  f1="?"
  startpos= s.find(f)+5
  endpos=s.find(f1)
  data1=s[startpos:endpos]
  import tweepy
  consumer_key = "3Pu7WwbafHcSaKOWkmAfeRdgQ"
  consumer_secret = "r2MdGLYWz1FoOsuMV4AXnnjtB8baFzyKxCyKrMW0bxwFhLcBwA"
  access_key="1147262209-oQCt8qwtRbmd2TctYDvKZy8e5gNOsB6YYQEeiI9"
  access_secret="SAGXSmoX8ExcNWbalZvao6naVvGs9UuNqTtTRawH9l281"
  auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
  auth.set_access_token(access_key, access_secret)
  #print "Step 1:    --Done--"
  api = tweepy.API(auth)
  #print "Step 2:    --Done--"
  try:
    user =api.get_user(data1)
    name=user.screen_name
    followerscount=user.followers_count
  except:
    name=0
    followerscount=0



  #print "Step 3:    --Done--"
  #print "Twitter handle:    ",user.screen_name
  #print "Twitter Follower:    ", user.followers_count

#instagram followers Data
  research_later=str(X[t])
  research_later+= " instagram handle"
  print research_later
  goog_search = "https://www.google.com.pk/search?sclient=psy-ab&client=ubuntu&hs=k5b&channel=fs&biw=1366&bih=648&noj=1&q=" + research_later


  r = requests.get(goog_search)
  #print "Step 4:    --Done--"
  soup = BeautifulSoup(r.text, "html.parser")
  #print "Instagram url:   ",soup.find('cite').text

  s=str(soup.find('cite').text)

  f=".com/"

  startpos= s.find(f)+5
  endpos=len(s)

  data1=s[startpos:endpos]


  import requests
  import json
  import time
  import random

  url = 'https://www.instagram.com/'
  url_user = '%s%s%s' % (url, data1, '/')
  url_login = 'https://www.instagram.com/accounts/login/ajax/'
  s = requests.Session()
  s.cookies.update ({'sessionid' : '', 'mid' : '', 'ig_pr' : '1',
                     'ig_vw' : '1920', 'csrftoken' : '',
                     's_network' : '', 'ds_user_id' : ''})
  login_post = {'username' : 'usmanahmed118',
                 'password' : 'usmanahmed1'}
  s.headers.update ()
  r = s.get(url)
  s.headers.update({'X-CSRFToken' : r.cookies['csrftoken']})
  time.sleep(5 * random.random())
  login = s.post(url_login, data=login_post,
                  allow_redirects=True)
  s.headers.update({'X-CSRFToken' : login.cookies['csrftoken']})
  if login.status_code == 200:
    r = s.get('https://www.instagram.com/')
    finder = r.text.find('your_login')

  r = s.get(url_user)
  text = r.text

  finder_text_start = ('<script type="text/javascript">'
                     'window._sharedData = ')
  finder_text_start_len = len(finder_text_start)-1
  finder_text_end = ';</script>'

  all_data_start = text.find(finder_text_start)
  all_data_end = text.find(finder_text_end, all_data_start + 1)
  json_str = text[(all_data_start + finder_text_start_len + 1) \
               : all_data_end]
  user_info = json.loads(json_str)
  try:
    follower_count = user_info['entry_data']['ProfilePage'][0]['user']["followed_by"]['count']
  except KeyError:
    follower_count=0

  #print "Instagram followers:   ", follower_count
  fout=open('/home/usman/Desktop/actor3.txt', 'a')
  line+=str(X[t])
  line+=","
  line+=str(name)
  line+=","
  line+=str(followerscount)
  line+=","
  line+=str(follower_count)
  line+=","
  print line
  fout.write("\n")
  fout.write(line)
  line=""
  data=""
  print t

