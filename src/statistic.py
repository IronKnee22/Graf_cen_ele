import matplotlib.pyplot as plt
import os
import pandas as pd
from matplotlib.table import Table

def min_max_function():
    max_day_time = None
    max_day_time_price = float('-inf')
    min_day_time = None
    min_day_time_price = float('inf')

    yearly_averages = {}
    
    for rok in range(2010, 2025):
        file_path = f"data/cvs/{rok}.csv"

        if os.path.exists(file_path):
            data = pd.read_csv(file_path)

            # Převeď sloupec 'Den' na datetime
            if '-' in data['Den'][0]:  # Pokud je datum ve formátu 'YYYY-MM-DD'
                data['Datum'] = pd.to_datetime(data['Den'], format='%Y-%m-%d')
            else:  # Pokud je datum ve formátu 'DD.MM.YYYY'
                data['Datum'] = pd.to_datetime(data['Den'], format='%d.%m.%Y')

            # Najdi maximální hodnotu pro jednotlivé hodiny
            max_row = data.loc[data['Marginální cena ČR (Kč/MWh)'].idxmax()]
            if max_row['Marginální cena ČR (Kč/MWh)'] > max_day_time_price:
                max_day_time_price = max_row['Marginální cena ČR (Kč/MWh)']
                max_day_time = (max_row['Datum'].strftime('%Y-%m-%d'), max_row['Hodina'])

            # Najdi minimální hodnotu pro jednotlivé hodiny
            min_row = data.loc[data['Marginální cena ČR (Kč/MWh)'].idxmin()]
            if min_row['Marginální cena ČR (Kč/MWh)'] < min_day_time_price:
                min_day_time_price = min_row['Marginální cena ČR (Kč/MWh)']
                min_day_time = (min_row['Datum'].strftime('%Y-%m-%d'), min_row['Hodina'])

            # Vypočítej průměrnou cenu pro daný rok
            yearly_avg = data['Marginální cena ČR (Kč/MWh)'].mean()
            yearly_averages[rok] = yearly_avg

    # Najdi rok s nejvyšší a nejnižší průměrnou cenou
    max_avg_year = max(yearly_averages, key=yearly_averages.get)
    min_avg_year = min(yearly_averages, key=yearly_averages.get)

    # Vytvoření tabulky v grafu
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.axis('tight')
    ax.axis('off')
    
    # Tabulková data
    table_data = [
        ['Den a hodina, kdy elektřina stála nejvíce:', f"{max_day_time[0]} {max_day_time[1]}h"],
        ['Nejvyšší cena elektřiny:', f"{max_day_time_price:.2f} Kč/MWh"],
        ['Rok s nejvyšší průměrnou cenou elektřiny:', str(max_avg_year)],
        ['Průměrná cena v tomto roce:', f"{yearly_averages[max_avg_year]:.2f} Kč/MWh"],
        ['Den a hodina, kdy elektřina stála nejméně:', f"{min_day_time[0]} {min_day_time[1]}h"],
        ['Nejnižší cena elektřiny:', f"{min_day_time_price:.2f} Kč/MWh"],
        ['Rok s nejnižší průměrnou cenou elektřiny:', str(min_avg_year)],
        ['Průměrná cena v tomto roce:', f"{yearly_averages[min_avg_year]:.2f} Kč/MWh"]
    ]

    # Vytvoření tabulky pomocí Table objektu
    table = Table(ax, bbox=[0, 0, 1, 1])

    # Přidání sloupců a řádků
    for i, row in enumerate(table_data):
        table.add_cell(i, 0, width=0.5, height=0.1, text=row[0], loc='center')
        table.add_cell(i, 1, width=0.5, height=0.1, text=row[1], loc='center')

    # Nastavení sloupcových popisků
    table.auto_set_column_width([0, 1])

    # Přidání tabulky do grafu
    ax.add_table(table)

    # Zobrazení grafu s tabulkou
    plt.show()

# Zavolání funkce
