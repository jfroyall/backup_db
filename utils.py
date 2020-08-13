#!/usr/bin/env python
"""
Name: utils.py
Description: Utility functions
Version: 
Author: 
"""
import os
#import yaml
import argparse


parser = argparse.ArgumentParser()
parser.add_argument('--aws', action='store_true')
args = parser.parse_args()


ForeRED = "\033[01;31m{0}\033[00m"
ForeYELLOW = "\033[01;32m{0}\033[00m"
ForeBLUE = "\033[01;33m{0}\033[00m"
HOME = os.getenv("HOME") + "/mdc-secrets/"
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
  print (ForeBLUE.format("info: %s" %(a_string)))

def print_warning(a_string):
  print (ForeYELLOW.format("warning: %s" %(a_string)))

def print_error(a_string):
  print (ForeRED.format("error: %s" %(a_string)))

def check_app_name(a_string):
  print_info("checking app named: " + a_string);
  print_warning("Fix this patch");
  return True;


def check_foundation_name(a_string):
  print_info("checking foundation named: " + a_string);
  print_warning("Fix this patch");
  return True;


def check_org_name(a_string):
  print_info("checking org named: " + a_string);
  print_warning("Fix this patch");
  return True;


def check_space_name(a_string):
  print_info("checking space named: " + a_string);
  print_warning("Fix this patch");
  return True;


def check_site_name(a_string):
  print_info("checking site named: " + a_string);
  print_warning("Fix this patch");
  return True;


def set_constants():
  print_warning("Fix this patch");
  return True;

def check_constants():
  print_warning("Fix this patch");
  print_warning("Check OPS_CONCOURSE_CREDS_FILE here!")
  return True;


def check_cf_config(region, foundation, org, space):
  print_error ("Fix this code")
  return False

def credhub_login(file_name):
  print_error ("Fix this code")
  return False

def omg(region, foundation):
  print_error ("Fix this code")
  return False

def is_key(a_string):
  print_error ("Fix this code")
  return False
  
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

    check_cf_config("r", "f", "o", "s")
    credhub_login("foobar");

    omg("r", "f")

    is_key("k")
    execute_over_ssh ("u", "c", "f", "c")



    print (ForeRED.format("Early exit %s" %(REPO_PATH)))

    exit(1);


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
