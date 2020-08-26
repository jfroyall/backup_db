#!/usr/bin/env python
##\file Description: Utility functions
#
#Name: utils.py
#Version: 
#Author: 

import sys
import os
#import yaml
import json
import argparse
import subprocess


ForeRED = "\033[01;31m{0}\033[00m"
ForeYELLOW = "\033[01;32m{0}\033[00m"
ForeBLUE = "\033[01;33m{0}\033[00m"

HOME = os.getenv("HOME") + "/mdc-secrets/"

OPS_CONCOURSE_CREDS_FILE="/home/ubuntu/mcp-secrets/concourse/ops/creds.yml"

DOMAIN=".kesselrun.org"
CF_API_TEMPLATE="api.system.{0}.{1}"+DOMAIN
CF_CONFIG_FILE_NAME="~/.cf/config.json"


## \todo remove this code
def read_yml(RFILE):
    try:
        with open(RFILE, "r") as read_file:
            ymlSecrets = yaml.load(read_file)
    except ValueError:
        print (ForeRED.format("%s Not a valid yml file!" %(RFILE)))
    return ymlSecrets


## \todo remove this code
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

## Builds a default message string
def build_msg(pfx, a_string):
  theFrame=sys._getframe(2);
  lineno=theFrame.f_lineno
  #print"This is the line number: %d" % lineno
  msg="%s: line: %d---%s" % (pfx, lineno, a_string)
  return(msg)

## Print informational messages
def print_info(a_string):
  msg=build_msg ("INFO", a_string);
  print (ForeBLUE.format("%s" %(msg)))


## Print warning messages
def print_warning(a_string):
  "This function prints a warning message"
  msg=build_msg ("WARNING", a_string);

  print (ForeYELLOW.format("%s" %(msg)))

## Print error messages
def print_error(a_string):
  msg=build_msg ("ERROR", a_string);
  print (ForeRED.format("%s" %(msg)))

## Used to raise errors
def raise_error(a_string):
  msg=build_msg ("ERROR", a_string);
  print (ForeRED.format("%s" %(msg)))
  raise SystemExit(1)

## Returns True if the specified app exists in the org and space  
def check_app_name(a_string):
  print_info("checking app named: " + a_string);
  print_warning("Fix this patch");
  return True;


#######################################################
## Returns True if the specified foundation exists
def check_foundation_name(a_string):
  print_info("checking foundation named: " + a_string);
  print_warning("Fix this patch");
  return True;


#######################################################
## Returns True if the specified org exists
def check_org_name(a_string):
  print_info("checking org named: " + a_string);
  print_warning("Fix this patch");
  return True;


#######################################################
## Returns True if the specified space exists
def check_space_name(a_string):
  print_info("checking space named: " + a_string);
  print_warning("Fix this patch");
  return True;


#######################################################
## Returns True if the specified site exists
def check_site_name(a_string):
  print_info("checking site named: " + a_string);
  print_warning("Fix this patch");
  return True;


#######################################################
## Set a few constants \todo This may not be needed
def set_constants():
  #print_warning("Fix this patch");
  return True;

#######################################################
## Verify constants \todo This may not be needed
def check_constants():
  print_warning("Check OPS_CONCOURSE_CREDS_FILE here!")
  return True;

#######################################################
## Runs the jq 'cmd' on the file named 'fn'
def jq(cmd, fn):
  print_warning ("Stubbed the returned value")
  return "https://aapi.system.fulcrum.eu.kesselrun.org"

#######################################################
## Check the CloudFoundry configuration
# \verbatim
#  Input CF deployment description
#  Returns True or False
#
#  if CF_CONFIG_FILE_NAME exists
#    if .Target value is the expected URL, 
#      return True
#
#  if force_flag is true 
#    login to CF 
#    check .Target
#    return True
#
#  return False
# \endverbatim
def check_cf_config(region, foundation, org, space, force_flag=False):

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
## Log onto 'credhub'
def credhub_login(file_name):

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


if __name__ == "__main__":


    parser = argparse.ArgumentParser()
    parser.add_argument('--aws', action='store_true')
    args = parser.parse_args()


    ## \todo remove this code
    PARAM_FILES = (
        "director/director-params{0}.yml".format('-aws' if args.aws else ''),
        "director/cloud-config-params{0}.yml".format('-aws' if args.aws else ''),
        "concourse/concourse-params{0}.yml".format('-aws' if args.aws else '')
    )

    REPO_PATH = os.path.dirname(os.path.realpath(__file__))

    os.environ['PATH']="./stubs:" + os.environ['PATH'];
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


    raise_error("Early exit!");     ##############<<<<<<





    for PARAM in PARAM_FILES:
        if "director" in PARAM:
            ADD_KEYS = []
            ADD_VALUES = []
            APP = "director"
            OLD_PARAM_FILE = HOME + PARAM
            if not os.path.isfile(OLD_PARAM_FILE):
                print (ForeRED.format("Creating %s" %(OLD_PARAM_FILE)))
                os.system("mkdir -p %s/%s" %(HOME, APP))
                os.system("cp %s/templates/%s %s" %(REPO_PATH, PARAM, OLD_PARAM_FILE))
            else:
                NEW_PARAM = ("%s/templates/%s" %(REPO_PATH, PARAM))

                OLD_PARAM_YML = read_yml(OLD_PARAM_FILE)
                NEW_PARAM_YML = read_yml(NEW_PARAM)
                print ("Adding new params to %s" %(OLD_PARAM_FILE))

                for key, value in NEW_PARAM_YML.iteritems():
                    if key not in OLD_PARAM_YML:
                        ADD_KEYS.append(key)
                        ADD_VALUES.append(value)
                        print (ForeRED.format("adding %s to %s" %(key, OLD_PARAM_FILE)))
                    else:
                        print ("%s found in %s" %(key, OLD_PARAM_FILE))

                save_yml(OLD_PARAM_FILE, OLD_PARAM_YML, ADD_KEYS, ADD_VALUES)
        if "concourse" in PARAM:
            APP = "concourse"
            for SERVER in ['app','ops']:
                ADD_KEYS = []
                ADD_VALUES = []
                OLD_PARAM_FILE = HOME + "concourse/" + SERVER +"/concourse-params.yml"

                if not os.path.isfile(OLD_PARAM_FILE):
                    print (ForeRED.format("Creating %s" %(OLD_PARAM_FILE)))
                    os.system("mkdir -p %s/%s/%s" %(HOME, APP, SERVER))
                    os.system("cp %s/templates/%s %s" %(REPO_PATH, PARAM, OLD_PARAM_FILE))
                else:
                    NEW_PARAM = ("%s/templates/%s" %(REPO_PATH, PARAM))

                    OLD_PARAM_YML = read_yml(OLD_PARAM_FILE)
                    NEW_PARAM_YML = read_yml(NEW_PARAM)
                    print ("Adding new params to %s" %(OLD_PARAM_FILE))

                    for key, value in NEW_PARAM_YML.iteritems():
                        if key not in OLD_PARAM_YML:
                            ADD_KEYS.append(key)
                            ADD_VALUES.append(value)
                            print (ForeRED.format("adding %s to %s" %(key, OLD_PARAM_FILE)))
                        else:
                            print ("%s found in %s" %(key, OLD_PARAM_FILE))

                    save_yml(OLD_PARAM_FILE, OLD_PARAM_YML, ADD_KEYS, ADD_VALUES)
