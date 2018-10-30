
This script is developed to read text force-displacement data, convert them to pandas data frame, write them in the original folders, and finally create a big excel data frame and format the header.
This is developed for seatBack ATW project for David.

import pandas as pd
import numpy as np
import os

root='t:/seatback/woHole/solid/Curve121'
dfAll=pd.DataFrame()
excelN=0

for dirName,subdirList,fileList in os.walk(root):
    for file in fileList:
        if file=='rcForce':
            simulation+=1
            FOLDER=dirName
            rFOLDER="%r" %FOLDER #string to raw_string
            rFOLDER=rFOLDER.split('\\')
            print('{0:2d} {1}'.format(simulation,rFOLDER[-1]))
            FILE=file
            fin=open(FOLDER+'/'+file,'r')
            disp=[]
            force=[]
            for line in fin: 
                if len(line.split())==1: continue
                disp.append(float(line.split()[0])/10.)
                force.append(float(line.split()[1]))
            dfDisp=pd.DataFrame(np.array(disp))
            dfForce=pd.DataFrame(np.array(force)) 
            fin.close()
            dfDisp.columns=['Displacement_'+rFOLDER[-1]]
            dfForce.columns=['Force_'+rFOLDER[-1]]
            df=[dfDisp,dfForce]
            df=pd.concat(df,axis=1)
            df.to_excel(FOLDER+'/'+FILE+'.xlsx',index=False)
            dfAll=pd.concat([df,dfAll],axis=1)

writer = pd.ExcelWriter(root+'/'+'forceDisp.xlsx', engine='xlsxwriter')
dfAll.to_excel(writer, sheet_name='Sheet1', startrow=1, header=False)
workbook = writer.book
worksheet = writer.sheets['Sheet1']
header_format = workbook.add_format({
    'bold': True,
    'text_wrap': True,
    'valign': 'top',
    'fg_color': '#D7E4BC',
    'border': 1})
for col_num, value in enumerate(dfAll.columns.values):
    worksheet.write(0, col_num + 1, value, header_format)
writer.save()