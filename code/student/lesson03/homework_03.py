# coding=utf8

import pandas as pd
import numpy as np
import os
import urllib2

csvFileCount = 31 # number of CSV files + 1

# if the data doesn't exist, download it -- should only happen first time this is run

def getFile(filePath):
  if not os.path.isfile(filePath):
    print localCopy, 'needs to be downloaded. Go grab a coffee, come back in', str(csvFileCount-i), 'minutes.'
    csvFile = urllib2.urlopen('http://stat.columbia.edu/~rachel/datasets/nyt'+str(i)+'.csv')
    output = open(localCopy,'wb')
    output.write(csvFile.read())
    output.close()

frame = pd.DataFrame()
# for year in years:
#     path ='C:\\Documents and Settings\\Foo\\My Documents\\pydata-book\\pydata-book-master`\\ch02\\names\\yob%d.txt' % year
#     frame = pd.read_csv(path, names=columns)

#     frame['year'] = year
#     names = names.append(frame, ignore_index=True)

for i in range(1,csvFileCount):
  filePath = '../../../data/nyt'+str(i)+'.csv'
  print 'reading', filePath

  thisFrame = pd.read_csv(filePath)

  frame = frame.append(thisFrame, ignore_index=True)
  # pd.read_csv

print frame.describe()

# load the data into the frame


