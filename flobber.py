#!/usr/bin/env python3

# # https://docs.python.org/3/library/argparse.html
import argparse
# https://cloudpathlib.drivendata.org/
from cloudpathlib import CloudPath

parser = argparse.ArgumentParser(
                    prog='flobber',
                    description='Upload a file to a Blob Storage',
                    epilog='https://github.com/cbwham/training-flobber') # TODO
parser.add_argument('--filename', '-f', default='root/index.html')
parser.add_argument('--uri', '-u', default='az://cbwtrainingbackup/') 
args = parser.parse_args()

# # DEBUG
# print(repr(args))

# copy
filename = args.filename
cloud_uri = args.uri

# open local file by name in the argument passed on the cli
local_file = open(filename, 'rb')
print(f'local file: {filename}')
# actually read file
local_text = local_file.read()

# connect to cloud endpoint
root_dir = CloudPath(cloud_uri)
print(f'cloud root directory: {root_dir}')

# use / to join paths (and, in this case, create a new file)
cloud_file = root_dir / filename
# check if file does exist
if(cloud_file.exists()):
    print(f'cloud file: {cloud_file} exists')
    # get content of cloud file
    cloud_text = cloud_file.read_bytes()
    # compare local and cloud text
    if(local_text == cloud_text):
        print(f'local file: {filename} is identical to {cloud_file}')
    else:
        print(f'updating: {cloud_file}')

# TODO: stupid logic, give this another try later
print(f'writing: {cloud_file}')
cloud_file.write_bytes(local_text)

# # DEBUG: list all markdown files in container
# print(list(root_dir.glob('**/*.md')))
