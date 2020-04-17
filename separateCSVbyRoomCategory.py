#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
This script separates JMU's CSV to 4 categories of Room, Operation-room, Hallway, and all.
It also convert point_ids of JMU to loc_ids of VT.
Usage:
% ./separateCSVbyRoomCategory.py JMUCSV.csv point_loc.csv
Output:
./JMUCSV-hallways-separated.csv
./JMUCSV-operations-separated.csv
./JMUCSV-rooms-separated.csv
./JMUCSV-all.csv
"""

import sys
import csv

args = sys.argv

point_loc_file = open(args[2], "r")
point_loc_reader = csv.DictReader(point_loc_file)
point_loc_dict = {}
for row in point_loc_reader:
    point_loc_dict[row['point_id']] = row['loc_id']
point_loc_file.close()

csv_file = open(args[1], "r")
csv_file_reader = csv.reader(csv_file)
header = next(csv_file_reader)
header[0] = 'loc_id'
csv_hallways_file = open(args[1][:-4] + "-hallways-separated.csv", "w")
csv_hallways_writer = csv.writer(csv_hallways_file)
csv_hallways_writer.writerow(header)
csv_operations_file = open(args[1][:-4] + "-operations-separated.csv", "w")
csv_operations_writer = csv.writer(csv_operations_file)
csv_operations_writer.writerow(header)
csv_rooms_file = open(args[1][:-4] + "-rooms-separated.csv", "w")
csv_rooms_writer = csv.writer(csv_rooms_file)
csv_rooms_writer.writerow(header)
csv_all_file = open(args[1][:-4] + "-all.csv", "w")
csv_all_writer = csv.writer(csv_all_file)
csv_all_writer.writerow(header)

for row in csv_file_reader:
    row[0] = point_loc_dict[row[0]]
    category = int(row[0]) // 100
    if category == 1:
        csv_hallways_writer.writerow(row)
    elif category == 2:
        csv_rooms_writer.writerow(row)
    elif category == 3:
        csv_operations_writer.writerow(row)
    csv_all_writer.writerow(row)

csv_file.close()
csv_hallways_file.close()
csv_operations_file.close()
csv_rooms_file.close()
csv_all_file.close()
