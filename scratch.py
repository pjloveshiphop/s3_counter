import boto3
import os
import collections
import glob

## setting up client object ###
client = boto3.client(service_name='s3', endpoint_url ='http://kr.object.ncloudstorage.com')
bucket='aidata-2020-02-009'
root='031.다양한 형태의 한글 문자 이미지 인식 데이터/01.데이터/6. 다양한 형태의 한글 문자 이미지 인식 학습용 데이터(50%이상, 의미적 정확성 검증용)/DATA/'

### setting up paginator and response ### 
paginator = client.get_paginator('list_objects')
response = client.list_objects(Bucket=bucket, Prefix=root, Delimiter='/')

for s in response.get('CommonPrefixes'):
    #sub_prefixes.append(s.get('Prefix'))
    print(s.get('Prefix'))


### genearting all subfolders of prefix given by user ###
#for s in response.get('CommonPrefixes'):
#    sub_prefixes.append(s.get('Prefix'))




