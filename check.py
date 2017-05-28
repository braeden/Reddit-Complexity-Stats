import praw
import time
r = praw.Reddit('RandSub')


#wait 6 hours from start, 
#Check upvotes from file 0.txt
#iterate up every 5 mins
iterator = 0

while iterator<288:
	with open(str(iterator)+".txt") as f:
		content = f.readlines().decode("utf8")
		#print(content)
		for data in content:
			each = data.strip().split(",")
			s = r.get_submission(each[1])
			print(s.score)
			submissionScore = s.score
			comment = s.comments[0]
			commentScore = comment.score

			outputFile = open('final.txt', 'a')

			outputFile.write(str(each[2]) + "," + str(each[0]) + "," + str(commentScore) + "," + str(submissionScore) + "," + str(each[1]) +"\n")
	print("sleeping")
	time.sleep(300)
	print(str(iterator))
	iterator += 1

outputFile.close()