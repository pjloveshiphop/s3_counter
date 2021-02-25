import pandas as pd
import os


myfiles = [f for f in os.listdir(r'C:\Users\Default.DESKTOP-6F3BTUF\Desktop\주간보고excel')]
for i in range(len(myfiles)):

    wb = pd.read_excel(os.path.join(r'C:\Users\Default.DESKTOP-6F3BTUF\Desktop\주간보고excel',myfiles[i]), sheet_name='붙임3.데이터셋 구축 실적관리')
    df = pd.DataFrame(wb)

    df_selected_cols = df[['데이터셋명', '데이터공정', '전체계획', '주간실적(누계)']]
    


    
    
    #sort data by column name
    #data=df_cols.sort_values(by='데이터셋명', axis=0, ascending=True, inplace=False, kind='quicksort', na_position='last')
    #data.to_csv(os.path.join(r'C:\Users\Default.DESKTOP-6F3BTUF\Desktop', 'trial.csv'), mode='a', index=False, encoding='utf-8-sig')

