#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
This script converts an XML output of './wifisnan.sh' on macOS to a CSV with
six columns of Point ID, Datetime, BSSID, SSID, RSSI, Channel.
Usage:
% ./AirportXML2CSV.py [file, ...]
"""

from lxml import etree
import sys

args = sys.argv
print("point_id,datetime,bssid,ssid,rssi,channel")

for file in args:
	if file[-4:] != ".xml":
		continue
	point_id = int(file[:4])
	dt = file[5:9] + "-" + file[9:11] + "-" + file[11:13] + " " + file[13:15] +\
		":" + file[15:17] + ":" + file[17:19]
	tree = etree.parse(file)
	root = tree.getroot()

	#print("point_id,dt,bssid,ssid,rssi,channel")

	dicts = tree.xpath('/plist/array/dict')
	for dict in dicts:
		bssid = (dict.xpath('./key[text()="BSSID"]'))[0].getnext().text
		ssid = (dict.xpath('./key[text()="SSID_STR"]'))[0].getnext().text
		rssi = (dict.xpath('./key[text()="RSSI"]'))[0].getnext().text
		channel = (dict.xpath('./key[text()="CHANNEL"]'))[0].getnext().text
		print("{},{},{},{},{},{}".format(point_id, dt, bssid, ssid, rssi, channel))
