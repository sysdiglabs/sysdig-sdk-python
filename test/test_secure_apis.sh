#!/bin/bash

set -euxo pipefail

SCRIPT=$(readlink -f $0)
SCRIPTDIR=$(dirname $SCRIPT)

export SDC_URL=https://secure-staging.sysdig.com

# we expect this to fail with 405. It only works for on-premise accounts.
set +e
OUT=`$SCRIPTDIR/../examples/set_secure_system_falco_rules.py $PYTHON_SDC_TEST_API_TOKEN $SCRIPTDIR/sample-falco-rules.yaml`
if [[ $? != 1 ]]; then
   echo "set_secure_system_falco_rules.py succeeded when it should have failed"
   exit 1
fi
set -e

# Get the system falco rules file. Don't validate it, just verify that it can be fetched.
$SCRIPTDIR/../examples/get_secure_system_falco_rules.py $PYTHON_SDC_TEST_API_TOKEN | tee /tmp/falco_rules.yaml

NOW=$(date)
cat <<EOF > /tmp/test_apis_user_rules.yaml
- rule: My Rule as of $NOW
  desc: My Description
  condition: evt.type=open and fd.name="/tmp/some-file.txt"
  output: Impossible file opened
  priority: INFO
EOF

$SCRIPTDIR/../examples/set_secure_user_falco_rules.py $PYTHON_SDC_TEST_API_TOKEN /tmp/test_apis_user_rules.yaml
$SCRIPTDIR/../examples/get_secure_user_falco_rules.py $PYTHON_SDC_TEST_API_TOKEN > /tmp/falco_rules.yaml
# Removed comparison. The new endpoint automatically adds a header to the YAML file,
# and this use case is already covered in the custom_rules_spec.py test file.
# diff /tmp/falco_rules.yaml /tmp/test_apis_user_rules.yaml


# Delete all policies and then get them. There should be none.
$SCRIPTDIR/../examples/delete_all_policies.py $PYTHON_SDC_TEST_API_TOKEN
OUT=`$SCRIPTDIR/../examples/list_policies.py $PYTHON_SDC_TEST_API_TOKEN`
if [[ $OUT != *"[]"* ]]; then
    echo "Unexpected output after deleting all policies"
    exit 1
fi

# Create the default set of policies and then fetch them. There should
# be 1, corresponding to the system falco rule.
$SCRIPTDIR/../examples/create_default_policies.py $PYTHON_SDC_TEST_API_TOKEN
OUT=`$SCRIPTDIR/../examples/list_policies.py $PYTHON_SDC_TEST_API_TOKEN`
if [[ $OUT != *"\"Suspicious Filesystem Changes\""* ]]; then
    echo "Unexpected output after creating default policies"
    exit 1
fi

# Get that policy, change the name, and create a new duplicate policy.
OUT=`$SCRIPTDIR/../examples/get_policy.py $PYTHON_SDC_TEST_API_TOKEN "Suspicious Filesystem Changes"`
MY_POLICY=$OUT
if [[ $OUT != *"\"Suspicious Filesystem Changes\""* ]]; then
    echo "Could not fetch policy with name \"Suspicious Filesystem Changes\""
    exit 1
fi

NEW_POLICY=`echo $MY_POLICY | sed -e "s/Suspicious Filesystem Changes/Suspicious Filesystem Changes 2/g" | sed -e 's/"id": [0-9]*,//' | sed -e 's/"version": [0-9]*/"version": null/'`
OUT=`echo $NEW_POLICY | $SCRIPTDIR/../examples/add_policy.py $PYTHON_SDC_TEST_API_TOKEN`
if [[ $OUT != *"\"Suspicious Filesystem Changes 2\""* ]]; then
    echo "Could not create new policy"
    exit 1
fi

# Change the description of the new policy and update it.
ID=`echo $OUT | grep -E -o '"id": [^,]+,' | awk '{print $2}' | awk -F, '{print $1}'`
MODIFIED_POLICY=`echo $MY_POLICY | sed -e "s/Suspicious Filesystem Changes/Suspicious Filesystem Changes 2/g" | sed -e "s,Identified suspicious filesystem activity that might change sensitive/important files,My New Description,g" | sed -e "s/\"id\": [0-9]*,/\"id\": $ID,/"`
OUT=`echo $MODIFIED_POLICY | $SCRIPTDIR/../examples/update_policy.py $PYTHON_SDC_TEST_API_TOKEN`
if [[ $OUT != *"\"description\": \"My New Description\""* ]]; then
    echo "Could not update policy \"Suspicious Filesystem Changes 2\""
    exit 1
fi

# Delete the new policy.
OUT=`$SCRIPTDIR/../examples/delete_policy.py --name "Suspicious Filesystem Changes 2" $PYTHON_SDC_TEST_API_TOKEN`
if [[ $OUT != *"\"Suspicious Filesystem Changes 2\""* ]]; then
    echo "Could not delete policy \"Suspicious Filesystem Changes 2\""
    exit 1
fi

OUT=`$SCRIPTDIR/../examples/list_policies.py $PYTHON_SDC_TEST_API_TOKEN`
if [[ $OUT = *"\"Suspicious Filesystem Changes 2\""* ]]; then
    echo "After deleting policy Suspicious Filesystem Changes 2, policy was still present?"
    exit 1
fi

# Make a copy again, but this time delete by id
NEW_POLICY=`echo $MY_POLICY | sed -e "s/Suspicious Filesystem Changes/Another Copy Of Suspicious Filesystem Changes/g" | sed -e 's/"id": [0-9]*,//' | sed -e 's/"version": [0-9]*/"version": null/'`
OUT=`echo $NEW_POLICY | $SCRIPTDIR/../examples/add_policy.py $PYTHON_SDC_TEST_API_TOKEN`
if [[ $OUT != *"\"Another Copy Of Suspicious Filesystem Changes\""* ]]; then
    echo "Could not create new policy"
    exit 1
fi

ID=`echo $OUT | grep -E -o '"id": [^,]+,' | awk '{print $2}' | awk -F, '{print $1}'`

OUT=`$SCRIPTDIR/../examples/delete_policy.py --id $ID $PYTHON_SDC_TEST_API_TOKEN`
if [[ $OUT != *"\"Another Copy Of Suspicious Filesystem Changes\""* ]]; then
    echo "Could not delete policy \"Another Copy Of Suspicious Filesystem Changes\""
    exit 1
fi

OUT=`$SCRIPTDIR/../examples/list_policies.py $PYTHON_SDC_TEST_API_TOKEN`
if [[ $OUT = *"\"Another Copy Of Write below binary dir\""* ]]; then
    echo "After deleting policy Another Copy Of Suspicious Filesystem Changes, policy was still present?"
    exit 1
fi

# Trigger some events
FOUND=0

for i in $(seq 10); do
    sudo cat /etc/shadow
    sleep 10

    EVTS=`$SCRIPTDIR/../examples/get_secure_policy_events.py $PYTHON_SDC_TEST_API_TOKEN 60`

    if [[ "$EVTS" != "" ]]; then
       FOUND=1
       break;
    fi
done

if [[ $FOUND == 0 ]]; then
   echo "Did not find any policy events after 10 attempts..."
   exit 1
fi