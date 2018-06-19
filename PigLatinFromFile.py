with open("b.in", "r") as f:
    data = f.readlines()
holder = 0
vowels = ['a', 'e', 'i', 'o', 'u', 'y']
for line in data:
    words = line.split()
    for word in range(0, len(words)):
        moreData = ''
        extraData = ''
        if words[word][0] in vowels:
            words[word] += ("yay")
            #print(words)
        for j in range(0, len(words[word])):
            if words[word][j] not in vowels:
                extraData += words[word][j]
                var = j - 1
                if var > -1:
                    moreData = words[word][j]
            if (words[word][j] in vowels and not (words[word].endswith('ay'))):
                holder = words[word].index(moreData)
                words[word] = words[word][(holder + 1):]
                words[word] += extraData
                words[word] += 'ay'
    print(words)
