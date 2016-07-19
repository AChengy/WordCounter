import urllib2 as url
from scipy import spatial

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
    f.close()

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

#create the vectors for cosine similarity analysis
vectors = []

for dict in wordCounts:
    temp = []
    for key, value in dict.iteritems():
        temp.append(value)

    vectors.append(temp)

#do the cosinie similarity calculations
cosineValues = []
i = 0

while i < 5:
    j = 0
    temp = []
    while j < 5:
        temp.append(1 - spatial.distance.cosine(vectors[i],vectors[j]))
        j+=1
    cosineValues.append(temp)
    i+=1

#print cosineValues

iterator = 0
print '\n\n\n'
print '\t\t\t\t\t<--Cosine Similarity Matrix For All Documents-->'
print '\t\t\t\t  Doc1\t\t\t  Doc2\t\t\t  Doc3\t\t\t  Doc4\t\t\t  Doc5'
while iterator < 5:
    print 'Doc[',iterator+1,']->\t\t%1.6f\t\t%1.6f\t\t%1.6f\t\t%1.6f\t\t%1.6f'% \
            (cosineValues[iterator][0],cosineValues[iterator][1],cosineValues[iterator][2], \
            cosineValues[iterator][3],cosineValues[iterator][4])
    iterator+=1