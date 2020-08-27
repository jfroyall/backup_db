#!/bin/bash

set -e

##############################################################
#utility script to push example apps onto a set of foundations

app_dir=./app_dir
test -d $app_dir || mkdir $app_dir

function build_manifest() {

    local app_name=$1
    local   domain=$2
    local      org=$3
    local    space=$4

    local route=`printf "%s.%s.apps.mycf.lan" $space $org`
    route=${route//_/-}


    echo "route: $route"
    cf create-domain  $org $route  
    cf create-route $space $route  --hostname $app_name

    echo "Hello World from $app_name" > $app_dir/index.html

    cat <<EOF > $app_dir/manifest.yml
applications:
- name: $app_name
  buildpacks:
  - staticfile_buildpack
  memory: 32M
  routes:
  - route: $app_name.$route
EOF

    echo cf

}



#++++++++++++++++ #++++++++++++++++ #++++++++++++++++

site=eu

SERVER=192.168.5.13
SECRETS_REPO=./mcp-secrets

#SERVER=$CREDHUB_SERVER
#SECRETS_REPO=/home/ubuntu/mcp-secrets

hold=
DASH=

domain="apps.mycf.lan"

# set the CredHub API
#credhub api --ca-cert=<(bosh int $SECRETS_REPO/concourse/ops/creds.yml --path /credhub-ca/ca) --server=$SERVER:8844
credhub api 

# get a CredHub token
#credhub login --client-name=concourse_to_credhub --client-secret=`bosh int $SECRETS_REPO/concourse/ops/creds.yml --path /concourse_to_credhub_secret`
credhub login 

for f in 0; do

    foundation=f$f
    credhub set -t value \
            -n /concourse/${site}${DASH}${hold}-${foundation}/opsman_admin_password \
            -v ops_man_pw

    #set the opsman password


    for o in {0..0}; do

        org=org$o
        cf create-org $org
        cf target -o $org
        for s in {0..0}; do

            space=space$s
            cf create-space $space
            cf target -s $space
            for a in {0..2}; do

                app=app$a
                echo pushing $app into $space of $org onto foundation $foundation
                #app_name=`printf "%s%s%s%s" $app $space $org $foundation`
                app_name=`printf "%s" $app` 
                app_name=${app_name//_/-}
                build_manifest $app_name $domain $org $space
                
                cf push -f $app_dir/manifest.yml -p $app_dir



            done


        done

    done
done

