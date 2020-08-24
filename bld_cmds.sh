#!/bin/bash

set -x

ECHO=echo

. ./utils.sh

function usage {
  echo -e "\nusage: $0"
  exit 1
}


print_warning "Restore getopts"


#Check that the cf CLI is properly configured
check_cf_config $site $foundation $org $space

# Source the cf utils
. ./cf_utils.sh


#set source region and foundation
readonly src_region=eu
readonly src_foundation=atlas

if ! check_site $src_region; then error_exit "Invalid source site: $src_region"; fi
if ! check_foundation $src_foundation; then error_exit "Invalid source foundation: $src_foundation"; fi


#set destination region and foundation
readonly dest_region=eu
readonly dest_foundation=atlas

if ! check_site $dest_region; then error_exit "Invalid source site: $dest_region"; fi
if ! check_foundation $dest_foundation; then error_exit "Invalid source foundation: $dest_foundation"; fi


declare -A db_names;

db_names=(
        [skyhook]="-db"
        [jigsaw]="jigsaw-mysql"
        [echo-base]="rebel-alliance-mysql-event-store"
        )

# source orgs
declare -A src_orgs;
src_orgs=(
        [skyhook]="skyhook"
        [jigsaw]="jigsaw"
        [echo-base]="rebel-alliance"
        )


# source spaces
declare -A src_spaces;
src_spaces=(
        [skyhook]="eu"
        [jigsaw]="eu"
        [echo-base]="eu"
        )


# source orgs
declare -A dest_orgs;
dest_orgs=(
        [skyhook]="skyhook"
        [jigsaw]="jigsaw"
        [echo-base]="rebel-alliance"
        )


# source spaces
declare -A dest_spaces;
dest_spaces=(
        [skyhook]="eu"
        [jigsaw]="eu"
        [echo-base]="eu"
        )
#build get commands
function build_src_cmds {

  local app=${1:?"The app must be provided"}
  local site=${2:?"The site must be provided"}
  local foundation=${3:?"The foundation must be provided"}
  local org=${4:?"The org must be provided"}
  local space=${5:?"The space must be provided"}


  print_info "Working on: $site/$foundation/$org/$space"

  local cmd_file_name="pull_$app.sh"
  cat /dev/null > $cmd_file_name
  chmod a-x  $cmd_file_name

  local db_name=${db_names[$app]}

  print_info "Checking the config"
  if ! check_cf_config $site $foundation $org $space; then
    print_error "Invalid cf configuration"
    return 1
  fi

  print_info "Extracting the information"
  if ! curl_work $org $db_name; then
    print_error "The curl extractions failed."
    return 1
  fi

  print_warning "remove this code"
  omg $site $foundation
  print_warning "remove this code"


  local stored_db=/tmp/$db_name.sql
  local storage_dir="~/${site}-db-backups"


  cat <<EOF >$cmd_file_name

#This file was automatically generated by $0.
#It is designed as a collection of command hints.
#The commands will dump the '$ap' database named $db_name, 
#and then move it from the VM at FOOBAR to the current working directory.
#
#Caveats:
#  o  These steps only apply to MySQL databases.
#  o  We assume that a 'bosh alias' has been run on the opsman machine.
#  o  The original instructions called for the stopping of the application.
#        This step is skipped for MySQL databases.


#create a storage directory on the MCP jumpbox
test -d $storage_dir || mkdir -p $storage_dir

#ssh into opsman of foundation; for example, "opsman.atlas.pac.kesselrun.smil.mil"
#>>>> PW: ${passwords[opsman_ssh]}
ssh ubuntu@opsman.$foundation.$site.kesselrun.smil.mil

#log onto the director (i.e. acquire a token from uaa:  bosh -e director login)
#>>>> USER: ${username[bosh]}
#>>>> PW: ${passwords[bosh]}
bosh -e director login


#ssh onto the instance
bosh -e director -d service-instance_${db_guid} ssh

#elevate priority
sudo -i


>>>>>>>>>> ???  change user to vcap????<<<<<<<<<<<<<

# dump the database
# >>> Check the alias.  If not valid, then you're on your own
#>>>> PW: ${passwords[bosh]}
alias msd=\`find /var/vcap/data/packages -name mysqldump\`
msd --single-transaction --set-gtid-purged=OFF --databases service_instance_db --user=$db_username -p> $stored_db


# Restore the vcap user on the instance
exit

# Leave the instance and return to the opsman 
exit

# copy the dump from the instance to the opsman machine
bosh -e director -d service-instance_${db_guid} scp mysql/0:$stored_db $stored_db

# copy the dump from the opsman machine to the jumpbox machine
scp $stored_db ubuntu@mcp-jumpbox.kesselrun.smil.mil:$storage_dir/$db_name.sql

EOF

  print_info "all done"
  return 0
}





function build_push_cmds {
}