import pandas as pd
import glob

filepath = "general_python/datalist/20221110/"
dataname = glob.glob(filepath + "*.xlsx")

for i in range(len(dataname)):
    read_file = pd.read_excel(dataname[i])
    filename  = dataname[i].replace('.xlsx', '.csv')
    read_file.to_csv (filename, index = None, header = True)

print("Task Finish!")