import matplotlib.pyplot as plt
import pandas as pd

def detail_year(selected_year):
    file_path = f"data/cvs/{selected_year}.csv"
    
    df = pd.read_csv(file_path)
    
    if selected_year >= 2014:
        df['Den'] = pd.to_datetime(df['Den'], format='%Y-%m-%d')
    else:
        df['Den'] = pd.to_datetime(df['Den'], format='%d.%m.%Y')
    
    plt.figure(figsize=(10, 6))
    
    plt.plot(df['Den'], df['Marginální cena ČR (Kč/MWh)'], label=f'Marginální cena {selected_year} (Kč/MWh)')
    
    plt.title(f'Marginal price of the Czech Republic in {selected_year}')
    plt.xlabel('Date')
    plt.ylabel('Price (Czk/MWh)')
    plt.xticks(rotation=45)
    
    plt.legend()
    
    plt.tight_layout()
    plt.show()