# -*- coding: utf-8 -*-

import json
import urllib
import urllib2
import csv

zbxsrv = "http://52.68.167.40/zabbix/api_jsonrpc.php"
headers = {"Content-Type": "application/json-rpc"}
zbx_user = "bci_admin"
zbx_pass = "Brains1234"
postdata = ""

class ZabbixApi(object):
    def __init__(self):
        self.request_id = 1
        self.auth_token = self.request('user.login', {'user':zbx_user, 'password':zbx_pass})['result']

    def request(self, method, params, auth_token=None):
        if hasattr(self, 'auth_token'):
            auth_token = self.auth_token

        postdata = {'jsonrpc': '2.0'}
        postdata['method'] = method
        postdata['params'] = params
        postdata['auth'] = auth_token
        postdata['id'] = self.request_id
        #data = json.dumps(postdata)

        request = urllib2.Request(zbxsrv, json.dumps(postdata), headers)
        self.request_id += 1
        return json.loads(urllib2.urlopen(request).read())

if __name__ == '__main__':
    #オブジェクト取得
    api = ZabbixApi()

    #ホスト情報の取得
    contents_dict = api.request('host.get',
        {'output': 'extend'})

    #イベンド情報の取得
    contents_dict = api.request('event.get',
        {"outout": "extend",
        "select_acknowledges": "extend",
#        "itemids": "23645",
        "sortfield": ["clock", "eventid"],
        "sortorder": "DESC",
        "limit":1})

    keys = []
    values = []

    #csitems()
    for item in contents_dict['result']:
        #keys.append(item.keys())
        #values.append(item.values())
        for key in item.keys():
            #print key
            keys.append(key)
        for value in item.values():
            #print value
            values.append(value)


    print keys
    print values


#下の行のコメントを外してみると、どんな配列ができたのかが分かります。
#print rowList                 
#dataWriter.writerows(rowList)
#f.close()