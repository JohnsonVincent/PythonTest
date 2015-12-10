#!/usr/bin/python
# -*- coding: utf-8 -*-
import json
import urllib2

zbxsrv = "http://52.68.167.40/zabbix/api_jsonrpc.php"
headers = {"Content-Type": "application/json-rpc"}
zbx_user = "bci_admin"
zbx_pass = "Brains1234"

post_data = json.dumps(
    {
    'jsonrpc': '2.0',
    'method': 'user.login', 
    'params':{'user':zbx_user, 'password':zbx_pass}, 
    'auth':None, 
    'id': 1
    })

request = urllib2.Request(zbxsrv, post_data, headers)
contents = urllib2.urlopen(request)
contents_str = contents.read()
contents_dict = json.loads(contents_str)
zbx_auth = contents_dict['result']

print zbx_auth

post_data = json.dumps({'jsonrpc': '2.0','method': 'host.get', 'params': {"outout":"extend"}, 'auth':zbx_auth, 'id': 1})

print post_data

request = urllib2.Request(zbxsrv, post_data, headers)
contents = urllib2.urlopen(request)
contents_str = contents.read()
contents_dict = json.loads(contents_str)

for host in contents_dict['result']:
    print host['name'], host['hostid']



post_data = json.dumps({'jsonrpc': '2.0','method': 'event.get', 'params':
    {"outout": "extend",
     "select_acknowledges": "extend",
     "itemids": "23645",
     "sortfield": ["clock", "eventid"],
     "sortorder": "DESC",
     "limit":1
     }, 'auth' :zbx_auth, 'id': 1})
request = urllib2.Request(zbxsrv, post_data, headers)
contents = urllib2.urlopen(request)
contents_str = contents.read()
contents_dict = json.loads(contents_str)
print contents_dict