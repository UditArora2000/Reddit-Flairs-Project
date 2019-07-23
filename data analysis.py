import csv
np={}
p={}
sp={}
f={}
ai={}
red={}
st={}
bf={}
pe={}
o={}

np['score']=0
p['score']=0
sp['score']=0
f['score']=0
ai['score']=0
red['score']=0
st['score']=0
bf['score']=0
pe['score']=0
o['score']=0

np['comments']=0
p['comments']=0
sp['comments']=0
f['comments']=0
ai['comments']=0
red['comments']=0
st['comments']=0
bf['comments']=0
pe['comments']=0
o['comments']=0

np['nops']=0
p['nops']=0
sp['nops']=0
f['nops']=0
ai['nops']=0
red['nops']=0
st['nops']=0
bf['nops']=0
pe['nops']=0
o['nops']=0

times=[]
for i in range(24):
	times.append(0)
tags=['Non-Political', 'Politics', 'AskIndia', 'Sports','Food','[R]eddiquette'
,'Science/Technology','Business/Finance','Policy/Economy', 'Other']
with open("data.csv",'r',encoding="utf-8") as fil:
	w=csv.reader(fil)
	t=0
	for x in w:
		if t==0:
			t=1
		else:
			x[5]=int(x[5])
			x[2]=int(x[2])
			if x[3]==tags[0]:
				np['score']+=x[5]
				np['comments']+=x[2]
				np['nops']+=1
			elif x[3]==tags[1]:
				p['score']+=x[5]
				p['comments']+=x[2]
				p['nops']+=1
			elif x[3]==tags[2]:
				ai['score']+=x[5]
				ai['comments']+=x[2]
				ai['nops']+=1
			elif x[3]==tags[3]:
				sp['score']+=x[5]
				sp['comments']+=x[2]
				sp['nops']+=1
			elif x[3]==tags[4]:
				f['score']+=x[5]
				f['comments']+=x[2]
				f['nops']+=1
			elif x[3]==tags[5]:
				red['score']+=x[5]
				red['comments']+=x[2]
				red['nops']+=1
			elif x[3]==tags[6]:
				st['score']+=x[5]
				st['comments']+=x[2]
				st['nops']+=1
			elif x[3]==tags[7]:
				bf['score']+=x[5]
				bf['comments']+=x[2]
				bf['nops']+=1
			elif x[3]==tags[8]:
				pe['score']+=x[5]
				pe['comments']+=x[2]
				pe['nops']+=1
			elif x[3]==tags[9]:
				o['score']+=x[5]
				o['comments']+=x[2]
				o['nops']+=1

			sta=x[1].find(' ')
			sta+=1
			z=x[1][sta:sta+2]
			z=int(z)
			times[z]+=1


np['scorepp']=np['score']/np['nops']
p['scorepp']=p['score']/p['nops']
sp['scorepp']=sp['score']/sp['nops']
f['scorepp']=f['score']/f['nops']
ai['scorepp']=ai['score']/ai['nops']
red['scorepp']=red['score']/red['nops']
st['scorepp']=st['score']/st['nops']
bf['scorepp']=bf['score']/bf['nops']
pe['scorepp']=pe['score']/pe['nops']
o['scorepp']=o['score']/o['nops']

np['compp']=np['comments']/np['nops']
p['compp']=p['comments']/p['nops']
sp['compp']=sp['comments']/sp['nops']
f['compp']=f['comments']/f['nops']
ai['compp']=ai['comments']/ai['nops']
red['compp']=red['comments']/red['nops']
st['compp']=st['comments']/st['nops']
bf['compp']=bf['comments']/bf['nops']
pe['compp']=pe['comments']/pe['nops']
o['compp']=o['comments']/o['nops']


print(np,p,ai,sp,f,red,st,bf,pe,o,times)

