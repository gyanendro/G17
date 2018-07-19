from __future__ import division
from sklearn.metrics import accuracy_score
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

f = open(sys.argv[1],"r")
lines = f.readlines()
f.close()
ori=[]
pre=[]
tag_dict = dict()

for l in lines:
	s = l.strip().replace(' ','').split('\t')
	#print s
	if len(s) >= 3:
		ori.append(s[1])
		pre.append(s[2])
		if s[1] == s[2]:
			if s[1] not in tag_dict:
				tag_dict[s[1]] = dict()
				tag_dict[s[1]]['tp'] = 0
				tag_dict[s[1]]['fp'] = 0
				tag_dict[s[1]]['fn'] = 0
			tag_dict[s[1]]['tp'] += 1
		else:
			if s[1] not in tag_dict:
				tag_dict[s[1]] = dict()
				tag_dict[s[1]]['tp'] = 0
				tag_dict[s[1]]['fp'] = 0
				tag_dict[s[1]]['fn'] = 0
			if s[2] not in tag_dict:
				tag_dict[s[2]] = dict()
				tag_dict[s[2]]['tp'] = 0
				tag_dict[s[2]]['fp'] = 0
				tag_dict[s[2]]['fn'] = 0
			tag_dict[s[1]]['fn']+=1
			tag_dict[s[2]]['fp']+=1

for tag in tag_dict:
	try:
		pr = tag_dict[tag]['tp']/(tag_dict[tag]['tp']+tag_dict[tag]['fp'])
	except:
		pr = 0
	try:
		rec = tag_dict[tag]['tp']/(tag_dict[tag]['tp']+tag_dict[tag]['fn'])
	except:
		rec = 0
	try:
		f1 = ((pr*rec)/(pr+rec))*2
	except:
		f1 = 0
	print tag,pr,rec,f1


print 'Accuracy : ', accuracy_score(ori, pre)
