#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
merge AP lists CSV (Point id, Datetime, BSSID, SSID, RSSI, Channel) and
Coordinates CSV (Point id, X, Y, Direction) assuming Point id as a key columnn.
Usage: ./mergeCSV.py aps.csv coordinates.csv > wifi_survey.csv
"""

import sys
import csv

args = sys.argv

coordinates_file = open(args[2], "r")
coordinates_csv = csv.DictReader(coordinates_file, delimiter = ",")
coordinates = {}
for coordinate in coordinates_csv:
    coordinates[coordinate['point_id']] = {'x': coordinate['x'],
    'y': coordinate['y'], 'direction': coordinate['direction']}

aps_file = open(args[1], "r")
aps_csv = csv.DictReader(aps_file, delimiter = ",")
print("point_id,datetime,x,y,direction,bssid,ssid,rssi,channel")
for ap in aps_csv:
    print('{},"{}",{},{},{},{},"{}",{},{}'.format(ap['point_id'], ap['datetime'],
    coordinates[ap['point_id']]['x'], coordinates[ap['point_id']]['y'],
    coordinates[ap['point_id']]['direction'], ap['bssid'], ap['ssid'], ap['rssi'],
    ap['channel']))
