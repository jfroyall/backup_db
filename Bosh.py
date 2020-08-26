##\file Main interface to BOSH

import os
import yaml
import argparse
from sys import exit

from utils import (print_info, print_warning, print_error)

## Class definition
class Bosh():

  def __loginConcourseCredhub (concourse_creds_file, concourse_host):
      with open(creds, 'r') as f:
          yml_creds = yaml.load(f)
      ca_cert = yml_creds['credhub_tls']['ca']
      os.environ['CREDHUB_CA_CERT'] = ca_cert
      print_info ("Logging into Concourse Credhub")
      cmd_credhub_api = "credhub api --server=%s:8844" % (concourse_host)
      cmd_credhub_login = "credhub login --client-name=concourse_to_credhub --client-secret=`bosh int %s --path /concourse_to_credhub_secret`" % (concourse_creds_file)
      os.system(cmd_credhub_api)
      os.system(cmd_credhub_login)
      print ("Successfully logged in")

  def __loginDirectorCredhub (SECRETS):
      cmd_credhub_api = "credhub api --ca-cert=<(bosh int %s/director/creds.yml --path /credhub_ca/ca) --ca-cert=<(bosh int %s/director/creds.yml --path /uaa_ssl/ca) --server=192.168.5.5:8844" % (SECRETS)
      cmd_credhub_login = "credhub login --client-name=director_to_credhub --client-secret=`bosh int %s/director/creds.yml --path /uaa_clients_director_to_credhub`" % (SECRETS)
      os.system(cmd_credhub_api)
      os.system(cmd_credhub_login)

  ## Initialization function
  def __init__(self, creds_file):
    print_info("Into the function")

    with open(creds_file, 'r') as f:
        yml_creds = yaml.load(f)
    #print(yml_creds);
    ca_cert = yml_creds['credhub_tls']['ca']

    print(ca_cert);
    print(type(yml_creds));
    print(yml_creds.keys());

    print_info("Leaving the function")

  ## Destructor function
  def __del__(self):
    print_info("Into the destructor")
    print_info("Leaving the destructor")


