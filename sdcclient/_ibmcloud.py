from time import sleep
import requests

class SdIbmCloud():
    def __init__(self, apikey, url, resource):
        self.apikey = apikey
        self.url = url
        self.resource = resource

    def __get_iam_token(self, last_retry):
        if '.test.' in self.url:
            env_url = 'iam.test.cloud.ibm.com'
        else:
            env_url = 'iam.cloud.ibm.com'
        response = requests.post(
            'https://' + env_url + '/identity/token',
            data={
                'grant_type': 'urn:ibm:params:oauth:grant-type:apikey',
                'response_type': 'cloud_iam',
                'apikey': self.apikey
            },
            headers={
                'Accept': 'application/json'
            })
        if response.status_code == 200:
            return response.json()['access_token']
        elif last_retry:
            response.raise_for_status()
        else:
            print('IBM Cloud token auth error: ' + str(response.status_code))
        return None

    def get_iam_token(self):
        retries = 0
        max_retries = 3
        while retries < max_retries:
            retries += 1
            auth_token = self.__get_iam_token(retries == max_retries)
            if auth_token:
                return auth_token
            sleep(1)

    def __get_get_guid(self, last_retry, auth_token):
        response = requests.get(
            'https://resource-controller.cloud.ibm.com/v2/resource_instances',
            headers={
                'Accept': 'application/json',
                'Authorization': 'Bearer ' + auth_token
            })
        if response.status_code == 200:
            resp_json = response.json()
            for resource in resp_json['resources']:
                if resource['name'] == self.resource:
                    return resource['guid']
            raise RuntimeError('IBM Cloud resource name not found in response')
        elif last_retry:
            response.raise_for_status()
        else:
            print('IBM Cloud resource retrieval error: ' + str(response.status_code))
        return None

    def get_get_guid(self, auth_token):
        retries = 0
        max_retries = 3
        while retries < max_retries:
            retries += 1
            guid = self.__get_get_guid(retries == max_retries, auth_token)
            if guid:
                return guid
            sleep(1)
