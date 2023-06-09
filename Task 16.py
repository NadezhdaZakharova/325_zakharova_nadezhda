file = open("C:\\Users\\Надежда\\Documents\\GitHub\\125_zakharova_nadezhda\\rows_300.csv", "w") 
import time
from datetime import datetime
for i in range(1,301):
    time.sleep(0.01)
    current_datetime = datetime.now()
    #print(current_datetime)
    dt = str(current_datetime)
    h = str(i)
    t = str(current_datetime.date)
    file.write(h + ';')
    file.write(dt[0:16] + ';')
    file.write(dt[17:19] + ';')
    file.write(dt[20:26] + ';')
    file.write('\n')
file.close()