'''writes the word frequence of a website in a text file'''

from bs4 import BeautifulSoup
import re
import urllib.request as urlReq

url = 'https://www.gutenberg.org/files/39947/39947-h/39947-h.htm'
reqObj = urlReq.urlopen(url)
raw_html = reqObj.read()

wordCount = {}
#raw_html = open('contrived.html').read()

html = BeautifulSoup(raw_html, 'html.parser')
for fullText in html.select('body'):
    findWords = re.findall( r'\w+', fullText.text, re.M|re.I)
    for word in findWords:
        if word in wordCount:
            wordCount[word]+=1
        else:
            wordCount[word]=1

descendingCount = list(wordCount.values())
descendingCount.sort(reverse=True)
print(type(descendingCount))

words = list(wordCount.keys())
counts = list(wordCount.values())

textFile = open('words.txt', 'w')
for nextMaxCount in descendingCount:
    index = counts.index(nextMaxCount)
    nextFrequentWord = words[index]
    counts.remove(nextMaxCount)
    del words[index]
    textFile.write(nextFrequentWord+' : '+str(nextMaxCount)+'\n')
textFile.close()
