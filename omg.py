##\file Description: rehost of omg/lol script
#

import subprocess

from   utils import print_info, print_warning, print_error

import CredHub
import Bosh

#######################################################
## Returns the credentials for various components of the specified foundation.
#
#  TO_DO:  Buffer the credentials for given arguments
def omg(credsFileName, DOMAIN,  region, foundation, force=False):
  print_warning ("Entering code")

  print_info("check for existence")

  print_info("Login with the CredHub");

  #credhub_login(OPS_CONCOURSE_CREDS_FILE)
  credHub=CredHub.CredHub(credsFileName)

  the_command="credhub get -n /concourse/%s-%s/opsman_admin_password | tail -3 head -1 | awk '{print $2}'" \
                        % (region, foundation)
  print_info("This is the command: "+the_command)
  opsman_pw = "foobar"

  #  Retrieve Product ID from OM
  opsman_url="https://opsman.%s.%s%s" %(foundation, region, DOMAIN) 
  print_info("This is the URL: "+opsman_url)

  the_command="./stubs/om -t %s  -u admin -p %s -k curl -s -p /api/v0/deployed/products" % (opsman_url, opsman_pw)
  the_command="./stubs/om"
  print_info("This is the command: "+the_command)
  p = subprocess.Popen(the_command,
                          stdin=subprocess.PIPE,
                          stdout=subprocess.PIPE,
                          stderr=subprocess.PIPE
                        )
  out, err = p.communicate(None)
  print_info("This is the result from the read: " + out)


  #  Run this command to get the product ID
  the_command="echo %s | jq '.[] | select(.type==\"cf\") | .installation_name'" % out;
  print_warning("This command must be implemented: "+the_command)
  product_id="FOOBAR"

  

  #  Run this command to get the director's password
  the_command="om -t %s  -u admin -p %s -k curl -s -p /api/v0/deployed/products/%s/credentials/.uaa.admin_credentials" % (opsman_url, opsman_pw, product_id)
  print_info("This is the command: "+the_command)
  p = subprocess.Popen(the_command,
                          shell=True,
                          stdin=subprocess.PIPE,
                          stdout=subprocess.PIPE,
                          stderr=subprocess.PIPE
                        )
  out, err = p.communicate(None)
  print_info("This is the result from the read: " + out)
  #  Run this command to get the product ID
  the_command="echo %s | jq '.credential.value.password'" % out
  print_warning("This command must be implemented: "+the_command)
  appsman_password="FOOBAR"


  #  Run this command to get the opsman's SSH password
  the_command="om -t %s  -u admin -p %s -k curl -s -p /api/v0/deployed/director/credentials/uaa_admin_user_credentials"\
                        % (opsman_url, opsman_pw)
  print_info("This is the command: "+the_command)
  p = subprocess.Popen(the_command,
                          shell=True,
                          stdin=subprocess.PIPE,
                          stdout=subprocess.PIPE,
                          stderr=subprocess.PIPE
                        )
  out, err = p.communicate(None)
  print_info("This is the result from the read: " + out)
  #  Run this command to get the product ID
  the_command="echo %s | jq '.credential.value.password'" % out
  print_warning("This command must be implemented: "+the_command)
  opssman_ssh_password="FOOBAR"


  print_warning ("Still need to collect all of the passwords in one dictionary")

  print_warning ("Leaving code")

  return False
