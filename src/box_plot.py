import os
import pandas as pd
import matplotlib.pyplot as plt

def box_plot_graph():
    yearly_data = []
    for rok in range(2010, 2025):
        file_path = f"data/cvs/{rok}.csv"

        if os.path.exists(file_path):
            data = pd.read_csv(file_path)

            if '-' in data['Den'][0]:  
                data['Den'] = pd.to_datetime(data['Den'], format='%Y-%m-%d')
            else:  
                data['Den'] = pd.to_datetime(data['Den'], format='%d.%m.%Y')

            yearly_data.append(data['Marginální cena ČR (Kč/MWh)'].values)

    plt.figure(figsize=(10, 6))
    plt.boxplot(yearly_data, labels=[str(rok) for rok in range(2010, 2025)], patch_artist=True)

    plt.xlabel('Year')
    plt.ylabel('Price (Czk/MWh)')
    plt.title('Boxplot hourly price of the electricity for each year')
    plt.grid(axis='y')

    plt.show()
