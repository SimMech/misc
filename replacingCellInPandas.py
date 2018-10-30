import pandas as pd
dataFrame=pd.read_excel('c:/temp/GM-F.xlsx')

#extracting a column from a database
time=dataFrame['Time']

#multiply a column by a scaler
time.head(5)
time=time*10
time.head(5)

#replacing a cell with a new value
t=10.44
dataFrame.set_value(0,'Time',t)
writer=pd.ExcelWriter('c:/temp/test.xlsx')
dataFrame.to_excel(writer,'Sheet1', index=False)
writer.save()

#renaming the column title
dataFrame.rename(columns={'Time':'newTime'})

#drawing two columns of a dataFrame
import matplotlib.pyplot as plt
plt.scatter(dataFrame['True Strain'],dataFrame['True Stress'])
plt.show()