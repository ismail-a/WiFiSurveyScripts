#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
This script converts an XML output of 'airport -s -x' on macOS to a CSV with
four columns of BSSID, SSID, RSSI, CHANNEL.
Example:
% airport -s -x | ./AirportXML2CSV.py
"""

from lxml import etree
import sys

tree = etree.parse(sys.stdin)
root = tree.getroot()

dicts = tree.xpath('/plist/array/dict')
for dict in dicts:
	bssid = (dict.xpath('./key[text()="BSSID"]'))[0].getnext().text
	ssid = (dict.xpath('./key[text()="SSID_STR"]'))[0].getnext().text
	rssi = (dict.xpath('./key[text()="RSSI"]'))[0].getnext().text
	channel = (dict.xpath('./key[text()="CHANNEL"]'))[0].getnext().text
	print("{},{},{},{}".format(bssid, ssid, rssi, channel))
