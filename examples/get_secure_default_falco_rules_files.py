#!/usr/bin/env python
#
# Get the sysdig secure default rules files.
#
# The _files programs and endpoints are a replacement for the
# system_file endpoints and allow for publishing multiple files
# instead of a single file as well as publishing multiple variants of
# a given file that are compatible with different agent versions.
#

import os
import sys
import pprint
import getopt
import shutil
sys.path.insert(0, os.path.join(os.path.dirname(os.path.realpath(sys.argv[0])), '..'))
from sdcclient import SdSecureClient

#
# Parse arguments
#
def usage():
    print 'usage: %s [-s|--save <path>] <sysdig-token>' % sys.argv[0]
    print '-s|--save: save the retrieved files to a set of files below <path> using save_default_rules_files().'
    print 'You can find your token at https://secure.sysdig.com/#/settings/user'
    sys.exit(1)

try:
    opts, args = getopt.getopt(sys.argv[1:],"s:",["save="])
except getopt.GetoptError:
    usage()

save_dir = ""
for opt, arg in opts:
    if opt in ("-s", "--save"):
        save_dir = arg

#
# Parse arguments
#
if len(args) != 1:
    usage()

sdc_token = args[0]

#
# Instantiate the SDC client
#
sdclient = SdSecureClient(sdc_token, 'https://secure.sysdig.com')

#
# Get the configuration
#
res = sdclient.get_default_falco_rules_files()

#
# Return the result
#
if res[0]:
    if save_dir == "":
        pp = pprint.PrettyPrinter(indent=4)
        pp.pprint(res[1])
    else:
        print "Saving falco rules files below {}...".format(save_dir)
        sres = sdclient.save_default_falco_rules_files(res[1], save_dir)
        if not sres[0]:
            print sres[1]
else:
    print res[1]
    sys.exit(1)
