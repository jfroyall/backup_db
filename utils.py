#!/usr/bin/env python
"""
Name: utils.py
Description: Utility functions
Version: 
Author: 
"""

import os
#import yaml
import json
import argparse
import subprocess


parser = argparse.ArgumentParser()
parser.add_argument('--aws', action='store_true')
args = parser.parse_args()


ForeRED = "\033[01;31m{0}\033[00m"
ForeYELLOW = "\033[01;32m{0}\033[00m"
ForeBLUE = "\033[01;33m{0}\033[00m"

HOME = os.getenv("HOME") + "/mdc-secrets/"

OPS_CONCOURSE_CREDS_FILE="/home/ubuntu/mcp-secrets/concourse/ops/creds.yml"

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

def print_info(a_string):
  "This function prints an informational message"
  print (ForeBLUE.format("info: %s" %(a_string)))

def print_warning(a_string):
  "This function prints a warning message"
  print (ForeYELLOW.format("warning: %s" %(a_string)))

def print_error(a_string):
  print (ForeRED.format("error: %s" %(a_string)))

def raise_error(a_string):
  print (ForeRED.format("error: %s" %(a_string)))
  raise SystemExit(1)

def check_app_name(a_string):
  print_info("checking app named: " + a_string);
  print_warning("Fix this patch");
  return True;


#######################################################
def check_foundation_name(a_string):
  print_info("checking foundation named: " + a_string);
  print_warning("Fix this patch");
  return True;


#######################################################
def check_org_name(a_string):
  print_info("checking org named: " + a_string);
  print_warning("Fix this patch");
  return True;


#######################################################
def check_space_name(a_string):
  print_info("checking space named: " + a_string);
  print_warning("Fix this patch");
  return True;


#######################################################
def check_site_name(a_string):
  print_info("checking site named: " + a_string);
  print_warning("Fix this patch");
  return True;


#######################################################
def set_constants():
  print_warning("Fix this patch");
  return True;

#######################################################
def check_constants():
  print_warning("Fix this patch");
  print_warning("Check OPS_CONCOURSE_CREDS_FILE here!")
  return True;

DOMAIN=".kesselrun.org"
CF_API_TEMPLATE="api.system.{0}.{1}"+DOMAIN
CF_CONFIG_FILE_NAME="~/.cf/config.json"


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
  print_error ("Fix this code")
  return False

#######################################################
def omg(region, foundation):
  print_error ("Fix this code")
  return False

#######################################################
def is_key(a_string):
  print_error ("Fix this code")
  return False
  
#######################################################
def execute_over_ssh (user_name, creds, fqdn, cmd):
  print_error ("Fix this code")
  return False



if __name__ == "__main__":

    print_info ("info test")
    print_warning ("warning test")
    print_error ("error test")
    check_app_name("foobar")
    check_org_name("foobar")
    check_foundation_name("foobar")
    check_space_name("foobar")
    check_site_name("foobar")

    set_constants();
    check_constants();

    check_cf_config("eu", "fulcrum", "org", "space", True)

    credhub_login("foobar");

    omg("r", "f")

    is_key("k")
    execute_over_ssh ("u", "c", "f", "c")


    raise_error("Early exit %s!" %(REPO_PATH))


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
