#!/bin/bash

# Save Wi-Fi scan XML file named like ARGUMENT-yyyymmddHHMMSS.xml
# Example:
# % ./wifiscan.sh 0001

/System/Library/PrivateFrameworks/Apple80211.framework/Versions/Current/Resources/airport -s -x > $1-`date "+%Y%m%d%H%M%S"`.xml
