import json
import csv

with open('log') as json_file:
  data = json.load(json_file)

assert len(data['all']) == len(data['one'])

data_file = open('log.csv', 'w')
csv_writer = csv.writer(data_file)
csv_writer.writerow(['cores', 'all', 'one'])

for i, (all_e, one_e) in enumerate(zip(data['all'], data['one'])):
    csv_writer.writerow([i, all_e, one_e])

data_file.close()
