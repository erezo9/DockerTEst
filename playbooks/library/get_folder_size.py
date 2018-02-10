#!/usr/bin/python

DOCUMENTATION = '''
---
module: get_folder_size
short_description: retrieve folder size
description:
     - Retrieves Size for a given folder.
options:
  path:
    description:
      - The full path of the folder
    required: true
    default: null
    aliases: []
  outputType:
    description:
      - output required (GB,MB,KB,B)
    required: false
    default: GB
    aliases: []
author: "Erez Tamam (@bpennypacker)"
'''
# uses ansible stat
from stat import *
import os
import sys

Sizes = {'GB': 'G',
	 'MB': 'M',
	 'KB': 'K',
	 'B' : '1',}

# Checks if the input given exists, and valids as a directory
def checkDirectory(module, path):
	try:
                 folder = os.lstat(path)
        except OSError, e:
                if e.errno == errno.ENOENT:
			module.fail_json(msg = e.strerror)
	isdir = S_ISDIR(folder.st_mode)
        if isdir == False:
                module.fail_json(msg="Expected a directory")

# Main module Code
def main():
	module = AnsibleModule(
        argument_spec = dict(
            path = dict(required=True),
            outputType = dict(required=False, default="GB", choices= ['GB','MB','KB','B']),
	),
	supports_check_mode = False,
	)
	# Get params from ansible
	path = module.params.get('path')
	outputType = module.params.get('outputType')

	# Check if valid
	checkDirectory(module, path)
	
	#Create the command line and run it
	args = "du -sB" + Sizes[outputType] + " " + path + " | cut -f1"
	response = module.run_command(args,use_unsafe_shell=True)
	#take the response and get the size only
	response = str(response[1]).rstrip()[:-1] + outputType
	# exit the module
	module.exit_json(changed=False,size=response);

# Import module snippets
from ansible.module_utils.basic import *
from ansible.module_utils.urls import *
if __name__ == '__main__':
    main()
