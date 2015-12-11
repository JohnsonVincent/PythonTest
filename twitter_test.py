#!/usr/bin/env python
# -*- coding:utf-8 -*-

import twitter

CONSUMER_KEY="8suXsmqXbbLJapkK8SR3LVmT2"
CONSUMER_SECRET="Yj0nJ8hThq4JMWSwy9ymGIUDUQrbQdZKbmMoavvuoNGNDYcimu"
ACCESS_TOKEN="1898875884-5tHxgGr0Iv6RZ4JC3qAASwuWPly0LrTC46p93"
ACCESS_TOKEN_SECRET="vTivsDlLmZkng4FlBiSUDfGg9UowRPA0t5MRMf8wSnBWi"

api = twitter.Api(consumer_key=CONSUMER_KEY,
                      consumer_secret=CONSUMER_SECRET,
                      access_token_key=ACCESS_TOKEN,
                      access_token_secret=ACCESS_TOKEN_SECRET,
                      cache=None)

postmsg = 'ぴかしなう'
status = api.PostUpdate(postmsg.decode("utf-8"))