#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
This script converts an JMU's CSV to a VT's CSV.
Usage:
% ./JMU2VT.py JMUCSV.csv > VTCSV.csv
"""

import sys
import csv

def channel2freq(channel):
    if 1 <= channel <= 13:
        return 2407 + channel * 5
    elif channel == 14:
        return 2484
    elif 36 <= channel <= 165:
        return 5000 + channel * 5
    else:
        return 0

args = sys.argv
wifi_file = open(args[1], "r")
wifi_csv = csv.DictReader(wifi_file, delimiter = ",")

aps = {}
index = 0
for beacon in wifi_csv:
    if beacon['bssid'] in aps:
        continue
    aps[beacon['bssid']] = {'channel': beacon['channel'], 'ssid': beacon['ssid'], 'index': index}
    index += 1

headers = ["Channel,", "SSID,", "time,"]

for key in aps:
    headers[0] += str(channel2freq(int(aps[key]['channel']))) + ","
    headers[1] += aps[key]['ssid'] + ","
    headers[2] += key + ","
headers[2] += "loc"

for header in headers:
    print(header)

wifi_file.seek(0)
wifi_csv = csv.DictReader(wifi_file, delimiter = ",")
for beacon in wifi_csv:
    line = beacon['datetime'] + ","
    for i in range(aps[beacon['bssid']]['index']):
        line += "0,"
    line += beacon['rssi'] + ","
    for i in range(len(aps) - aps[beacon['bssid']]['index'] - 1):
        line += "0,"
    line += beacon['loc_id']
    print(line)
