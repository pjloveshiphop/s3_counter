import pandas as pd
import os


root=r'C:\Users\Default.DESKTOP-6F3BTUF\Desktop\1월 참여인력'
fileName= r'08.중국어-일본어 번역 말뭉치_참여인력(크라우드)_01월_플리토컨소시엄_1차검수완료.xlsx'

ws = pd.read_excel(os.path.join(root, fileName), sheet_name='크라우드', skiprows=4)
df = pd.DataFrame(ws)

num_rows= df.shape[0]
num_cols= df.shape[1]
print(num_rows)
print(num_cols)

#print(df.columns)
#for col in df.columns:
 #   print(col)

#check '영역'

