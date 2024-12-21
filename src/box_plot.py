import os
import pandas as pd
import matplotlib.pyplot as plt

def box_plot_graph():
    yearly_data = []
    for rok in range(2010, 2025):
        file_path = f"data/cvs/{rok}.csv"

        if os.path.exists(file_path):
            data = pd.read_csv(file_path)

            # Převeď sloupec 'Den' na datetime
            if '-' in data['Den'][0]:  # Pokud je datum ve formátu 'YYYY-MM-DD'
                data['Den'] = pd.to_datetime(data['Den'], format='%Y-%m-%d')
            else:  # Pokud je datum ve formátu 'DD.MM.YYYY'
                data['Den'] = pd.to_datetime(data['Den'], format='%d.%m.%Y')

            # Přidej všechny hodnoty sloupce 'Marginální cena ČR (Kč/MWh)' do seznamu
            yearly_data.append(data['Marginální cena ČR (Kč/MWh)'].values)

    # Vytvoř boxplot
    plt.figure(figsize=(10, 6))
    plt.boxplot(yearly_data, labels=[str(rok) for rok in range(2010, 2025)], patch_artist=True)

    # Nastavení grafu
    plt.xlabel('Rok')
    plt.ylabel('Cena (Kč/MWh)')
    plt.title('Boxplot hodinových cen elektřiny pro jednotlivé roky')
    plt.grid(axis='y')

    # Zobrazení grafu
    plt.show()
