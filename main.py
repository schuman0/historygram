import string
historygram = {char: 0 for char in string.ascii_lowercase}
try:
    with open('/var/lib/words/dict', 'r') as file:
        for line in file:
            word = line.strip().lower()
            for char in word:
                if char in historygram:
                    historygram[char] += 1
    print(historygram)
except:
    print("unable to open file")