import pandas as pd
import csv
import numpy as np
header = ['Time','Temperature°C','Humidity%']

f = open('Export.csv', 'w' ,encoding='UTF8',newline='')
b = open('Export2.csv', 'w' ,encoding='UTF8',newline='')

writer = csv.writer(f)
writer2 = csv.writer(b)
writer.writerow(header)
writer2.writerow(header)
df = pd.read_csv('csv.csv', parse_dates=['Time'], index_col='Time',encoding = "ISO-8859-1")
hours = -1
if_filter = input('would you like your time to be filtered? (Y/N) : ')
if_day = input('is daily data required? (Y/N) : ')
if if_filter == 'Y' or if_filter == 'y':
    start = input('Enter Start Time: (2020-01-01) : ')
    end = input('Enter End Time: (2020-01-01) : ')
    dd = df.loc[start:end]
else:
    dd = df
for x in dd.iterrows():
    time = x[0]
    if hours == -1:
        hours = time.hour
        sum1 = 0
        count = 0
        sum2 = 0
        day = time.day
        daytime = time

    if hours == time.hour:
        count +=1
        sum1 += x[1][0]
        sum2 += x[1][1]

    else:
        av1 = sum1/count
        av2 = sum2/count
        writer.writerow(['Average Hour '+str(hours),av1,av2])
        writer2.writerow([last,av1,av2])
        sum1 = 0
        count = 0
        sum2 = 0
        # Next Hour
        count += 1
        sum1 += x[1][0]
        sum2 += x[1][1]
        hours = time.hour
    if if_day == 'y' or if_day == 'Y':
        if day != time.day:
            daydf = df.loc[daytime: time]
            writer.writerow(['End of Day : '+str(daytime.day), 'Max: '+str(daydf['Temperature¡C'].max()),'Max: '+str(daydf['Humidity%'].max())])
            writer.writerow(['', 'Min: '+str(daydf['Temperature¡C'].min()),'Min: '+str(daydf['Humidity%'].min())])
            writer.writerow(['', 'Avg: '+str(daydf['Temperature¡C'].mean()),'Avg: '+str(daydf['Humidity%'].mean())])
            writer.writerow([])
            day = time.day
            daytime = time

    writer.writerow([x[0], x[1][0], x[1][1]])
    last = x[0]

f.close()
b.close()