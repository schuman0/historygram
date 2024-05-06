import string
#Generate dictionary for storing the character counts
historygram = {char: 0 for char in string.ascii_lowercase}
try:
    #open file
    with open('/var/lib/words/dict', 'r') as file:
        for line in file:
            #remove whitespace and convert to lower
            word = line.strip().lower()
            for char in word:
                #add character to correct dictionary item
                if char in historygram:
                    historygram[char] += 1
    print(historygram)
except:
    print("unable to open file")
