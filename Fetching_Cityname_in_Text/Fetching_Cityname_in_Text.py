import pandas as pd
import string
import time

# Method to fecth the city name in JSON Data
def fetch_city(wordsToFetch):
    #converting list to str with space in between the words
    cityName = ' '.join(wordsToFetch)
    cityName = string.capwords(cityName)
    if cityName in data[country]:        
        print(cityName)
        
# Recursive Method to loop through all the words in the given text
def process_data(words, length,noOfWords,country):
    words_required = []    
    words_deleting = words[:] 
    # Recursive function returns when the number words become zero.
    if noOfWords == 0:        
        return
    else:
        # In the first run number of words will be equal to length of words. so reading all the data to words_required variable
        if noOfWords == length:
            words_required = words[:]
        else:
            #In the subsequent runs words upto noOfWords will be taken into words_required
            words_required = words[:noOfWords]
        # Method to fecth the city name in JSON Data
        fetch_city(words_required)           
        while words_required[len(words_required) - 1] != words[len(words) - 1]:            
            counter = 0            
            while len(words)-noOfWords != counter:
                #Popping out the words
                poppedWord = words_deleting.pop(0)
                words_required = words_deleting[:noOfWords]
                counter = counter + 1
                # Method to fecth the city name in JSON Data
                fetch_city(words_required)                       
        noOfWords = noOfWords - 1
        #call to the same function
        return process_data(words, length, noOfWords,country)

    
#Data containing city names which needs to be fetched
textData = "we are in new delhi kavali hyderabad nellore kadapa google mysore"
# Country name to fetch the city name
country = "India"
country = string.capwords(country)
#start Timer
t0 = time.time()
#Reading the JSON data of Country and cities using Pandas module is series type
data = pd.read_json("Countriestocities.json",typ='Series')
words = []
words = textData.split(' ')
length = len(words)
# Main method where the data is processed
process_data(words, length, length,country)
# End timer
t1 = time.time()
print('Execution time = ' +str(t1-t0))
