# coding=utf-8

# 1. Clean up a the source
# 2. Make a unique key string for each aggregation based on the requirements - age,gender,impressions
# 3. Reduce each line of the csv into that dictionary
# 4. Run through the aggregation dictionary again to calcualte averages
# 5. Output results to a new csv file

# Required aggregation:
# "age", "gender", "signed_in", "avg_click", "avg_impressions", "max_click", "max_impressions"

# Given headers:
# "Age","Gender","Impressions","Clicks","Signed_In"

# open file
inputPath = '../../../data/nytimes.csv'
outputPath = '../../../data/nytimes_agg.csv'

# Create index dictionary of given headers for maintainability (eg: the source file indexes change)
# This is not totally necessary, but keep things DRY
headers = {
  'age':0,
  'gender':1,
  'impressions':2,
  'clicks':3,
  'signed_in':4
}

# Set up empty dictionary for the aggregation
agg = {}

# Step 1.

# Parse the input csv file
lines = open(inputPath).readlines()
lines.pop(0)

for line in lines:
   # sanitize the list
  split_line = line.strip().split(',')

  # Step 2.

  # create an agg key using the format 'age,gender,impressions'
  key = ','.join(split_line[0:3])
  # convert the line to integers for math later on
  split_line = [int(i) for i in split_line]

  if key not in agg:
    # if the key doesn't exists, populate the agg it with the first result (metadata)
    agg[key] = {
      'age':split_line[headers['age']],
      'gender':split_line[headers['gender']],
      'signed_in':split_line[headers['signed_in']],
      'clicks':{
        'combined':split_line[headers['clicks']],
        'max':split_line[headers['clicks']]
      },
      'impressions':{
        'combined':split_line[headers['impressions']],
        'max':split_line[headers['impressions']]
      },
      'count': 1
    }
  else:

    # Step 3.

    # otherwise, do some bean counting with the existing entry
    agg[key]['count'] += 1
    agg[key]['clicks']['combined'] += split_line[headers['clicks']]
    agg[key]['impressions']['combined'] += split_line[headers['impressions']]

    if split_line[headers['clicks']] > agg[key]['clicks']['max']:
      agg[key]['clicks']['max'] = split_line[headers['clicks']]

    if split_line[headers['impressions']] > agg[key]['impressions']['max']:
      agg[key]['impressions']['max'] = split_line[headers['impressions']]

# Step 4.

# I could have done the averaging stage each time I iterated over a line
# But it would have been needlessly inefficient as only one calculation is needed
# So let's just do it once per agg now that we have all the numbers

# Calcualte the average clicks & impressions for each agg
for i in agg:
  agg[i]['clicks']['average'] = agg[i]['clicks']['combined'] / agg[i]['count']
  agg[i]['impressions']['average'] = agg[i]['impressions']['combined'] / agg[i]['count']

# Step 5.

# Now we have all the data we need to populate a CSV file
file = open(outputPath, "w")

# Write the headers
file.write(','.join(['age','gender','signed_in','avg_click','avg_impressions','max_click','max_impressions']))

for i in agg:
  row = [
    agg[i]['age'],
    agg[i]['gender'],
    agg[i]['signed_in'],
    agg[i]['clicks']['average'],
    agg[i]['impressions']['average'],
    agg[i]['clicks']['max'],
    agg[i]['impressions']['max']
  ]
  file.write('\n')
  file.write(','.join([str(cell) for cell in row]))

# Finished writing tp the file
file.close()

# Lesson Learned:
# In hindsight I should have probably not nested my clicks or impressions objects and just used avg_* and max_*
# It would mean I could change the output indexes around more easily


