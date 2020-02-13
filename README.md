# WiFi Survey Scripts

These scripts support save Wi-Fi scan results on each point by only input the point number.

When you input this command on your Mac,
```sh
$ ./wifiscan.sh 0001
```
It saves XML file like 0001-20200201082015.xml

You can convert this XML to a CSV with four columns of BSSID, SSID, RSSI, and CHANNEL.
```sh
$ ./AirportXML2CSV.py < 0001-20200201082015.xml > 0001-20200201082015.csv
```
