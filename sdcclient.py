import sys
import time
import requests
import json
import re

###############################################################################
# The sysdig cloud client
###############################################################################
class SdcClient:
    userinfo = None
    n_connected_agents = None

    def __init__(self, token, sdc_url = 'https://app.sysdigcloud.com'):
        self.token = token
        self.hdrs = {'Authorization': 'Bearer ' + self.token, 'Content-Type': 'application/json'}
        self.url = sdc_url
   
    def __checkResponse(self, r):
        if r.status_code >= 300:
            self.errorcode = r.status_code

            j = r.json()
            if 'errors' in j:
                self.lasterr = j['errors'][0]['message']
            else:
                self.lasterr = 'status code ' + str(self.errorcode)
            return False
        return True

    def getUserInfo(self):
        if self.userinfo == None:
            r = requests.get(self.url + '/api/user/me', headers=self.hdrs)
            if not self.__checkResponse(r):
                return [False, self.lasterr]
            self.userinfo = r.json()
        return [True, self.userinfo]

    def getNConnectedAgents(self):
        r = requests.get(self.url + '/api/agents/connected', headers=self.hdrs)
        if not self.__checkResponse(r):
            return [False, self.lasterr]
        data = r.json()
        return [True, data['total']]

    def getNotificationSettings(self):
        r = requests.get(self.url + '/api/settings/notifications', headers=self.hdrs)
        if not self.__checkResponse(r):
            return [False, self.lasterr]
        return [True, r.json()]

    def createAlert(self, name, description, condition, for_each, for_atelast_us, severity):
        #
        # Get the list of alerts from the server
        #
        r = requests.get(self.url + '/api/alerts', headers=self.hdrs)
        if not self.__checkResponse(r):
            return [False, self.lasterr]
        j = r.json()

        print 'Creating alert %s' % (description)

        #
        # If this alert already exists, don't create it again
        #
        for db in j['alerts']:
            if 'description' in db:
                if db['description'] == description:
                    return [False, 'alert ' + name + ' already exists']

        #
        # Populate the alert information
        #
        alert_json = {
            'alert' : {
                'type' : 'MANUAL',
                'name' : name,
                'description' : description,
                'enabled' : True,
                #'filter' : 'kubernetes.namespace.name = "loris" and kubernetes.service.name = "mysql"',
                'severity' : severity,
                'notify' : [ 'EMAIL' ],
                'timespan' : for_atelast_us,
                'condition' : condition
            }
        }

        if for_each != None and for_each != []: 
            alert_json['alert']['segmentBy'] = [ for_each ]
            alert_json['alert']['segmentCondition'] = { 'type' : 'ANY' }

        #
        # Create the new alert
        #
        r = requests.post(self.url + '/api/alerts', headers=self.hdrs, data = json.dumps(alert_json))
        if not self.__checkResponse(r):
            return [False, self.lasterr]
        return [True, r.json()]

    def addEmailNotificationRecipient(self, email):
        #
        # Retirieve the user's notification settings
        #
        r = requests.get(self.url + '/api/settings/notifications', headers=self.hdrs)
        if not self.__checkResponse(r):
            return [False, self.lasterr]
        j = r.json()

        #
        # Enable email notifications
        #
        j['userNotification']['email']['enabled'] = True

        #
        # Add the given recipient
        #
        if not email in j['userNotification']['email']['recipients']:
            j['userNotification']['email']['recipients'].append(email)
            print 'adding notification target ' + email
        else:
            return [False, 'notification target ' + email + ' already present']

        r = requests.put(self.url + '/api/settings/notifications', headers=self.hdrs, data = json.dumps(j))
        if not self.__checkResponse(r):
            return [False, self.lasterr]
        return [True, r.json()]
