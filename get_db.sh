#!/usr/bin/env python
"""
Name: utils.py
Description: Utility functions
Version: 
Author: 
"""

import sys
import os
#import yaml
import json
import argparse
import subprocess

from utils import print_info, print_warning, print_error, raise_error 
from utils import check_cf_config, omg

DOMAIN=".kesselrun.org"


def extract_tools():
  """
    Extract tools from the S3.
  """
  MC="/usr/local/bin/mc"
  print_warning("Remove this patch");
  MC="stubs/mc"
  SSH_PASS="sshpass"
  

  if ( not os.path.exists(MC)):
      raise_error("The minio client (%s) was not found." % MC)
    
  if ( os.path.exists(SSH_PASS)):
    return True

  the_command="mc cp ecs/docker-images/s3/masterblaster.tgz ."
  ret = subprocess.call(the_command, shell=True)
  if (ret != 0 ):
      raise_error("Failed the following command: %s " % the_command)
  

  the_command="tar xzf masterblaster.tgz ./rootfs/usr/bin/sshpass"
  ret = subprocess.call(the_command, shell=True)
  #if (ret != 0 ):
  #    raise_error("Failed the following command: %s " % the_command)

  #the_command="ln -s ./rootfs/usr/bin/sshpass ./sshpass"
  #ret = subprocess.call(the_command, shell=True)
  
  print_warning("Must clean up after the run")

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument('--aws', action='store_true')
    args = parser.parse_args()

    os.environ['PATH']="./stubs:" + os.environ['PATH'];

    site="usec"
    foundation="fulcrum"
    org="slapshot"
    space="usec"
    app_name="org"
    db_name="slapshot-db"

    db_name="slapshot-usec"
    db_user_name="service_instance_db"
    db_user_password="foobar"
    service_guid="foobar"


    DOMAIN=".kesselrun.org"

    opsman_fqdn="opsman"+foundation+site+DOMAIN
    opsman_url="https://"+opsman_fqdn
    jumpbox_fqdn="jumpbox"+site+DOMAIN

    temp_working_dire="/tmp/db_dump_work"


    

    # check that the cf CLI is properly configured
    check_cf_config(site, foundation, org, space, True)

    # get the required passwords
    omg(site, foundation)

    extract_tools();

    raise_error("Early exit!");     ##############<<<<<<

    #print_info("This is the PATH: " + os.environ['PATH']);

    check_app_name("foobar")
    check_org_name("foobar")
    check_foundation_name("foobar")
    check_space_name("foobar")
    check_site_name("foobar")
    set_constants();
    check_constants();

    check_cf_config("eu", "fulcrum", "org", "space", True)

    is_key("foobar");
    execute_over_ssh ("u", "c", "f", "c")


    credhub_login("foobar");

    omg("r", "f")





ForeRED = "\033[01;31m{0}\033[00m"
ForeYELLOW = "\033[01;32m{0}\033[00m"
ForeBLUE = "\033[01;33m{0}\033[00m"

HOME = os.getenv("HOME") + "/mdc-secrets/"

OPS_CONCOURSE_CREDS_FILE="/home/ubuntu/mcp-secrets/concourse/ops/creds.yml"

DOMAIN=".kesselrun.org"
CF_API_TEMPLATE="api.system.{0}.{1}"+DOMAIN
CF_CONFIG_FILE_NAME="~/.cf/config.json"


PARAM_FILES = (
    "director/director-params{0}.yml".format('-aws' if args.aws else ''),
    "director/cloud-config-params{0}.yml".format('-aws' if args.aws else ''),
    "concourse/concourse-params{0}.yml".format('-aws' if args.aws else '')
)

REPO_PATH = os.path.dirname(os.path.realpath(__file__))


def read_yml(RFILE):
    try:
        with open(RFILE, "r") as read_file:
            ymlSecrets = yaml.load(read_file)
    except ValueError:
        print (ForeRED.format("%s Not a valid yml file!" %(RFILE)))
    return ymlSecrets


def save_yml(OLD_PARAM_FILE, OLD_PARAM_YML, ADD_KEYS, ADD_VALUES):
    with open(OLD_PARAM_FILE, 'a') as OLD_PARAM_FILE1:
        try:
            for i in range(len(ADD_KEYS)):
                item = ADD_KEYS[i]
                value = ADD_VALUES[i]
                OLD_PARAM_FILE1.write("{0}: {1}\n".format(item, value if value else ''))
            OLD_PARAM_FILE1.close()
        except yaml.YAMLError as exc:
            print(exc)

def build_msg(pfx, a_string):
  theFrame=sys._getframe(2);
  lineno=theFrame.f_lineno
  #print"This is the line number: %d" % lineno
  msg="%s: line: %d---%s" % (pfx, lineno, a_string)
  return(msg)

def print_info(a_string):
  msg=build_msg ("INFO", a_string);
  print (ForeBLUE.format("%s" %(msg)))


def print_warning(a_string):
  "This function prints a warning message"
  msg=build_msg ("WARNING", a_string);

  print (ForeYELLOW.format("%s" %(msg)))

def print_error(a_string):
  msg=build_msg ("ERROR", a_string);
  print (ForeRED.format("%s" %(msg)))

def raise_error(a_string):
  msg=build_msg ("ERROR", a_string);
  print (ForeRED.format("%s" %(msg)))
  raise SystemExit(1)

def check_app_name(a_string):
## Returns True if the specified app exists in the org and space  
  print_info("checking app named: " + a_string);
  print_warning("Fix this patch");
  return True;


#######################################################
def check_foundation_name(a_string):
## Returns True if the specified foundation exists
  print_info("checking foundation named: " + a_string);
  print_warning("Fix this patch");
  return True;


#######################################################
def check_org_name(a_string):
## Returns True if the specified org exists
  print_info("checking org named: " + a_string);
  print_warning("Fix this patch");
  return True;


#######################################################
def check_space_name(a_string):
## Returns True if the specified space exists
  print_info("checking space named: " + a_string);
  print_warning("Fix this patch");
  return True;


#######################################################
def check_site_name(a_string):
## Returns True if the specified site exists
  print_info("checking site named: " + a_string);
  print_warning("Fix this patch");
  return True;


#######################################################
def set_constants():
  #print_warning("Fix this patch");
  return True;

#######################################################
def check_constants():
  print_warning("Check OPS_CONCOURSE_CREDS_FILE here!")
  return True;

#######################################################
def jq(cmd, fn):
  """
    Runs the jq 'cmd' on the file named 'fn'
  """
  print_warning ("Stubbed the returned value")
  return "https://aapi.system.fulcrum.eu.kesselrun.org"

#######################################################
def check_cf_config(region, foundation, org, space, force_flag=False):
  """
  Input CF deployment description
  Returns True or False

  if CF_CONFIG_FILE_NAME exists
    if .Target value is the expected URL, 
      return True

  if force_flag is true 
    login to CF 
    check .Target
    return True

  return False
  """

  print_warning ("Check this code")

  end_point=CF_API_TEMPLATE.format(foundation, region)
  print_info ("This is the endpoint: "+end_point)

  print_warning("Stubbed the opsman password.")
  pw="foobar"

  cmd_template="cf login -u admin -p {0} -a {1} -o {2} -s {3}"
  the_command=cmd_template.format(pw, foundation, org, space)
  print_info ("This is the command: "+the_command)

  print_warning("patched the cf command");
  the_command=["ls", "-al", "."]


  expected_url="https://"+end_point
  print_info ("This is the expected URL: "+expected_url)

  jq_cmd=".Target"
  if (True or os.path.exists(CF_CONFIG_FILE_NAME)):
    ret_val = jq(jq_cmd, CF_CONFIG_FILE_NAME)
    print_info("This is the returned value: " + ret_val);
    if (ret_val == expected_url):
      return True
      
  if( force_flag ):
    print_info("Forcing the login")
    p = subprocess.Popen(the_command,
                          stdin=subprocess.PIPE,
                          stdout=subprocess.PIPE,
                          stderr=subprocess.PIPE
                        )
    #p = subprocess.Popen('ls -l')
    #p = subprocess.Popen(the_command, bufsize=1);
    out, err = p.communicate(None)
    #print_warning("This is the error status from the read: " + err)
    print_info("This is the result from the read: " + out)

    print_warning("Remove this patch")
    if (False or os.path.exists(CF_CONFIG_FILE_NAME)):
      raise_error("The CF configuration file should have been created.")

    ret_val = jq(jq_cmd, CF_CONFIG_FILE_NAME)
    print_info("This is the returned value: " + ret_val);
    if (ret_val == expected_url):
      return True
      
    
  print_warning("Not connected to CF.")
  print_warning("Try this command: %s" %"SOME COMMAND")

  print_warning("Returning false");

  return False


#######################################################
def credhub_login(file_name):
  """
  Log onto 'credhub'
    
  """

  print_warning ("Entering the function!")

  bosh_command="bosh int %s --path /credhub-ca/ca" % file_name
  print_info ("bosh command: "+bosh_command )
  ch_command="credhub api --ca-cert=%s --server=https://ciops%s:8844" % ("foobar", DOMAIN)
  print_info ("ch command: "+ch_command )

  print_warning("Add BOSH and credhub commands here.")

  bosh_command="bosh login %s --path /concourse_to_credhub_secret" % file_name
  print_info ("bosh command: "+bosh_command )

  ch_command="credhub login --client-name=concourse_to_credhub --client_secret=%s" %("foobar")
  print_info ("ch command: "+ch_command )

  print_warning("Add BOSH and credhub commands here")

  print_warning ("Leaving the function!")

  return False



#######################################################
def omg(region, foundation, force=False):
  """
  Returns the credentials for various components of the specified foundation.

  TO_DO:  Buffer the credentials for given arguments
  """
  print_warning ("Entering code")

  print_info("check for existence")

  print_info("Login with the CredHub");

  credhub_login(OPS_CONCOURSE_CREDS_FILE)

  the_command="credhub get -n /concourse/%s-%s/opsman_admin_password | tail -3 head -1 | awk '{print $2}'" \
                        % (region, foundation)
  print_info("This is the command: "+the_command)
  opsman_pw = "foobar"

  #  Retrieve Produce ID from OM
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


#######################################################
def is_key(a_string):
  """
    Returns True if the regular expression "^----BEGIN.*PRIVATE KEY----" is
    found.
  """
  print_warning ("Fix this code")
  return False
  
#######################################################
def execute_over_ssh (user_name, creds, fqdn, cmd):
  """
    Executes the specified command on the specified host using the specified
    arguments.
  """
  print_warning ("Fix this code")

  if is_key(creds):
    
    """
      --- pseudo code ---
      fn=fqdn + ".pem"
      echo creds > fn
      chmod 0400 fn
      ssh -q -o StrictHostKeyChecking=no -i fn user_name@fqdn
      rm fn
    """
    pass
  else:
    """
      sshpass  -p creds  ssh -q -o StrictHostKeyChecking=no -i fn
      user_name@fqdn cmd
    """
    pass

  return False


