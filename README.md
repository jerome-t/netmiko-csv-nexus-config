# netmiko-csv-nexus-config
This is a very simple python script to configure multiple Cisco Nexus switches from a CSV file.

The script take the CVS file line by line; the first entry is the switch name, used to establish the SSH session.
And the next entries are the configuration variables.
Then, into the Python script, we use these variables with any commands you like.

Before doing any change, the script will show you the planned changes and ask you for a confirmation.
The script will also log all changes into log files, under /logs directory, including the date and time of the change.

This code can easily be customized and reused for another use-case, by modifying the configuration commands, that's why I share it.


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
Update the **lb-config.csv** file with the list of your network switches as first colonm, and the configuration variables(s) on the next colonms.

Then, update the **lb-config.py** file this way:
 - You can change the device-type, currently set for Cisco NXOS on the line: "device_type": "cisco_nxos",
Please refer to the Netmiko documentation here for more information: https://pynet.twb-tech.com/blog/automation/netmiko-scp.html

 - Under the **commands** part, you can set the configuration commands you need, using the variables of the CSV file.
   For example, the lines:

	```python   
	command1 = "ip address "+sw_lb0
	command2 = "ip address "+sw_lb1
	command3 = "ip address "+sw_lb1sec
	config_commands = ["interface loopback0", command1, "interface loopback1", command2, command3]
  	```
 
   Will configure, for the switch **switch-c**:

	``` 
	interface loopback0
	 ip address 172.17.138.153
	interface loopback1
	 ip address 172.17.138.213
	 ip address 172.17.138.248 secondary
	```

 - by changing the CSV values and the commands in the python script, the possibilities are almost endless. 


## Usage
When you execute the script, it will show you the configuration changes and ask you for a confirmation before doing the change.
Then, it will do the changes, and log all changes into log files, under /logs directory, including the date, time and the details of the change.
**Usage: lb-config.py**


## Getting help and Getting involved
Please contact me on [Twitter](https://twitter.com/JeromeTissieres) or open an Issue/P.R.


## Author(s)
This project was written and is maintained by the following individuals:
* Jerome Tissieres <jerome@tissieres.ch>

## Credits and references
All credits to Kirk Byers for making [Netmiko](https://github.com/ktbyers/netmiko)

