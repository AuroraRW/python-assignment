#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

import sys
import re
from glob import iglob

"""Baby Names

Define the extract_names() function below and change main()
to call it.

For writing regex, it's nice to include a copy of the target
text for inspiration.

Here's what the html looks like in the baby.html files:
...
<h3 align="center">Popularity in 1990</h3>
....
<tr align="right"><td>1</td><td>Michael</td><td>Jessica</td>
<tr align="right"><td>2</td><td>Christopher</td><td>Ashley</td>
<tr align="right"><td>3</td><td>Matthew</td><td>Brittany</td>
...

Suggested milestones for incremental development:
 -Extract the year and print it
 -Extract the names and rank numbers and just print them
 -Get the names data into a dict and print it
 -Build the [year, 'name rank', ... ] list and print it
 -Fix main() to use the extract_names list
"""

def extract_names(filename):
  """
  Given a file name for baby.html, returns a list starting with the year string
  followed by the name-rank strings in alphabetical order.
  ['2006', 'Aaliyah 91', Aaron 57', 'Abagail 895', ' ...]
  """
  #open the file, read the content
  file=open(filename,'r')
  babytext=file.read()
  file.close()

  #read the year
  year=re.search(r'Popularity\sin\s(\d\d\d\d)', babytext)
  result=[]
  if year:
      result.append(year.group(1))
    
  #read the baby name information 
  babylist=re.findall(r'<td>(\d+)</td><td>(\w+)</td>\<td>(\w+)</td>', babytext)
    
  #If a name appears more than once, then choose the one with the smaller rank.
  babydic={}  
  for baby in babylist:
    if baby[1] not in babydic:
      babydic[baby[1]]=baby[0]
    if baby[2] not in babydic:
      babydic[baby[2]]=baby[0]
    
  #make the output format
  for babykey in babydic.keys():
    babystr=babykey+' '+babydic[babykey]
    result.append(babystr)   
    
  #sort the result
  resultsorted=sorted(result)
    
  return resultsorted

def main():
  # This command-line parsing code is provided.
  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  
  args = sys.argv[1:]

  if not args:
    print('usage: [--summaryfile] file [file ...]')
    sys.exit(1)

  # Notice the summary flag and remove it from args if it is present.
  summary = False
  if args[0] == '--summaryfile':
    summary = True
    del args[0]
    
  # For each filename, get the names, then either print the text output
  # or write it to a summary file

  #print the text output
  if summary== False:
    
    for filename in args:
      babyresult = extract_names(filename)
      babytext = '\n'.join(babyresult)
      print(babytext)

  #write the text to a summary file    
  else:
    #read the html file name
    for temp in args:     
      for filename in iglob(temp):
        babyresult = extract_names(filename)
        babytext = '\n'.join(babyresult)
        #write into a summary file
        outputfile = open(filename + '.summary', 'w')
        outputfile.write(babytext + '\n')
        outputfile.close()

      
if __name__ == '__main__':
  main()
