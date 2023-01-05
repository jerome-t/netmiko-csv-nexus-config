#!/usr/local/bin/python3

import csv
import datetime
from getpass import getpass
from netmiko import ConnLogOnly


# --- Set the variables
sw_name = ()
sw_lb0 = ()
sw_lb1 = ()
sw_lb1sec = ()
command1 = ()
command2 = ()
command3 = ()
config_commands = []


# --- yes/no question
def confirm(prompt=None, resp=False):
    """prompts for yes or no response from the user. Returns True for yes and
    False for no.

    'resp' should be set to the default value assumed by the caller when
    user simply types ENTER.

    >>> confirm(prompt='Create Directory?', resp=True)
    Create Directory? [y]|n:
    True
    >>> confirm(prompt='Create Directory?', resp=False)
    Create Directory? [n]|y:
    False
    >>> confirm(prompt='Create Directory?', resp=False)
    Create Directory? [n]|y: y
    True

    """

    if prompt is None:
        prompt = 'Confirm'

    if resp:
        prompt = '%s [%s]|%s: ' % (prompt, 'y', 'n')
    else:
        prompt = '%s [%s]|%s: ' % (prompt, 'n', 'y')

    while True:
        ans = input(prompt)
        if not ans:
            return resp
        if ans not in ['y', 'Y', 'n', 'N']:
            print('please enter y or n.')
            continue
        if ans == 'y' or ans == 'Y':
            return True
        if ans == 'n' or ans == 'N':
            return False


# --- Ask the credentials
username = input('Please insert your Nexus username: ')
print("And your password")
password = getpass()


with open("./lb-config.csv", 'r') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=',')
    for row in csv_reader:
        sw_name = row[0]
        sw_lb0 = row[1]
        sw_lb1 = row[2]
        sw_lb1sec = row[3]

        print(40*"-")
        print("From CSV file:")
        print("Switch Name: ",sw_name)
        print("Loopback0: ", sw_lb0)
        print("Loopback1: ", sw_lb1)
        print("Loopback1-Secondary: ", sw_lb1sec)
        print(40*"-")

        # --- Set the config commands
        command1 = "ip address "+sw_lb0
        command2 = "ip address "+sw_lb1
        command3 = "ip address "+sw_lb1sec
        config_commands = ["interface loopback0", command1, "interface loopback1", command2, command3]
        
        # --- Show the switch and config commands:
        print("for switch:", sw_name)
        print(config_commands)
        print(40*"-")

        # --- Ask a confirmation before the config, if not, we skip this switch
        prompt = str("Please confirm configuration change for switch: "+sw_name)
        if confirm(prompt=prompt, resp=False) == True:

            # --- Prepare the log file
            now = datetime.datetime.now()
            LOGFILE = "./logs/"+str(now.strftime("%Y%m%d-%H-%M_"))+str(sw_name)+".txt"

            # --- Make the change
            device = {
                "device_type": "cisco_nxos",
                "host": sw_name,
                "username": username,
                "password": password,
                "log_file": LOGFILE,
                "fast_cli" : True,
                "verbose": False,
            }

            net_connect = ConnLogOnly(**device)

            if net_connect is None:
                print(sw_name+ ": Logging in failed... skipping")
                print(40*"-")

            else:
                print(net_connect.find_prompt())
                output = net_connect.send_config_set(config_commands)
                print(output)
                print()
                net_connect.save_config()
                print("Changes done, logged and config saved")
                print(40*"-")
                net_connect.disconnect()

# --- All done
print(40*"=")
print("All changes are done")
print(40*"=")
raise SystemExit
