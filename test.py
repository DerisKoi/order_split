import csv
import pandas as pd
# f = csv.reader(open('cpst1.csv', 'r'))
# for i in f:
#     print(i)

data = pd.read_table('out_0.csv', header=None, sep=',', encoding='utf8')
print(data.shape)
row_num, column_num =data.shape
for i in range(0, 100):
    save_data = data.iloc[i*180000+1:(i+1)*180000+1, :]
    file_name = 'C:\\Users\\Lenovo\\Desktop\\yz\\2\\cpst' + str(i) + '.csv'
    save_data.to_csv(file_name, header=None, index=False)
