import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.realpath(sys.argv[0])), '..'))
from sdcclient import SdcClient

if len(sys.argv) != 2:
    print 'usage: %s <sysdig-token> ' % sys.argv[0]
    print 'You can find your token at https://app.sysdigcloud.com/#/settings/user'
    sys.exit(1)

sdc_token = sys.argv[1]

#
# Instantiate the SDC client
#
sdclient = SdcClient(sdc_token)

res=sdclient.create_alert_from_jsonfile(alertformat.json)

if not res[0]:
    sys.exit(1)
