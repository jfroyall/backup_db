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

import omg



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


#print_info("Create a CredHub instance")
#credHub=CredHub();
#
#print_info("Create a Bosh instance")
#bosh=Bosh.Bosh('test_data/bosh-creds.yml');


#print_info("Create a CloudFoundry instance")
omg.omg(infile_name, "no.where.net", "eu", "atlas");

#print_info("Create a CloudFoundry instance")
#
print_info("Goodbye World!")
#
#
sys.exit(0)
