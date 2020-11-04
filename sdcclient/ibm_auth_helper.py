import requests


class IbmAuthHelper:
    '''Authenticate with IBM Cloud IAM.

    **Arguments**
        **url**: Sysdig endpoint URL that should point to IBM Cloud
        **apikey**: IBM Cloud IAM apikey that will be used to retrieve an access token
        **guid**: GUID of an IBM Cloud Monitoring with Sysdig instance

    **Returns**
        A dictionary that will authenticate you with the IBM Cloud IAM API.
    '''

    @staticmethod
    def get_headers(url, apikey, guid):
        iam_token = IbmAuthHelper.__get_iam_token(url, apikey)
        return {
            'Authorization': 'Bearer ' + iam_token,
            'IBMInstanceID': guid
        }

    @staticmethod
    def __get_iam_endpoint(url):
        IAM_ENDPOINT = {
            'stage': 'iam.test.cloud.ibm.com',
            'prod': 'iam.cloud.ibm.com'
        }
        if '.test.' in url:
            return IAM_ENDPOINT['stage']
        else:
            return IAM_ENDPOINT['prod']

    @staticmethod
    def __get_iam_token(url, apikey):
        env_url = IbmAuthHelper.__get_iam_endpoint(url)
        response = requests.post(
            'https://' + env_url + '/identity/token',
            data={
                'grant_type': 'urn:ibm:params:oauth:grant-type:apikey',
                'response_type': 'cloud_iam',
                'apikey': apikey
            },
            headers={
                'Accept': 'application/json'
            })
        if response.status_code == 200:
            return response.json()['access_token']
        else:
            response.raise_for_status()
