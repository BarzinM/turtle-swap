# test code

import csv
import StringIO



with open('City_Zhvi_Summary_AllHomes.csv','rb') as csvfile:
    reader = csv.DictReader(csvfile)
    header = reader.next()
    print header
    # for row in reader:
	   #  print(row['Date'])