#!/usr/bin/env python
from getpass import getpass
from netmiko import ConnectHandler
from netmiko.ssh_exception import NetMikoTimeoutException
from paramiko.ssh_exception import SSHException
from netmiko.ssh_exception import AuthenticationException
import json
import re

# Enter creds

username = raw_input('Enter your SSH username: ')
password = getpass()


# Open device file

with open('./devices_file.txt') as f:
    devices_list = f.read().splitlines()




for devices in devices_list:
    #print ('Connecting to device ' + devices)
    ip_address_of_device = devices
    ios_device = {
        'device_type': 'cisco_ios',
        'ip': ip_address_of_device, 
        'username': username,
        'password': password
    }
 
    try:
        net_connect = ConnectHandler(**ios_device)
    except (AuthenticationException):
        print ('Authentication failure: ' + ip_address_of_device)
        continue
    except (NetMikoTimeoutException):
        print ('Timeout to device: ' + ip_address_of_device)
        continue
    except (EOFError):
        print ("End of file while attempting device " + ip_address_of_device)
        continue
    except (SSHException):
        print ('SSH Issue. Are you sure SSH is enabled? ' + ip_address_of_device)
        continue
    except Exception as unknown_error:
        print ('Some other error: ' + str(unknown_error))
        continue
 
    
  # Check
    for d in devices:
        print ('Check for license in ' + ip_address_of_device)
        output_version = net_connect.send_command('show bootflash')
        #print(output_version)
        regex = re.findall(r'JAE\S+.lic', output_version)
        
        def listTostr(regex):
            license  = ""
            for item in regex:
                license += item
            return license

        int_version = 0 # Reset integer value
        int_version = output_version.find('.lic') # Check for license
        if int_version > 0:
           # print ('License version found: ')
            #print regex
            nf = open('newfile.txt', 'a')
            nf.write(ip_address_of_device + ' ')
            nf.write(listTostr(regex) + ',\n')
            nf.close
            break
        else:
            #print ('Did not find a license.')
            nf = open('newfile.txt', 'a')
            nf.write(ip_address_of_device + ' does not have a license\n')
            nf.close
            break