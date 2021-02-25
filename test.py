#!/usr/bin/python
import boto3, os, sys, collections, time
import pandas as pd
from datetime import datetime


#bucket = input('Enter Bucket Name: ')
#root = input('Enter Prefix: ')
#endpoint_url = input('Enter Endpoint-URL: ')

print("Commencing Counting Process..........")
start_time = time.time()

now=datetime.now()
date=now.strftime('%Y-%m-%d')

endpoint_url=str(sys.argv[1])
bucket = str(sys.argv[2])
root = str(sys.argv[3])

sub_prefixes=list()
folder_name=list()
count=0
file_count= list()
file_names= list()
file_ext=list()
cnt = collections.Counter()


### setting up client object ###
client = boto3.client(service_name='s3', endpoint_url ='http://'+endpoint_url)

### setting up paginator and response ### 
paginator = client.get_paginator('list_objects')
response = client.list_objects(Bucket=bucket, Prefix=root, Delimiter='/')


### genearting all subfolders of prefix given by user ###
for s in response.get('CommonPrefixes'):
    sub_prefixes.append(s.get('Prefix'))

if len(sub_prefixes)!=0:
    for i in range(len(sub_prefixes)):
        pages= paginator.paginate(Bucket=bucket, Prefix=sub_prefixes[i])
        for page in pages:
            for obj in page['Contents']:
                if obj['Key'][-1:] !='/':
                    count+=1
                    file_names.append(obj['Key'])

        for f in file_names:
            name, ext  = os.path.splitext(f)
            cnt[ext]+=1
    
        folder_name.append(sub_prefixes[i][len(root):])
        file_count.append(count)
        count=0
        file_ext.append(str(cnt)[7:])
        cnt.clear()
        file_names=list()
        


df= pd.DataFrame()
df.insert(0, "Folder_Name", folder_name)
df.insert(1, "File_Count", file_count)
df.insert(2, "Count by extension", file_ext)

file_dest = desktop = os.path.join(os.environ['USERPROFILE'], 'Desktop')
df.to_csv(os.path.join(file_dest,'{}_output_{}.csv'.format(root[:root.find('/')],date)), index=False, encoding="utf-8-sig") 


print("All Jobs Are Finished. Check Out the Result")
print('Execution took {} seconds'.format(round(time.time()-start_time,2)))
