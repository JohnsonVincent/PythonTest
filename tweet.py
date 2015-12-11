#!/usr/bin/env python
# -*- coding: utf-8 -*-

from requests_oauthlib import OAuth1Session
import twitter
import json

### Constants
oath_key_dict = {
  "consumer_key": "8suXsmqXbbLJapkK8SR3LVmT2",
  "consumer_secret": "Yj0nJ8hThq4JMWSwy9ymGIUDUQrbQdZKbmMoavvuoNGNDYcimu",
  "access_token": "1898875884-5tHxgGr0Iv6RZ4JC3qAASwuWPly0LrTC46p93",
  "access_token_secret": "vTivsDlLmZkng4FlBiSUDfGg9UowRPA0t5MRMf8wSnBWi"
}

def main():
  #url = "https://api.twitter.com/1.1/statuses/update.json?"
  #params = {"status": "hello,World!"}
  twitter = create_oath_session(oath_key_dict)

  url = 'https://api.twitter.com/1.1/statuses/home_timeline.json'
  #　url = 'https://api.twitter.com/1.1/search/tweets.json?q=検索ワード'
  params = {'count': 10, 'include_rts': False}  # 取得するツイート数(10～200)，リツイートの有無
  resp = twitter.get(url, params=params)
  print resp.text
  data = json.loads(resp.text)
  print data

  #tweet_fields = ['created_at', 'text', 'id']
  #tweets = DataFrame(data, columns=tweet_fields)
  #　tweets = DataFrame(data['statuses'], columns=tweet_fields)

  #user_fields = ['name', 'screen_name']
  #tweets[user_fields] = DataFrame([d['user'] for d in data], columns=user_fields)
  #　tweets[user_fields] = DataFrame([d['user'] for d in data['statuses']], columns=user_fields)

def create_oath_session(oath_key_dict):
  oath = OAuth1Session(
  oath_key_dict["consumer_key"],
  oath_key_dict["consumer_secret"],
  oath_key_dict["access_token"],
  oath_key_dict["access_token_secret"]
  )
  return oath

### Execute
if __name__ == "__main__":
    main()