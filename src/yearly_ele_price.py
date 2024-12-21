import matplotlib.pyplot as plt
import pandas as pd
import os

def yearly_electricity_price(selected_years):
    colors = [
        'b', 'g', 'r', 'c', 'm', 'y', 'k',  
        'orange', 'pink', 'brown', 'purple', 'olive', 'gray', 'indigo',  
        'teal', 'violet', 'lime', 'navy', 'cyan', 'magenta', 'beige',  
        'darkgreen', 'lightblue'  
    ]
    color_cycle = iter(colors)

    plt.figure(figsize=(10, 6))

    for rok in selected_years:
        file_path = f"data/cvs/{rok}.csv"
        
        if os.path.exists(file_path):
            data = pd.read_csv(file_path)
            
            if '-' in data['Den'][0]:  
                data['Den'] = pd.to_datetime(data['Den'], format='%Y-%m-%d').dt.strftime('%m-%d')
            else:  
                data['Den'] = pd.to_datetime(data['Den'], format='%d.%m.%Y').dt.strftime('%m-%d')

            daily_avg = data.groupby('Den')['Marginální cena ČR (Kč/MWh)'].mean().reset_index()

            x = daily_avg['Den']  
            y = daily_avg['Marginální cena ČR (Kč/MWh)']
            
            plt.plot(x, y, label=f"Rok {rok}", color=next(color_cycle))  
    
    plt.xlabel('Day')
    plt.ylabel('Price (Kč/MWh)')
    plt.title('Graph of average daily electricity prices for different years')
    plt.legend()
    plt.grid(True)
    
    plt.show()