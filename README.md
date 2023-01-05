# netmiko-csv-nexus-config
This is a very simple python script to configure multiple Cisco Nexus switches from a CSV file.

The script take the CVS file line by line; the first entry is the switch name, used to establish the SSH session. And the next entries are the configuration part, who can be changed.


## Use Case Description
In the current state of the script, I was configuring loopback interfaces for a bunch of Cisco Nexus VXLAN leafs.
I needed to configure two loopbacks per leaf: The first loopback with a single IP, and the second with a single IP per switch plus a common secondary IP per pair of vPC leafs.


## Installation

Requirements: All you need is Python and pip.
Then, with pip we will install Netmiko and dependencies.

Installation:

	$ git clone https://github.com/jerome-t/netmiko-csv-nexus-config
	$ sudo pip install -r requirements.txt


## Configuration

Update the **lb-config.csv** file with the list of your network switches (first colonm), and the configuration changes (next colonms).


## Usage

When you execute the script, it will show you the configuration changes and ask you for a confirmation before doing the change.

**Usage: lb-config.py**

This code can be customized and re-used for anything else by changing the configuration commands, this is why I share it.


## Getting help and Getting involved

Please contact me on [Twitter](https://twitter.com/JeromeTissieres) or open an Issue/P.R.


## Author(s)

This project was written and is maintained by the following individuals:

* Jerome Tissieres <jerome@tissieres.ch>
