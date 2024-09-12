import pandas as pd
from openpyxl.workbook import Workbook

# Writing data to an Excel file
data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [30, 25, 35],
    "City": ["New York", "Los Angeles", "Chicago"]
}

df = pd.DataFrame(data)
df.to_excel('data.xlsx', index=False)
