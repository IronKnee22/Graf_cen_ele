import tkinter as tk
from tkinter import messagebox
from today_ele_price import today_electricity_price
from yearly_ele_price import yearly_electricity_price
from year_detail import detail_year
from box_plot import box_plot_graph
from statistic import min_max_function

def show_electricity_price():
    today_electricity_price()

def compare_years():
    year_window = tk.Toplevel(root)
    year_window.title("Compare years")
    year_window.geometry("300x430")

    years = list(range(2010, 2025))
    selected_years = []

    def toggle_year(year):
        if year in selected_years:
            selected_years.remove(year)
        else:
            selected_years.append(year)

    for year in years:
        tk.Checkbutton(year_window, text=str(year), command=lambda year=year: toggle_year(year)).pack(anchor='w')

    def submit_years():
        if selected_years:
            yearly_electricity_price(selected_years)
            year_window.destroy()
        else:
            messagebox.showwarning("Choice", "You must select al least")

    submit_btn = tk.Button(year_window, text="Confirm choice", command=submit_years)
    submit_btn.pack(pady=10)


def select_single_year():
    year_window = tk.Toplevel(root)
    year_window.title("Choose year")
    year_window.geometry("300x430")

    years = list(range(2010, 2025)) 
    selected_year = tk.IntVar()  

    
    def submit_year():
        if selected_year.get() != 0:  
            detail_year(selected_year.get())  
            year_window.destroy()  
        else:
            messagebox.showwarning("Choice", "You must select a year") 

    for year in years:
        tk.Radiobutton(year_window, text=str(year), variable=selected_year, value=year).pack(anchor='w')

    tk.Button(year_window, text="Compare", command=submit_year).pack(pady=20)

def box_plot():
    box_plot_graph()

def function_for_min_max():
    min_max_function()


root = tk.Tk()
root.title("Compare price of electricity")

root.geometry("300x250")

btn_electricity = tk.Button(root, text="Today's Electricity Price", command=show_electricity_price)
btn_electricity.pack(pady=10)

btn_years = tk.Button(root, text="Compare Years", command=compare_years)
btn_years.pack(pady=10)

btn_months = tk.Button(root, text="Specific year", command=select_single_year)
btn_months.pack(pady=10)

btn_box_plot = tk.Button(root, text="Box Plot", command=box_plot)
btn_box_plot.pack(pady=10)

btn_min_max = tk.Button(root, text="Max Min", command=function_for_min_max)
btn_min_max.pack(pady=10)



root.mainloop()
