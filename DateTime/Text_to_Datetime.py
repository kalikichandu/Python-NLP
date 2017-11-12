from datetime import datetime,timedelta
import re

days_of_week = ['sunday','monday','tuesday','wednesday','thursday','friday','saturday']
months_of_year = ['january','february','march','april','may','june','july','august','september','october','november','december']
days = ['tomorrow','today','yesterday','day after tomorrow','day before yesterday']
times = ['evening','morning','night','afternoon','tonight']
clock = ['am','pm']

def daydiff(d,no_days,change_needed):
    x = timedelta(days=no_days)
    if change_needed == 'minus':
        d = d - x;        
    elif change_needed == 'plus':
        d = d + x;        
    return d

def matched_day(words, matched_word, index, context):
    x = datetime.now()
    y = x.strftime("%A")    
    y = y.lower()
    minus_words = ['last', 'previous']
    plus_words = ['this', 'coming', 'next']
    if context == 'days_of_week':
        d = ''
        i = days_of_week.index(y) - days_of_week.index(matched_word)
        for w in minus_words:
            if words[index-1] == w:
                change_needed = 'minus'
                if i > 0:
                    d = daydiff(x, i, change_needed)
                elif i < 0:
                    d = daydiff(x, len(days_of_week) + i, change_needed)
                elif i == 0:
                    d = daydiff(x, len(days_of_week) + i, change_needed)
        for w in plus_words:
            if words[index-1] == w:
                change_needed = 'plus'
                if i > 0:
                    d = daydiff(x, len(days_of_week) - i, change_needed)
                elif i == -1 and w == 'next':
                    d = daydiff(x,len(days_of_week) + 1,change_needed)
                elif i < 0:
                    d = daydiff(x, i*-1, change_needed)
                elif i == 0:
                    d = daydiff(x, len(days_of_week) - i, change_needed)
        
        return words[index-1] +" "+words[index]+" is "+ str(d)
    elif context == 'days':
        minus_words = ['yesterday', 'before']
        plus_words = ['after', 'tomorrow']
        print_word = ""
        if words[index-1] == 'before' or words[index-1] == 'after':
            i = 2
            print_word= 'day ' + words[index-1] + ' '
        elif words[index] == 'yesterday' or words[index] == 'tomorrow':
            i = 1
        elif (words[index]) == 'today':
            i = 0
            d = daydiff(x, i, 'minus')
        for w in minus_words:
            if words[index] == w or words[index-1] == w:
                change_needed = 'minus'                
                d = daydiff(x, i, change_needed)
        for w in plus_words:
            if words[index] == w or words[index-1] == w:
                change_needed = 'plus'                
                d = daydiff(x, i, change_needed)        
        return print_word + words[index] + " is " + str(d)

def textInput(input):
    words = []
    input = input.strip()
    input = re.sub(' +', ' ', input).lower()
    words = input.split(' ')    
    for w in words:
        if w != '':
            for x in days_of_week:
                context = 'days_of_week'
                if x == w:                
                   return matched_day(words,w,words.index(w),context)
            for x in days:
                context = 'days'
                if x == w:                    
                   return matched_day(words, w, words.index(w), context)


class FindDatetime:    
    def __init__(self,sentance):
        self.Inputsentance = sentance
        self.output = str(textInput(re.sub("\W",' ',self.Inputsentance)))       

result = FindDatetime("this friday")
print(result.output)

#sample_text = ["tomorrow","last friday","coming monday","day before Yesterday","next friday"]
