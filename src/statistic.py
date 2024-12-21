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

            if '-' in data['Den'][0]:  
                data['Datum'] = pd.to_datetime(data['Den'], format='%Y-%m-%d')
            else:  
                data['Datum'] = pd.to_datetime(data['Den'], format='%d.%m.%Y')

            max_row = data.loc[data['Marginální cena ČR (Kč/MWh)'].idxmax()]
            if max_row['Marginální cena ČR (Kč/MWh)'] > max_day_time_price:
                max_day_time_price = max_row['Marginální cena ČR (Kč/MWh)']
                max_day_time = (max_row['Datum'].strftime('%Y-%m-%d'), max_row['Hodina'])

            min_row = data.loc[data['Marginální cena ČR (Kč/MWh)'].idxmin()]
            if min_row['Marginální cena ČR (Kč/MWh)'] < min_day_time_price:
                min_day_time_price = min_row['Marginální cena ČR (Kč/MWh)']
                min_day_time = (min_row['Datum'].strftime('%Y-%m-%d'), min_row['Hodina'])

            yearly_avg = data['Marginální cena ČR (Kč/MWh)'].mean()
            yearly_averages[rok] = yearly_avg

    max_avg_year = max(yearly_averages, key=yearly_averages.get)
    min_avg_year = min(yearly_averages, key=yearly_averages.get)

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.axis('tight')
    ax.axis('off')
    
    table_data = [
    ['Day and time when electricity was the most expensive:', f"{max_day_time[0]} {max_day_time[1]}h"],
    ['Highest electricity price:', f"{max_day_time_price:.2f} Czk/MWh"],
    ['Year with the highest average electricity price:', str(max_avg_year)],
    ['Average price in this year:', f"{yearly_averages[max_avg_year]:.2f} Czk/MWh"],
    ['Day and time when electricity was the cheapest:', f"{min_day_time[0]} {min_day_time[1]}h"],
    ['Lowest electricity price:', f"{min_day_time_price:.2f} Czk/MWh"],
    ['Year with the lowest average electricity price:', str(min_avg_year)],
    ['Average price in this year:', f"{yearly_averages[min_avg_year]:.2f} Czk/MWh"]
] 

    table = Table(ax, bbox=[0, 0, 1, 1])

    for i, row in enumerate(table_data):
        table.add_cell(i, 0, width=0.5, height=0.1, text=row[0], loc='center')
        table.add_cell(i, 1, width=0.5, height=0.1, text=row[1], loc='center')

    table.auto_set_column_width([0, 1])

    ax.add_table(table)

    plt.show()

