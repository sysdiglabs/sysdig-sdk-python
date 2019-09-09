from time import sleep
import requests

class SdIbmCloud():
    '''Authenticate with IBM Cloud IAM.

    **Arguments**
        **apikey**: IBM Cloud IAM apikey that will be used to retrieve an access token
        **guid**: GUID of an IBM Cloud Monitoring with Sysdig instance

    **Returns**
        An object that will authenticate you with the IBM Cloud IAM API.
    '''

    IAM_ENDPOINT = {
        'stage': 'iam.test.cloud.ibm.com',
        'prod': 'iam.cloud.ibm.com'
    }

    def __init__(self, apikey, guid):
        self.apikey = apikey
        self.guid = guid

    def get_iam_token(self, url):
        if '.test.' in url:
            env_url = self.IAM_ENDPOINT['stage']
        else:
            env_url = self.IAM_ENDPOINT['prod']
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
        else:
            response.raise_for_status()
