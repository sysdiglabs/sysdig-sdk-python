#!/bin/bash

set -euxo pipefail

# Start an agent using the testing account API key to send some data
docker run -d -it --rm --name sysdig-agent --privileged --net host --pid host -e COLLECTOR=collector-staging.sysdigcloud.com -e ACCESS_KEY=$PYTHON_SDC_TEST_ACCESS_KEY -v /var/run/docker.sock:/host/var/run/docker.sock  -v /dev:/host/dev -v /proc:/host/proc:ro -v /boot:/host/boot:ro -v /lib/modules:/host/lib/modules:ro -v /usr:/host/usr:ro --shm-size=350m sysdig/agent

# make sure the agent starts sending data and the backend makes it available via API
sleep 60

# Start the falco event generator to generate policy events in Secure
docker run --rm -d -it falcosecurity/event-generator run syscall
