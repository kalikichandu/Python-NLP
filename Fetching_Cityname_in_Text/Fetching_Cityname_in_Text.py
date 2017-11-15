import pandas as pd
import string
import time

# Method to fecth the city name in JSON Data
def fetch_city(wordsToFetch):
    cityName = ' '.join(wordsToFetch)
    cityName = string.capwords(cityName)
    if cityName in data[country]:        
        print(cityName)
        
# Recursive Method to loop through all the words in the given text
def process_data(words, length,noOfWords,country):
    words_required = []    
    if noOfWords == 0:        
        return
    else:
        if noOfWords == length:
            words_required = words[:]
        else:
            words_required = words[:noOfWords]
        # Method to fecth the city name in JSON Data
        fetch_city(words_required)
        words_deleting = words[:]    
        while words_required[len(words_required) - 1] != words[len(words) - 1]:            
            counter = 0            
            while len(words)-noOfWords != counter:
                poppedWord = words_deleting.pop(0)
                words_required = words_deleting[:noOfWords]
                counter = counter + 1
                # Method to fecth the city name in JSON Data
                fetch_city(words_required)                       
        noOfWords = noOfWords - 1
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
# End time
t1 = time.time()
print('Execution time = ' +str(t1-t0))
