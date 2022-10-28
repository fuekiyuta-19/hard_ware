import pandas as pd
import glob

filepath = "general_python/datalist/20221028/"
dataname = glob.glob(filepath + "*.xlsx")
print(len(dataname))

for i in range(len(dataname)):
    read_file = pd.read_excel(dataname[i])
    filename  = dataname[i].replace('.xlsx', '.csv')
    read_file.to_csv (filename, index = None, header = True)

print("Task Finish")