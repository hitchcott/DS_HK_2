#!/usr/bin/python
# Import required libs
import sys

# sart a counter and store the file in memory

impressions = 0
lines = sys.stdin.readlines()
lines.pop(0)

# find the sum of index 2 in the list

oldest = 0
clicks = 0
ages = 0

for line in lines:
  split_line = line.strip().split(',')
  if int(split_line[0]) > oldest:
    oldest = int(split_line[0])
  impressions = impressions + int(split_line[2])
  clicks = clicks + int(split_line[3])
  ages = ages + int(split_line[0])

average_age = ages / len(lines)

click_through_rate = float(clicks) / float(impressions)

print 'Clicks', clicks
print 'Impressions', impressions
print 'Average Ages', average_age
print 'Oldest', oldest
print 'Click thorugh', click_through_rate

file = open("newfile.txt", "w")

file.write("\nclicks %s" % clicks)
file.write("\nimpressions %s" % impressions)
file.write("\naverage_age %s" % average_age)
file.write("\noldest %s" % oldest)
file.write("\nclick_through_rate %s" % click_through_rate)

file.close()
