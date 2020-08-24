#!/bin/bash

function error_exit() {
  echo "Message--- $1"
  echo "An error occured in function ${FUNCNAME[1]} at line ${BASH_LINENO[0]} of file ${BASH_SOURCE[1]}"
  exit 1
}

function early_exit() {
  echo "Early exit called from function ${FUNCNAME[1]} at line ${BASH_LINENO[0]} of file ${BASH_SOURCE[1]}"
  exit 1
}

function print_error() {
  echo -e "\033[31;1;4mERROR--${BASH_SOURCE[1]}-LINE: ${BASH_LINENO[0]} $* \033[0m "
}

function print_warning() {
  echo -e "\033[32;1;4mWARNING--${BASH_SOURCE[1]}-LINE: ${BASH_LINENO[0]} $* \033[0m "
}


function print_info() {
  echo -e "\033[32;1;4mINFO--${BASH_SOURCE[1]}-LINE: ${BASH_LINENO[0]} $* \033[0m "
}

function check_app_name() {  ${1:?"The argument must be specified"} 
}
function check_foundation() { : ${1:?"The argument must be specified"} 
}
function check_org() { : ${1:?"The argument must be specified"} 
}
function check_space() { : ${1:?"The argument must be specified"} 
}
function check_site() { : ${1:?"The argument must be specified"} 
}
#
function check_cf_config() { return 0; 
}


check_cf_config $site $foundation $org $space

