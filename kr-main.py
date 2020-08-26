##\file Main KR file

import sys
import os
import yaml
import json
import argparse
import subprocess

from utils import (print_info, print_warning, print_error)
import Bosh
from CredHub import CredHub




#if __name__ == "__main__":

print_info("Hello World!")

credHub=CredHub();
bosh=Bosh.Bosh('test_data/bosh-creds.yml');

print_info("Create a CredHub instance")
print_info("Create a Bosh instance")
print_info("Create a CloudFoundry instance")

print_info("Goodbye World!")


