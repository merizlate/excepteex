def read_results(file_name):
  # import the csv module
  import csv
  # create an empty list to store the results
  results = []
  # open the file in read mode
  with open(file_name, 'r') as f:
    # create a csv reader object
    reader = csv.reader(f)
    # skip the header row
    next(reader)
    # loop through the rows
    for row in reader:
      # append the row to the results list
      results.append(row)
  # return the results list
  return results
