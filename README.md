# netmiko-csv-nexus-config
This is a very simple python script to configure multiple Cisco Nexus switches from a CSV file.

In this case, I was configuring loopback interfaces for a bunch of VXLAN leafs, 
so two loopbacks per leaf. The first loopback with a single IP, and the second with a single IP per switch plus a common secondary IP per pair of vPC leafs.

This code can be customized and re-used for anything else by changing the configuration commands, this is why I share it.

Enjoy!
Jerome Tissieres

