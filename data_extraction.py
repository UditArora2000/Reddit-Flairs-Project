import pandas as pd
import requests
import json
import csv
import time
import datetime

def getPushshiftData(query, after, before, sub):
    url = 'https://api.pushshift.io/reddit/search/submission/?title='+str(query)+'&size=50000&after='+str(after)+'&before='+str(before)+'&subreddit='+str(sub)
    r = requests.get(url)
    data = json.loads(r.text)
    return data['data']

def collectSubData(subm):
    subData = list()
    tags=['Non-Political', 'Politics', 'AskIndia', 'Sports','Food','[R]eddiquette','Science/Technology','Business/Finance','Policy/Economy', ]
    score =subm['score']
    title = subm['title']
    try:
        flair = subm['link_flair_text']
        if flair not in tags:
            flair="Other"
    except KeyError:
        flair = "NaN"    
    created = datetime.datetime.fromtimestamp(subm['created_utc'])
    numComms = subm['num_comments']
    try:
        body = subm["selftext"]
    except:
    	body = ' '
    sub_id = subm['id']
    if flair!="NaN" :
	    subData.append((title,created,numComms,flair,body,score))
	    subStats[sub_id] = subData

sub='india'
before = "1563259612" 
after = "1531719868"  
query = ""
subCount = 0
subStats = {}
data = getPushshiftData(query, after, before, sub)

flag=0
while len(data) > 0 or flag==1:
    for submission in data:
        collectSubData(submission)
        subCount+=1
    print(len(data))
    print(str(datetime.datetime.fromtimestamp(data[-1]['created_utc'])))
    after = data[-1]['created_utc']
    try:
        data = getPushshiftData(query, after, before, sub)
        flag=0
    except:
    	flag=1
    
print(str(len(subStats)) + " submissions have added to list")

def updateSubs_file():
    upload_count = 0
    file = "data1.csv"
    with open(file, 'w', newline='', encoding='utf-8') as file: 
        a = csv.writer(file, delimiter=',')
        headers = ["Title","Publish Date","Total No. of Comments","Flair","Body","Score"]
        a.writerow(headers)
        for sub in subStats:
            a.writerow(subStats[sub][0])
            upload_count+=1
            
        print(str(upload_count) + " submissions have been uploaded")
updateSubs_file()
