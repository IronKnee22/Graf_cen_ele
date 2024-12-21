import requests
import matplotlib.pyplot as plt

def today_electricity_price():
    data = requests.get("https://spotovaelektrina.cz/api/v1/price/get-prices-json")
    data = data.json()
    
    hours_today = data.get("hoursToday", [])
    hours = []
    prices = []
    
    for hour_data in hours_today:
        hour = hour_data.get("hour")
        price_czk_mWh = hour_data.get("priceCZK")
        price_czk_kWh = price_czk_mWh / 1000
    
        hours.append(hour)
        prices.append(price_czk_kWh)
    
    hours, prices = zip(*sorted(zip(hours, prices)))
    
    min_price = min(prices)
    max_price = max(prices)
    normalized_prices = [(price - min_price) / (max_price - min_price) for price in prices]
    
    colormap = plt.cm.RdYlGn  
    colors = [colormap(1 - norm_price) for norm_price in normalized_prices]  
    
    fig, ax = plt.subplots(figsize=(12, 7))
    
    for i, (x, y) in enumerate(zip(hours, prices)):
        ax.scatter(x, y, color=colors[i], s=100, edgecolor='k', zorder=3)  
        ax.text(x, y + 0.1, f"{y:.2f}", ha='center', fontsize=9, color='navy')  
    
    ax.plot(hours, prices, linestyle='-', color='deepskyblue', alpha=1, linewidth=2)
    
    ax.set_title('Electricity Price Throughout the Day', fontsize=20, fontweight='bold', color='navy')
    ax.set_xlabel('Hour', fontsize=14, fontweight='bold')
    ax.set_ylabel('Price (kWh) in CZK', fontsize=14, fontweight='bold')
    
    ax.set_xticks(hours)
    ax.set_xticklabels(hours, fontsize=10, rotation=45)
    ax.tick_params(axis='y', labelsize=10)
    ax.grid(True, linestyle='--', linewidth=0.5, alpha=0.7)
    
    ax.set_facecolor('#f7f7f7')
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    
    plt.tight_layout()
    plt.show()
    