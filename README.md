# WiFi Survey Scripts

These scripts support save Wi-Fi scan results on each point by only input the point number.

When you input this command on your Mac,
```sh
$ ./wifiscan.sh 0001
```
It saves a XML file like 0001-20200201082015.xml

You can convert this/these XML file(s) to a CSV with six columns of Point id, Datetime, BSSID, SSID, RSSI, and Channel.
```sh
$ ./AirportXML2CSV.py [xmlfile ...] > aps.csv
```

If you have coordinates CSV (Point id, X, Y, Direction (Up, Down, Right, Left)) of each Point id, you can merge them by using mergeCSV.py.
```sh
$ ./mergeCSV.py aps.csv coordinates.CSV
```
