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



for i in range(1,csvFileCount):
  filePath = '../../../data/nyt'+str(i)+'.csv'
  getFile(filePath)
  # pd.read_csv


# load the data into the frame


