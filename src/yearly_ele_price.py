import matplotlib.pyplot as plt
import pandas as pd
import os

def yearly_electricity_price(selected_years):
    # Definice barev pro jednotlivé roky
    colors = [
        'b', 'g', 'r', 'c', 'm', 'y', 'k',  # 7 základních barev
        'orange', 'pink', 'brown', 'purple', 'olive', 'gray', 'indigo',  # 7 dalších barev
        'teal', 'violet', 'lime', 'navy', 'cyan', 'magenta', 'beige',  # 7 barev
        'darkgreen', 'lightblue'  # 2 poslední barvy
    ]
    # Cyklické přiřazování barev
    color_cycle = iter(colors)

    plt.figure(figsize=(10, 6))

    # Pro každý rok v seznamu
    for rok in selected_years:
        # Cesta k souboru CSV pro daný rok
        file_path = f"data/cvs/{rok}.csv"
        
        # Zkontroluj, jestli soubor existuje
        if os.path.exists(file_path):
            data = pd.read_csv(file_path)
            
            # Převeď sloupec 'Den' na datetime, aby se získal pouze měsíc-den
            if '-' in data['Den'][0]:  # Pokud je datum ve formátu 'YYYY-MM-DD'
                data['Den'] = pd.to_datetime(data['Den'], format='%Y-%m-%d').dt.strftime('%m-%d')
            else:  # Pokud je datum ve formátu 'DD.MM.YYYY'
                data['Den'] = pd.to_datetime(data['Den'], format='%d.%m.%Y').dt.strftime('%m-%d')

            # Seskupí data podle dne a spočítá průměrnou cenu
            daily_avg = data.groupby('Den')['Marginální cena ČR (Kč/MWh)'].mean().reset_index()

            # Použij správné názvy sloupců pro osy
            x = daily_avg['Den']  # Měsíc-Den
            y = daily_avg['Marginální cena ČR (Kč/MWh)']
            
            # Vykresli data pro tento rok s příslušnou barvou
            plt.plot(x, y, label=f"Rok {rok}", color=next(color_cycle))  # Přidání alpha pro průhlednost

    
    # Přidej popisky, legendu a grid
    plt.xlabel('Den')
    plt.ylabel('Cena (Kč/MWh)')
    plt.title('Graf průměrných denních cen elektřiny pro různé roky')
    plt.legend()
    plt.grid(True)
    
    # Ukázat graf
    plt.show()