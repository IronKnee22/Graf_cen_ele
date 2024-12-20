import pandas as pd
from pathlib import Path

for i in range(2010, 2025,):
    excel_path = Path(f"D:/Programing/Graf_cen_ele/data/raw/Rocni_zprava_o_trhu_{i}_V0.xls")
    
    try:
        if (i<=2020):
            df = pd.read_excel(excel_path, sheet_name="DT ČR", skiprows=5, usecols=[0, 1, 8], index_col=None, engine="xlrd")
        else:
            df = pd.read_excel(excel_path, sheet_name="DT ČR", skiprows=5, usecols=[0, 1, 9], index_col=None, engine="xlrd")
        df.to_csv(f"data/cvs/data_{i}.csv", index=False, encoding="utf-8")
        print(f"{i} success")
    except FileNotFoundError:
        print(f"File for year {i} was not found.")

