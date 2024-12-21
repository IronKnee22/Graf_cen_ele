import matplotlib.pyplot as plt
import pandas as pd

def detail_year(selected_year):
    # Cesta k souboru
    file_path = f"data/cvs/{selected_year}.csv"
    
    # Načtení dat do DataFrame
    df = pd.read_csv(file_path)
    
    if selected_year >= 2014:
        # Formát je YYYY-MM-DD, převedení na datetime
        df['Den'] = pd.to_datetime(df['Den'], format='%Y-%m-%d')
    else:
        # Formát je DD.MM.YYYY, převedení na datetime
        df['Den'] = pd.to_datetime(df['Den'], format='%d.%m.%Y')
    
    # Vytvoření grafu
    plt.figure(figsize=(10, 6))
    
    # Vykreslení marginální ceny pro každý den a hodinu
    plt.plot(df['Den'], df['Marginální cena ČR (Kč/MWh)'], label=f'Marginální cena {selected_year} (Kč/MWh)')
    
    # Nastavení popisků a titulu
    plt.title(f'Marginální cena ČR v roce {selected_year}')
    plt.xlabel('Datum')
    plt.ylabel('Cena (Kč/MWh)')
    plt.xticks(rotation=45)
    
    # Přidání legendy
    plt.legend()
    
    # Zobrazení grafu
    plt.tight_layout()
    plt.show()