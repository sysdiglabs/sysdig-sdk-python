#!/usr/bin/env python
#
# Set the sysdig secure default rules files.
#
# The _files programs and endpoints are a replacement for the
# system_file endpoints and allow for publishing multiple files
# instead of a single file as well as publishing multiple variants of
# a given file that are compatible with different agent versions.
#

import getopt
import os
import sys

import yaml

from sdcclient import SdSecureClient


#
# Parse arguments
#
def usage():
    print(
        (
            "usage: %s [-l|--load <path>] [-t|--tag <tag>] [-c|--content <content>] <sysdig-token>"
            % sys.argv[0]
        )
    )
    print(
        "-l|--load: load the files to set from a set of files below <path> using load_default_rules_files()."
    )
    print("-t|--tag: Set a tag for the set of files")
    print("-c|--content: the (single) file to set")
    print("if --load is specified, neither --tag nor --content can be specified")
    print("You can find your token at https://secure.sysdig.com/#/settings/user")
    sys.exit(1)


try:
    opts, args = getopt.getopt(
        sys.argv[1:], "l:t:n:c:", ["load=", "tag=", "name=", "content="]
    )
except getopt.GetoptError:
    usage()

load_dir = ""
tag = ""
cpath = ""
for opt, arg in opts:
    if opt in ("-l", "--load"):
        load_dir = arg
    elif opt in ("-t", "--tag"):
        tag = arg
    elif opt in ("-c", "--content"):
        cpath = arg

if load_dir != "" and (tag != "" or cpath != ""):
    usage()
#
# Parse arguments
#
if len(args) != 1:
    usage()

sdc_token = args[0]

#
# Instantiate the SDC client
#
sdclient = SdSecureClient(sdc_token, "https://secure.sysdig.com")

files_obj = {}
if load_dir != "":
    print(("Loading falco rules files from {}...".format(load_dir)))
    ok, res = sdclient.load_default_falco_rules_files(load_dir)
    if ok:
        files_obj = res
    else:
        print(res)
        sys.exit(1)
else:
    with open(cpath, "r") as content_file:
        content = content_file.read()
        required_engine_version = 0
        cyaml = yaml.safe_load(content)
        for obj in cyaml:
            if "required_engine_version" in obj:
                try:
                    required_engine_version = int(obj["required_engine_version"])
                except ValueError:
                    print(
                        (
                            'Required engine version "{}" in content {} must be a number'.format(
                                obj["required_engine_version"], cpath
                            )
                        )
                    )
                    sys.exit(1)
        files_obj = {
            "tag": tag,
            "files": [
                {
                    "name": os.path.basename(cpath),
                    "variants": {
                        "required_engine_version": required_engine_version,
                        "content": content,
                    },
                }
            ],
        }

ok, res = sdclient.set_default_falco_rules_files(files_obj)

#
# Return the result
#
if ok:
    print("default falco rules files set successfully")
else:
    print(res)
    sys.exit(1)
