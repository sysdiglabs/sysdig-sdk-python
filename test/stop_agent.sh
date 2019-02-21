#!/bin/bash

set -euxo pipefail

docker logs sysdig-agent
docker stop sysdig-agent
