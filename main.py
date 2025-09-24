import tkinter as tk

def update_rate_label():
    """Updates the displayed rate based on the selected fare type."""
    selected_fare = fare_choice.get()
    rate = 0.0
    if selected_fare == "standard":
        rate = 1.20
    elif selected_fare == "peak":
        rate = 1.50
    elif selected_fare == "holiday":
        rate = 1.80
    
    rate_label.config(text=f"Rate per km: RM {rate:.2f}")

def calculate_fare():
    """Calculates and displays the total fare."""
    try:
        distance = float(distance_input.get())
        
        # Set rate per km based on fare type
        rate = 0.0
        if fare_choice.get() == "standard":
            rate = 1.2
        elif fare_choice.get() == "peak":
            rate = 1.5
        elif fare_choice.get() == "holiday":
            rate = 1.8
        
        total = rate * distance
        label_result.config(text=f"Total Fare: RM {total:.2f}")
    except ValueError:
        label_result.config(text="Invalid input. Please enter numeric values.")

# GUI window
window = tk.Tk()
window.geometry("400x400")
window.title("Fare Calculator")

design = tk.Label(window, text="Fare Calculator", fg="white", bg="green",
                  font=("Times New Roman", 20), width=100)
design.pack()

# Initialize variables
fare_choice = tk.StringVar(value="standard")

tk.Label(window, text="Choose Fare Type:").pack(pady=5)
tk.Radiobutton(window, text="Standard", variable=fare_choice, value="standard", command=update_rate_label).pack()
tk.Radiobutton(window, text="Peak Hours", variable=fare_choice, value="peak", command=update_rate_label).pack()
tk.Radiobutton(window, text="Public Holiday", variable=fare_choice, value="holiday", command=update_rate_label).pack()

# Rate display label
rate_label = tk.Label(window, text="", font=("Arial", 10, "bold"))
rate_label.pack(pady=5)
update_rate_label() # Call on startup to show default rate

# Distance input
tk.Label(window, text="Distance (km):").pack(pady=5)
distance_input = tk.Entry(window)
distance_input.pack()

# Calculate button
calculate_button = tk.Button(window, text="Calculate Fare", command=calculate_fare)
calculate_button.pack(pady=20)

# Result label
label_result = tk.Label(window, text="Total Fare: RM 0.00", font=("Arial", 12, "bold"))
label_result.pack(pady=10)

window.mainloop()

#the changes