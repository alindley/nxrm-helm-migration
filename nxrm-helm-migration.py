#!/usr/bin/env python3
import requests
import json
import urllib.request
import os
import sys

download_dir = './helm-packages/'
download_url = ''
source_nxrm = 'http://localhost:9081'
source_repo = 'helm-hosted'
source_auth = ('admin', 'admin123')
target_nxrm = 'http://localhost:9081'
target_repo = 'helm-hosted-new'
target_auth = ('admin', 'admin123')


if not os.path.exists(download_dir):
	print("Creating directory:", target_dir)
	os.makedirs(download_dir)

print("Requesting a list of components from the repository", source_repo)
try:
	params = {'repository': source_repo}
	list_response = requests.get(f'{source_nxrm}/service/rest/v1/components', params=params, auth=source_auth, verify=False)
	list_response.raise_for_status()
except requests.exceptions.RequestException as err:
	print(err, err.response.text)
	sys.exit()

for item in list_response.json()['items']:
	download_url = item['assets'][0]['downloadUrl']
	filename = item['assets'][0]['path']
	print("Downloading ", download_url)
	urllib.request.urlretrieve(download_url, download_dir+filename)
	print("Uploading ", download_dir+filename, "->", target_nxrm)
	params = {'repository': target_repo}
	files = {'helm.asset': open(download_dir+filename, 'rb')}
	try:
		upload_response = requests.post(f'{target_nxrm}/service/rest/v1/components', params=params, files=files, auth=target_auth, verify=False)
		upload_response.raise_for_status()
	except requests.exceptions.HTTPError as err:
		print(err)

print("Transfer Complete")
