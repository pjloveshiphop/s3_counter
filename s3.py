import boto3
import pandas as pd
import os

endpoint_url = 'http://kr.object.ncloudstorage.com'

buckets=["aidata-2020-02-001","aidata-2020-02-001","aidata-2020-02-001",	
"aidata-2020-02-001",	"aidata-2020-02-002",	"aidata-2020-02-002",	"aidata-2020-02-002",	
"aidata-2020-02-002",	"aidata-2020-02-003",	"aidata-2020-02-003",	"aidata-2020-02-003",	
"aidata-2020-02-003",	"aidata-2020-02-004",	"aidata-2020-02-004",	"aidata-2020-02-004",	"aidata-2020-02-004",	
"aidata-2020-02-004",	"aidata-2020-02-005",	"aidata-2020-02-005",	"aidata-2020-02-005",	"aidata-2020-02-006",	"aidata-2020-02-006",	
"aidata-2020-02-006",	"aidata-2020-02-006",	"aidata-2020-02-007",	"aidata-2020-02-007",	"aidata-2020-02-008",	"aidata-2020-02-008",	
"aidata-2020-02-008",	"aidata-2020-02-009",	"aidata-2020-02-009",	"aidata-2020-02-009",	"aidata-2020-02-048",	"aidata-2020-02-055"]

prefixes=["001.자유대화(일반남여)/01.데이터/6.",	"002.자유대화(노인남여)/01.데이터/6.",	"003.자유대화(소아남여, 유아 등 혼합)/01.데이터/6.",	"004.한국인 외래어 발화/01.데이터/6.",	
"005.명령어 데이터(일반남여-정형‧비정형 포함)/01.데이터/6.",	"006.명령어 데이터(노인남여-정형‧비정형 포함)/01.데이터/6.",	"007.명령어 데이터(소아남여,유아-정형‧비정형 포함)/01.데이터/6.",	
"008.차량 내 대화 및 명령어 데이터/01.데이터/6.",	"009.한국어 강의 데이터/01.데이터/6.",	"010.회의 음성 데이터/01.데이터/6.",	"011.고객 응대 데이터/01.데이터/6.",	"012.상담 음성 데이터/01.데이터/6.",	
"013.한국어 방언 발화 데이터(강원도)/01.데이터/6.",	"014.한국어 방언 발화 데이터(경상도)/01.데이터/6.",	"015.한국어 방언 발화 데이터(전라도)/01.데이터/6.",	"016.한국어 방언 발화 데이터(제주도)/01.데이터/6.",	
"017.한국어 방언 발화 데이터(충청도)/01.데이터/6.",	"018.논문자료 요약 데이터/01.데이터/6.",	"019.도서자료 요약 데이터/01.데이터/6.",	"020.한국어 대화 요약 데이터/01.데이터/6.",	"021.도서자료 기계독해/01.데이터/6.",	
"022.민원(콜센터) 질의-응답 데이터/01.데이터/6.",	"023.전문분야 말뭉치 데이터(분야별 개체명 인식 포함)/01.데이터/6.",	"024.한국어 SNS 데이터/01.데이터/6.",	"025.한국어-영어 1 번역 말뭉치/01.데이터/6.",	
"026.한국어-영어 2 번역 말뭉치/01.데이터/6.",	"027.한국어-중국어 번역 말뭉치 1/01.데이터/6.",	"028.한국어-중국어 번역 말뭉치 2/01.데이터/6.",	"029.한국어-일본어 번역 말뭉치/01.데이터/6.",	
"030.야외 실제 촬영 한글 이미지/01.데이터/6.",	"031.다양한 형태의 한글 문자 이미지 인식 데이터/01.데이터/6.",	"032.공공행정문서 OCR/01.데이터/6.",	"126.생활 및 거주환경 VQA/01.데이터/6.",	"133.고서 한자 인식/01.데이터/6."]


prefixes2 = ["027.한국어-중국어 번역 말뭉치 1/01.데이터/6.한국어-중국어 번역 말뭉치 1 데이터셋(50% 이상, 의미적 정확성 검증용)/", ]


df= pd.DataFrame()
result=[]
### setting up client object ###
client = boto3.client(service_name='s3', endpoint_url =endpoint_url)

paginator = client.get_paginator('list_objects')
#response = client.list_objects(Bucket=buckets[i], Prefix=prefixes[i])
response = client.list_objects(Bucket="aidata-2020-02-055", Prefix="126.생활 및 거주환경 VQA/01.데이터/6. 생활 및 거주환경 VQA 학습용 데이터(50%이상, 의미적 정확성 검증용)/실내 가전 및 가구배치 이미지 수집/"+subs[i])

#pages= paginator.paginate(Bucket=buckets[i], Prefix=prefixes[i])
pages= paginator.paginate(Bucket="aidata-2020-02-048", Prefix="126.생활 및 거주환경 VQA/01.데이터/6. 생활 및 거주환경 VQA 학습용 데이터(50%이상, 의미적 정확성 검증용)/실내 가전 및 가구배치 이미지 수집/"+subs[i])


for page in pages:
    for obj in page['Contents']:
        #print(obj)
        if obj['Key'][-1:] !='/':
            count+=1  

result.append("126.생활 및 거주환경 VQA/01.데이터/6."+subs[i]+">> 파일개수: "+str(count))
count=0
    
df.insert(0, "result", result)
file_dest = r'C:\Users\Default.DESKTOP-6F3BTUF\Desktop\fileChecker'
df.to_csv(os.path.join(file_dest,'result_48.csv'), index=False, encoding="utf-8-sig") 

print("Done. check out the result")
