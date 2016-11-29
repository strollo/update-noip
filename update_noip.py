#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import urllib2
import random
import syslog
import ConfigParser

# Adding syslog support.
# I want to make sure that when the crontab runs it really execute
# the update of the IP at noip.com.
log = syslog.syslog

def main():
	config = ConfigParser.ConfigParser()		
	config.read('etc/noip.ini')
	
	IPS_BAG=eval(config.get('Default', 'ips'), {}, {})
	HOSTNAME=config.get('Default', 'host')
	USERNAME=config.get('Default', 'usr')
	PASSWORD=config.get('Default', 'pwd')
	
	_old_ = IPS_BAG[random.randrange(0, len(IPS_BAG) - 1)]
	_new_ = urllib2.urlopen("http://api.enlightns.com/tools/whatismyip/?format=text").read().strip()
	_url_ = "https://dynupdate.no-ip.com/nic/update?hostname={hostname}&myip={ip}"

	log('... Update www.noip.com account ...')
	log('... OLD IP: {ip}'.format(ip=_old_))
	log('... NEW IP: {ip}'.format(ip=_new_))

	# Update no-ip with the fake old ip
	_url_called_ = _url_.format(hostname=HOSTNAME, ip=_old_)

	r = requests.get(_url_called_, auth=(USERNAME, PASSWORD))
	print r.status_code  # if 200 this means the page was reached
	print r.content  # should be the response from noip.com
	
	# Update current public ip
	_url_called_ = _url_.format(hostname=HOSTNAME, ip=_new_)
	r = requests.get(_url_called_, auth=(USERNAME, PASSWORD))
	print r.status_code  # if 200 this means the page was reached
	print r.content  # should be the response from noip.com

	if r.status_code == 200:
		success = 'yes'
	else:
		success = 'no'

	log('... Succeed: {success}'.format(success=success))
	# Successfully forced a change of your domain ip

if __name__ == '__main__':
	main()
	