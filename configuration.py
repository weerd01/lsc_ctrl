#!/usr/bin/env python3

import sys
import yaml

groups = []
groups_unique = []

with open(r'devices.yaml') as file: 
  devices = yaml.load(file, Loader=yaml.FullLoader)

def get_groups():
  
  for _ in devices:
    for device_name, parameter in _.items():
      groups.append(parameter['group'])

  for _ in groups:
    if _ not in groups_unique:
      groups_unique.append(_)

  return groups_unique

def get_group_ipaddr(group):

  ip_addrs = []

  for _ in devices:
    for device_name, parameter in _.items():
      if (parameter['group']) == group:
        ip_addrs.append(parameter['ip'])

  return ip_addrs


#print(devices[0]['lamp_1']['ip'])
