#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import urllib
import urllib2
import csv

zbxsrv = "http://52.68.167.40/zabbix/api_jsonrpc.php"
headers = {"Content-Type": "application/json-rpc"}
zbx_user = "bci_admin"
zbx_pass = "Brains1234"
#ログイン情報のJSON POST情報
postdata = ""

#ホスト情報取得 API リクエスト
postdata_host_get = {
    'output': 'extend'
    #"limit": 1
    }

#イベント情報取得 API リクエスト
postdata_event_get = {
    'outout': 'extend',
    #'select_acknowledges': "extend",
    "select_hosts"
    "itemids": "23645",
    "sortfield": ["clock", "eventid"],
    "sortorder": "DESC"
    #"limit": 1
}

#アイテム情報取得 API リクエスト
postdata_item_get = {
    "output": "extend",
#    "hostids": "10084",
    "search": {
        "key_": "system"
    },
    "sortfield": "name"
    #"limit": 1
}

#トリガー情報取得 API リクエスト
postdata_trigger_get = {
#    "triggerids": "14062",
    "output": "extend",
    "selectFunctions": "extend"
    #"limit": 1
}

postdata_history_get = {
    "output": "extend",
    "history": 0,
    #"itemids": "23296",
    "sortfield": "clock",
    "sortorder": "DESC"
    #"limit": 10
}

postdata_alert_get = {
    'output': 'extend',
    'limit': 3
    }



FIELD_NAMES = [
'eventid',
'objectid',
'clock',
'object',
'acknowledged',
'value',
'source',
'ns'
]

FIELD_NAMES2 = [
'itemid',
'username',
'snmpv3_contextname',
'inventory_link',
'multiplier',
'authtype',
'trends',
'snmpv3_authpassphrase',
'snmp_oid',
'templateid',
'snmpv3_securitylevel',
'port',
'lastns',
'password',
'logtimefmt',
'mtime',
'delay',
'publickey',
'state',
'params',
'snmpv3_securityname',
'formula',
'type',
'snmpv3_authprotocol',
'prevvalue',
'status',
'lastlogsize',
'lastclock',
'snmp_community',
'description',
'data_type',
'evaltype',
'trapper_hosts',
'lastvalue',
'units',
'value_type',
'delta',
'snmpv3_privprotocol',
'delay_flex',
'interfaceid',
'snmpv3_privpassphrase',
'hostid',
'key_',
'name',
'privatekey',
'lifetime',
'valuemapid',
'flags',
'error',
'ipmi_sensor',
'history'
]

FIELD_NAMES3 = [
'status',
'functions',
'description',
'state',
'url',
'type',
'templateid',
'lastchange',
'value',
'priority',
'triggerid',
'flags',
'comments',
'error',
'expression'
]

FIELD_NAMES4 = [
'available',
'maintenance_type',
'ipmi_errors_from',
'ipmi_username',
'snmp_disable_until',
'ipmi_authtype',
'ipmi_disable_until',
'lastaccess',
'snmp_error',
'ipmi_privilege',
'jmx_error',
'jmx_available',
'maintenanceid',
'snmp_available',
'status',
'description',
'host',
'disable_until',
'ipmi_password',
'templateid',
'ipmi_available',
'maintenance_status',
'snmp_errors_from',
'ipmi_error',
'proxy_hostid',
'hostid',
'name',
'jmx_errors_from',
'jmx_disable_until',
'flags',
'error',
'maintenance_from',
'errors_from'
]


#FIELD_NAMES5 = [
#'itemid',
#'ns',
#'value',
#'clock'
#]

FIELD_NAMES6 = [
'eventid',
'mediatypeid',
'alerttype',
'alertid',
'clock',
'error',
'userid',
'retries',
'status',
'actionid',
'sendto',
'message',
'esc_step',
'subject'
]


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

        request = urllib2.Request(zbxsrv, json.dumps(postdata), headers)
        self.request_id += 1
        return json.loads(urllib2.urlopen(request).read())


def CsvCreate(zabbix_dict, csvFileName, fieldnames):

    if fieldnames:
        #CSV吐き出し
        f = open(csvFileName+'.csv', 'w')
        dataWriter = csv.DictWriter(f, fieldnames = fieldnames)
        dataWriter.writeheader()

        for item in zabbix_dict['result']:
           dataWriter.writerow(item)
        f.close()

    else:
    #フィールド名抜き出したい時に使いたい
        for item in zabbix_dict['result']:
            for key in item.keys():
                print key


#メイン処理
if __name__ == '__main__':
    #オブジェクト取得
    api = ZabbixApi()

    #ホスト情報の取得
    host_dict = api.request('host.get', postdata_host_get)
    CsvCreate(host_dict, 'host_get', FIELD_NAMES4)

    #イベンド情報の取得
    event_dict = api.request('event.get', postdata_event_get)
    #CSV書き込み
    CsvCreate(event_dict, 'event_get', FIELD_NAMES)

    #アイテム情報の取得
    item_dict = api.request('item.get', postdata_item_get)
    #CSV書き込み
    CsvCreate(item_dict, 'item_get', FIELD_NAMES2)

    #トリガー情報の取得
    trigger_dict = api.request('trigger.get', postdata_trigger_get)
    #CSV書き込み
    CsvCreate(trigger_dict, 'trigger_get', FIELD_NAMES3)

    history_dict = api.request('history.get', postdata_history_get)
    CsvCreate(history_dict, 'history_get', "")

    alert_dict = api.request('alert.get', postdata_alert_get)
    CsvCreate(alert_dict, 'alert_get', FIELD_NAMES6)

    print 'end'