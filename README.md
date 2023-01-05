# netmiko-csv-nexus-config
This is a very simple python script to configure multiple Cisco Nexus switches from a CSV file.

The script takes the CVS file line by line; the first entry is the switch name, used to establish the SSH session.
And the next entries are the configuration variables.
Then, in the Python script, we use these variables with any commands you like.

Before doing any changes, the script will show you the planned changes and ask you for confirmation.
The script will also log all changes into log files, under the /logs directory, including the date and time of the change.

This code can easily be customized and reused for another use case, by modifying the configuration commands, that's why I share it.


## Use Case Description
In the current state of the script, I was configuring loopback interfaces for a bunch of Cisco Nexus VXLAN leafs.
I needed to configure two loopbacks per leaf: The first loopback with a single IP, and the second with a single IP per switch plus a common secondary IP per pair of vPC leafs.


## Installation
Requirements: All you need is Python and pip.
Then, pip will install Netmiko and dependencies.

Installation:
```
	$ git clone https://github.com/jerome-t/netmiko-csv-nexus-config
	$ sudo pip install -r requirements.txt
```

## Configuration
Update the **lb-config.csv** file with the list of your network switches as first colunm, and the configuration variables(s) in the next colunms.

Then, update the **lb-config.py** file this way:
 - You can change the device type, currently set for Cisco NXOS on the line: "device_type": "cisco_nxos",
Please refer to the Netmiko documentation here for more information: https://pynet.twb-tech.com/blog/automation/netmiko-scp.html

 - Under the **commands** part, you can set the configuration commands you need, using the variables of the CSV file.

   For example, the lines:

	```python   
	command1 = "ip address "+sw_lb0
	command2 = "ip address "+sw_lb1
	command3 = "ip address "+sw_lb1sec
	config_commands = ["interface loopback0", command1, "interface loopback1", command2, command3]
  	```
 
   Will configure, for the switch **switch-c** this way:

	``` 
	interface loopback0
	 ip address 172.17.138.153
	interface loopback1
	 ip address 172.17.138.213
	 ip address 172.17.138.248 secondary
	```

 - By changing the CSV values and the commands in the python script, the possibilities are almost endless. 


## Usage
1) Install Python.
2) Clone this repository and install Netmiko and the required modules.

	```
	$ git clone https://github.com/jerome-t/netmiko-scp-multi-thread-upload
	$ sudo pip install -r requirements.txt
	```
3) Update the **lb-config.csv** file with the switch names on the first column, and the variables on the next columns.
4) Update the **lb-config.py** file with the configuration commands you need.
5) Run the script, it will ask you username and password to login into your device(s), and confirmation for each config changes:

```
$ ./lb-config.py
Please insert your Nexus username: admin
And your password
Password:
----------------------------------------
From CSV file:
Switch Name:  switch-c
Loopback0:  172.17.153/32
Loopback1:  172.17.138.213/32
Loopback1-Secondary:  172.17.138.248/32 secondary
----------------------------------------
for switch: switch-c
['interface loopback0', 'ip address 172.17.138.153/32', 'interface loopback1', 'ip address 172.17.138.213/32', 'ip address 172.17.138.248/32 secondary']
----------------------------------------
Please confirm configuration change for switch: switch-c [n]|y: y
switch-c#
 configure terminal
Enter configuration commands, one per line. End with CNTL/Z.

switch-c(config)#  interface loopback0

switch-c(config-if)# ip address 172.17.138.153/32

switch-c(config-if)# interface loopback1

switch-c(config-if)# ip address 172.17.138.213/32

switch-c(config-if)# ip address 172.17.138.248/32 secondary

switch-c(config-if)#  end

switch-c#

Changes done, logged and config saved
----------------------------------------
----------------------------------------
From CSV file:
Switch Name:  switch-d
Loopback0:  172.17.138.154/32
Loopback1:  172.17.138.214/32
Loopback1-Secondary:  172.17.138.248/32 secondary
----------------------------------------
for switch: n9300d
['interface loopback0', 'ip address 172.17.138.154/32', 'interface loopback1', 'ip address 172.17.138.214/32', 'ip address 172.17.138.248/32 secondary']
----------------------------------------
Please confirm configuration change for switch: switch-d [n]|y:
(... skipped ...)
========================================
All changes are done
========================================
```


## Getting help and Getting Involved
Please contact me on [Twitter](https://twitter.com/JeromeTissieres) or open an Issue/P.R.


## Author(s)
This project was written and is maintained by the following individuals:
* Jerome Tissieres <jerome@tissieres.ch>

## Credits and References
All credit to Kirk Byers for making [Netmiko](https://github.com/ktbyers/netmiko)

