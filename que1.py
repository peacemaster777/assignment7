# Q1
import tkinter as tk

def calculate_gst():
    original_cost = float(original_cost_entry.get())
    net_price = float(net_price_entry.get())

    gst_rate = ((net_price - original_cost) * 100) / original_cost

    gst_result_label.config(text="GST Rate: {:.2f}%".format(gst_rate))

# Create the main window
window = tk.Tk()
window.title("GST Tax Finder Calculator")

# Create labels and entries for original cost and net price
original_cost_label = tk.Label(window, text="Original Cost:")
original_cost_label.pack()
original_cost_entry = tk.Entry(window)
original_cost_entry.pack()

net_price_label = tk.Label(window, text="Net Price:")
net_price_label.pack()
net_price_entry = tk.Entry(window)
net_price_entry.pack()

# Create a button to calculate the GST rate
calculate_button = tk.Button(window, text="Calculate GST", command=calculate_gst)
calculate_button.pack()

# Create a label to display the GST result
gst_result_label = tk.Label(window, text="")
gst_result_label.pack()

# Start the GUI event loop
window.mainloop()