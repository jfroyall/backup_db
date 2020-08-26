##\file Main interface to CredHub

import yaml
from utils import (print_info, print_warning, print_error)

class CredHub():
  def __init__(self, creds_file):
    print_info("Into the function")
    print_info("class name is: "+ CredHub.__name__)

    with open(creds_file, 'r') as f:
        yml_creds = yaml.safe_load(f)
    #print(yml_creds);
    ca_cert = yml_creds['credhub_tls']['ca']

    #print(ca_cert);
    #print(type(yml_creds));
    #print(yml_creds.keys());

    print_info("Leaving the function")

  ## Destructor function
  def __del__(self):
    print_info("Into the destructor")
    print_info("Leaving the destructor")


