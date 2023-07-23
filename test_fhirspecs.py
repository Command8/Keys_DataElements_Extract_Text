#Calling functions from python scripts to perform validations
from Dev_functions import getlines,obtainkeys,wordcount,csvValidate

#Load the textfiles and HCS spreadsheet csv into variables
input = "Input.txt"
output = "Output.txt"
csv =  "HCS_CombinedData.csv"

#Choose the Data Domain to identify the Data elements
fhir_resource = "Coverage"

#Prints all lines in input textfile 
getlines(input)

#Prints all keys in a dictionary and returns list
obtainkeys(input)

#print all the data.data.Elements in HCS csv for each resource and returns a list of strings.
csvValidate(csv, fhir_resource)

#Prints keys presence in Liquid template
#wordcount(output,(obtainkeys(input)))
#wordcount(output,csvValidate(csv, data_domain)))
wordcount(output,(obtainkeys(input)+csvValidate(csv, fhir_resource)))