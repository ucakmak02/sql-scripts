import pandas as pd
import MySQLdb
import csv

from config import cur

cursor = cur.cursor ()
cursor.execute('Select * from news_api where aoi="energy"')
data = cursor.fetchall()


with open("output.csv","w") as outfile:
    writer = csv.writer(outfile, quoting=csv.QUOTE_NONNUMERIC)
    writer.writerow(col[0] for col in data)
    for row in cursor:
        writer.writerow(row)


scp -r root@51.15.243.166:/root/output.csv /Users/ugurcakmak/hs/projects/excel-parsing