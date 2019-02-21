
import pprint
# -*- coding: utf-8 -*-
#path = r'C:\Users\johnsonkev\Networking Code\Cisco Fun\4500\4500XOSPF.txt'
#OSPF_commands = open(path, 'r')

OSPF_commands = open(r'C:\Users\johnsonkev\Networking Code\Cisco Fun\4500\4500XOSPF.txt', 'r')

commands = OSPF_commands.readlines()

cmd_list=[]

for i in commands:
    lines = i.strip ('\n')
    #pprint (lines)
    cmd_list.append(lines)
    
#pprint (cmd_list)


def inter_cli():
   return_list = []    
   for i in (cmd_list):
       x = ('net_connect.send_command("' + str(i) + '")')
       return_list.append(x)
   return return_list


interface_cli=inter_cli()
#pprint(interface_cli)

f=open('crazycommands'+'.txt', 'w')
pprint.pprint(interface_cli, f)

