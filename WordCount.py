import urllib2 as url
iterator = 0
urls = ["https://www.csuohio.edu/engineering/eecs/faculty-staff", "http://engineering.case.edu/eecs/",
        "http://my.clevelandclinic.org/research", "https://en.wikipedia.org/wiki/Data_mining",
        "https://en.wikipedia.org/wiki/Data_mining#Data_mining"]
wordCounts = []

while iterator < 5:
    words = {'engineering' : 0, 'professor' : 0 , 'research' : 0 , 'data' : 0 , 'mining' : 0  }
    f = url.urlopen(urls[iterator])

    for line in f:
        words2 = line.split(" ")
        for wrd in words2:
            if words.has_key(wrd.lower()):
                words[wrd.lower()] = int(words[wrd.lower()]) + 1

    #print words
    wordCounts.append(words)
    iterator += 1

#print wordCounts

#print the number of occurences for each word
iterator =  0
print "\t\t\t<--Document Vectors For Key Words-->"
print "\t\t\tengineering\tprofessor\tresearch\tdata\tmining"
while iterator < 5:
    print "Doc[",iterator+1,"]->\t\t",wordCounts[iterator]['engineering'],"\t\t\t",wordCounts[iterator]['professor'], \
        "\t\t\t",wordCounts[iterator]['research'],"\t\t",wordCounts[iterator]['data'],"\t\t", \
        wordCounts[iterator]['mining']
    iterator += 1

