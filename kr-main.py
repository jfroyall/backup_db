#!/usr/local/bin/python
##\file Main KR file

import sys
import os
import yaml
import json
import optparse
import subprocess


from   utils import print_info, print_warning, print_error
import Bosh
from   CredHub import CredHub




#if __name__ == "__main__":

print_info("Hello World!")

p= optparse.OptionParser()

p.add_option("-f", "--file", action="store", type="string", dest="infile")

p.set_defaults(infile="foobar")

opt, args = p.parse_args()

print_info("input file is: "+opt.infile)

infile_name=opt.infile

args = p.parse_args()
if not os.path.isfile(infile_name):
    print_error ("File '%s' does not exist!" % infile_name)
    sys.exit(1)


#parser = optparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
#
#required = parser.add_argument_group('required argument')
#required.add_argument(
#                        '-f', '--file',
#                        help='File to process',
#                        type=str,
#                        metavar='/path/to/file',
#                        required=True,
#                    )
#
#requiredgroupA = parser.add_mutually_exclusive_group(required=True,)
#requiredgroupA.add_argument(
#    '-d',
#    '--director',
#    help='Targets director credhub server',
#    action="store_true",
#)

#requiredgroupA.add_argument(
#    '-co',
#    '--concourse-ops',
#    help='Targets concourse-ops credhub server',
#    action="store_true",
#)

#requiredgroupA.add_argument(
#    '-ca',
#    '--concourse-app',
#    help='Targets concourse-app credhub server',
#    action="store_true",
#)
#

#parser.add_argument(
#    '--aws',
#    help='Targets AWS',
#    action='store_true'
#)

#parser.add_argument(
#    '--skip-tls-verification',
#    help='Skip TLS verification',
#    action='store_true'
#)



#if args.aws:
#    secrets_repo = os.path.expanduser("~/mdc-secrets")
#else:
#    secrets_repo = "/home/ubuntu/mdc-secrets"
#
#concourse_type = 'ops' if args.concourse_ops else 'app'
#concourse_params = os.path.join(secrets_repo, "concourse/{}/concourse-params.yml".format(concourse_type))
#
#
#credHub=CredHub();
#bosh=Bosh.Bosh('test_data/bosh-creds.yml');
#
#print_info("Create a CredHub instance")
#print_info("Create a Bosh instance")
#print_info("Create a CloudFoundry instance")
#
print_info("Goodbye World!")
#
#
sys.exit(0)
