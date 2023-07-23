# import re to extract between quotes in python
import re
import csv
#Load the file into variable
filename = ""
#Function takes file as input parameter and prints each line
def getlines(filename):
    #try and catch feature to capture if file is unavailable
    try:
        #Read the file and read individual lines
        file = open(filename,"r")
        readfl = file.readlines()
        file.close()
        #Run a for loop to print each line from HL7 JSON
        print ("/////////////////////////////FHIR Resource JSON with comments///////////////////////////////")
        for sentence in readfl:
            print (sentence)
    except FileExistsError:
        print ("File is not there")
#Load the file into variable
filename = ""
def obtainkeys(filename1):
    #try and catch feature to capture if file is unavailable
    try:
        #Convert the entire file into string
        my_str = open(filename1,"r").read()
        #Create a dictionary to identify the keys that match pattern
        #The parenthesis () in the regular expression match whatever is inside and indicate the start and end of a group.
        #The group's contents can still be retrieved after the match.
        #The square brackets [] are used to indicate a set of characters.
        #The caret ^ at the beginning of the set means "NOT". In other words, match all characters that are NOT a double quote.
        #The asterisk * matches the preceding regular expression (anything but double quotes) zero or more times.
        my_list = re.findall(r'\"([^\"]*)\" :',my_str)
        #Printing all the keys into a dictionary
        print ("////////////////KeyWords in HL7 JSON///////////////////////////")
        print (my_list)
        #Returning the dictionary with all keys
        return (my_list)
    except FileExistsError:
        print ("File is not there")
#Load the file into variable
filename2 = ""
#Function defined to have text file and list of words to be searched as input parameters
def wordcount(filename2,listwords):
    #try and catch feature to capture if file is unavailable
    try:
        #Opening the file and reading the contents using readlines feature
        file = open(filename2,"r")
        readfl = file.readlines()
        file.close()
        keycount = 0
        misscount =0
        foundcount =0
        #For loop used to traverse through all the words that needs to be tested
        print ("////////////////Validation of Input Words///////////////////////////")
        for wordck in listwords:
            # Initial counts are set to 0
            count =0
            keycount+=1
            # For Loop to traverse the text file and split the lines for easy comparison
            for sentence in readfl:
                line = sentence.split()
                # For loop to traverse through each separated line to identify the specific word
                for eachck in line:
                    #Comparing the word searched from text file and list of words
                    if (wordck.lower() in eachck.lower())==True:
                            #Increment the count if match is found
                            count+=1
            #Printing end result based on words presence in text file
            if count!=0:
                #Print the word along with its count
                foundcount+=1
                print(wordck,":Found; Count:", count)
            else:
                #Print that value is not found
                misscount +=1
                print(wordck,":Missing")
        #Print the total keywords count from dictionary
        print ("////////////////Final Results///////////////////////////")
        print("Total Keywords Validated:",keycount)
        print("Total Keywords Found:",foundcount)
        print("Total Keywords Missing:",misscount)
    except FileExistsError:
        print ("File is not there")


def csvValidate(csvfilename, dataDomain):
        with open (csvfilename, 'r') as (dataInventory):
            CombinedData = csv.DictReader(dataInventory)
            dataelements = []
            mycsv_list=[] # empty array
            
            # search for data point 
            print ("////////////////Data Domain, Data Element, Data FHIR, FHIR Resource Name from HCS spreadsheet///////////////////////////")
            for row in CombinedData:
                #print(row['Data.Domain'], row['Data.Data Element'])
                dataelements = (row['Data.Domain'],row['Data.Data Element'],row['Data.FHIR'],row['FHIR Resource Name'])
                                                
                #if value in row['Data.Domain']
                if dataDomain in row['FHIR Resource Name']:
                    print(dataelements[0],":", dataelements[1],":", dataelements[2],":",dataelements[3])
                    if dataelements[1]!='':
                     mycsv_list.append(dataelements[1])   
            
        #Print the list of Data elements filtered based on Data Domain        
        print ("////////////////Data Elements in HCS SPREADSHEET///////////////////////////")
        print (mycsv_list)
        
        #Returns the list of Data elements
        return mycsv_list