import pandas as pd

sf = pd.read_excel('./file.xlsx')
numbers = sf['kWh']

a = [max(numbers[i:i+3]) for i in range(0, len(numbers), 4)]


pd.DataFrame(a).to_csv('./file_divided_4.csv')