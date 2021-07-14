#!/bin/bash

/usr/local/foglamp/bin/foglamp kill
sudo apt -y remove 'foglamp*'
sudo rm -rf /usr/local/foglamp
wget -q -O - http://archives.dianomic.com/KEY.gpg| sudo apt-key add -
sudo rm /etc/apt/sources.list.d/foglamp.list
echo "deb [arch=armv7l] http://archives.dianomic.com/foglamp/1.9.0/buster/armv7l/ ./" | sudo tee -a /etc/apt/sources.list.d/foglamp.list
sudo apt -y update
sudo DEBIAN_FRONTEND=noninteractive apt-get -y install foglamp
sudo apt-get -y install foglamp-gui
sudo apt-get -y install foglamp-south-sensehat foglamp-south-sinusoid foglamp-south-randomwalk foglamp-filter-delta foglamp-filter-change foglamp-filter-expression foglamp-filter-rms foglamp-filter-fft foglamp-filter-metadata foglamp-filter-python35 foglamp-rule-simple-expression foglamp-notify-asset foglamp-notify-python35
