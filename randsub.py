import praw
import json
import math
import string
import time
r = praw.Reddit(user_agent="test")
f = open('englishOrder1.txt', 'r')
#text_file = open("Output.txt", "w")
##	subreddit = r.get_subreddit('random')
#	text_file.write(str(subreddit)+"\n")
#	print x
#text_file.close
#upvotes to word complexity - defaults

# sed --in-place -re '43900,456628d' englishOrder.txt 
#sed 's/[0-9]*//g' englishOrder.txt > englishOrder1.txt 
i = 0

dictionary = f.read().splitlines()
lines = [line.rstrip('\n') for line in open('defaults.txt')]

while i<288:
	for sub in lines:
		print(sub)
		subreddit = r.get_subreddit(sub)
		comments = subreddit.get_comments(limit=1)
		for comment in comments:
			print(comment.body)
			complexityScaled = 0
			words = str(comment.body.encode('ascii', 'ignore')).translate(None, string.punctuation).lower().split()
			wordCount = len(words)
			for word in words:
				#print(word)
				logTrans = 0
				if word in dictionary:
					logTrans = math.log((math.ceil(dictionary.index(word)))/5+1, 2)
					#print(logTrans)
					if logTrans > 0:
						math.ceil(logTrans)
					else:
						logTrans=0
					complexityScaled+=(logTrans)
					#print("true")
				else:
					wordCount -= 1

			#print(complexityScaled)
			#print(wordCount)
			avgComplexity = complexityScaled/(wordCount+1)
			avgComplexity = round(avgComplexity, 4)
			print(avgComplexity)
			outputFile = open(str(i)+'.txt', 'a')
			outputFile.write(str(avgComplexity) + "," + str(comment.permalink.decode('utf-8').encode('ascii', errors='ignore')) + "," + sub + "\n")
	if i is 72:
		os.system("check.py")
	i += 1
	time.sleep(300)
f.close()
outputFile.close()