#!/usr/bin/python

#Name          : DemonLayer IP Lookup
#Writer(s)     : Abay | @demon.layer On IG
#Description   : DemonLayer is a simple IP Tracker using Python.

import os
import urllib2
import json
import colorama
colorama.init(autoreset=True)

os.system("clear");
print colorama.Fore.CYAN + """
    ____                             __                         
   / __ \___  ____ ___  ____  ____  / /   ____ ___  _____  _____
  / / / / _ \/ __ `__ \/ __ \/ __ \/ /   / __ `/ / / / _ \/ ___/
 / /_/ /  __/ / / / / / /_/ / / / / /___/ /_/ / /_/ /  __/ /    
/_____/\___/_/ /_/ /_/\____/_/ /_/_____/\__,_/\__, /\___/_/     
                                             /____/                                                       
  DemonLayer IP Lookup - DemonLayer | @demon.layer On IG
"""
print "\r"
while True:
		ip = raw_input("What Your Target IP : ")
		url = "https://api.ipdata.co/"
		response = urllib2.urlopen(url + ip)
		data = response.read()
		values = json.loads(data)

		print("------------------------------------")
		print "\r"
		print(" IP           :  " + values['ip'])
		print(" City         :  " + values['city'])
		print(" Region       :  " + values['region'])
		print(" Country      :  " + values['country_name'])
		print(" Continent    :  " + values['continent_name'])
		print(" Time Zone    :  " + values['time_zone'])
		print(" Currency     :  " + values['currency'])
		print(" Calling Code :  " + "+" + values['calling_code'])
		print(" Organisation :  " + values['organisation'])
		print(" ASN          :  " + values['asn'])
		print "\r"
		break
