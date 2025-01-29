import tkinter as tk
from tkinter import filedialog, messagebox
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Functionality for the application
def load_data():
    global data
    file_path = filedialog.askopenfilename(title="Select Excel File", filetypes=[("Excel files", "*.xlsx")])
    if file_path:
        try:
            data = pd.read_excel(file_path)
            messagebox.showinfo("Success", "File loaded successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load file: {e}")

def calculate_revenue():
    if data is not None:
        data["Revenue"] = data["Quantity"] * data["Price"]
        messagebox.showinfo("Success", "Revenue calculated successfully!")
    else:
        messagebox.showerror("Error", "No data loaded!")

def top_customers_analysis():
    if data is not None:
        top_customers = data.groupby('Customer ID')["Revenue"].sum().sort_values(ascending=False).head(10)
        fig, ax = plt.subplots(figsize=(10, 6))
        top_customers.plot(kind='bar', ax=ax)
        ax.set_title("Top Customers by Revenue")
        ax.set_xlabel("Customer ID")
        ax.set_ylabel("Revenue")
        plot_in_tkinter(fig)
    else:
        messagebox.showerror("Error", "No data loaded!")

def monthly_revenue_analysis():
    if data is not None:
        data['InvoiceDate'] = pd.to_datetime(data['InvoiceDate'])
        data['Month'] = data['InvoiceDate'].dt.to_period('M')
        monthly_revenue = data.groupby('Month')['Revenue'].sum()
        fig, ax = plt.subplots(figsize=(12, 6))
        monthly_revenue.plot(kind='line', ax=ax)
        ax.set_title("Monthly Revenue Trends")
        ax.set_xlabel("Month")
        ax.set_ylabel("Revenue")
        plot_in_tkinter(fig)
    else:
        messagebox.showerror("Error", "No data loaded!")

def product_performance_analysis():
    if data is not None:
        product_performance = data.groupby('StockCode')['Revenue'].sum().sort_values(ascending=False).head(10)
        fig, ax = plt.subplots(figsize=(10, 6))
        product_performance.plot(kind='bar', ax=ax)
        ax.set_title("Top Performing Products")
        ax.set_xlabel("Stock Code")
        ax.set_ylabel("Revenue")
        plot_in_tkinter(fig)
    else:
        messagebox.showerror("Error", "No data loaded!")

def plot_in_tkinter(fig):
    for widget in plot_frame.winfo_children():
        widget.destroy()
    canvas = FigureCanvasTkAgg(fig, master=plot_frame)
    canvas.draw()
    canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

# Create the main application window
root = tk.Tk()
root.title("Customer Transaction Analysis")
root.geometry("900x700")

# Create a frame for the buttons
button_frame = tk.Frame(root)
button_frame.pack(side=tk.TOP, fill=tk.X)

# Create a frame for the plot
plot_frame = tk.Frame(root)
plot_frame.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

# Add buttons to the button frame
data = None

tk.Button(button_frame, text="Load Data", command=load_data).pack(side=tk.LEFT, padx=10, pady=10)
tk.Button(button_frame, text="Calculate Revenue", command=calculate_revenue).pack(side=tk.LEFT, padx=10, pady=10)
tk.Button(button_frame, text="Top Customers Analysis", command=top_customers_analysis).pack(side=tk.LEFT, padx=10, pady=10)
tk.Button(button_frame, text="Monthly Revenue Trends", command=monthly_revenue_analysis).pack(side=tk.LEFT, padx=10, pady=10)
tk.Button(button_frame, text="Product Performance", command=product_performance_analysis).pack(side=tk.LEFT, padx=10, pady=10)

root.mainloop()
