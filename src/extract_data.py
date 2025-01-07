import pandas as pd
from pathlib import Path

for i in range(2010, 2025):
    excel_path_xlsx = Path(f"data/raw/Rocni_zprava_o_trhu_{i}_V0.xlsx")
    excel_path_xls = Path(f"data/raw/Rocni_zprava_o_trhu_{i}_V0.xls")
    
    # Kontrola existence souborů
    if excel_path_xlsx.exists():
        excel_path = excel_path_xlsx
    elif excel_path_xls.exists():
        excel_path = excel_path_xls
    else:
        print(f"File for year {i} was not found.")
        continue

    try:
        # Čtení dat podle roku
        if i <= 2020:
            df = pd.read_excel(
                excel_path,
                sheet_name="DT ČR",
                skiprows=5,
                usecols=[0, 1, 8],
                index_col=None,
                engine="openpyxl" if excel_path.suffix == ".xlsx" else "xlrd"
            )
        else:
            df = pd.read_excel(
                excel_path,
                sheet_name="DT ČR",
                skiprows=5,
                usecols=[0, 1, 9],
                index_col=None,
                engine="openpyxl" if excel_path.suffix == ".xlsx" else "xlrd"
            )
        
        # Uložení do CSV
        df.to_csv(f"data/cvs/{i}.csv", index=False, encoding="utf-8")
        print(f"{i} success")
    except Exception as e:
        print(f"Error processing file for year {i}: {e}")


