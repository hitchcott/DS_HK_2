# coding=utf8

import pandas as pd
from numpy import *
import os
import urllib2
import matplotlib.pyplot as plt
import csv

concatPath = '../../../data/nytConcat.csv'
csvFileCount = 31 # number of CSV files + 1

# if the data doesn't exist, download it -- should only happen first time this is run

def getFile(filePath):
  if not os.path.isfile(filePath):
    print localCopy, 'needs to be downloaded. Go grab a coffee, come back in', str(csvFileCount-i), 'minutes.'
    csvFile = urllib2.urlopen('http://stat.columbia.edu/~rachel/datasets/nyt'+str(i)+'.csv')
    output = open(localCopy,'wb')
    output.write(csvFile.read())
    output.close()


# concat the CSV files
if not os.path.isfile(concatPath):
  print 'Concat file doesnt exist, lets make it'
  for i in range(1,csvFileCount):
    filePath = '../../../data/nyt'+str(i)+'.csv'
    getFile(filePath)
    fout=open(concatPath,"a")
    f = open(filePath)

    # first file:
    if i is 1:
      for line in f:
        fout.write(line)

    else:
      # now the rest:
      f.next() # skip the header
      for line in f:
        fout.write(line)
      f.close() # not really needed

    fout.close()

# GO PANDAS!
df = pd.read_csv(concatPath)

dfg = df[ ['Age', 'Impressions', 'Clicks'] ].groupby(['Age']).agg([np.mean])



# x = linspace(-15,15,100) # 100 linearly spaced numbers
# y = sin(x)/x # computing the values of sin(x)/x

# # compose plot
# fig = plt.figure(figsize=(18, 8), dpi=300)
# plt.plot(x,y) # sin(x)/x
# plt.plot(x,y,'co') # same function with cyan dots
# plt.plot(x,2*y,x,3*y) # 2*sin(x)/x and 3*sin(x)/x
# plt.show() # show the plot
