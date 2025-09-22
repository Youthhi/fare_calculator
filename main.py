import tkinter as tk

def calculate_fare(): # function to calculate fare based on distance and rate per km
    try:
        rate = float(rate_input.get()) # variable to store the fare rate (input by user)
        distance = float(distance_input.get()) # variable to store the ride distance in km (input by user)
        
        # Calculate total fare based on fare type
        if fare_choice.get() == "standard": # standard fare calculation
            total = rate * distance
        elif fare_choice.get() == "peak":
            total = rate * distance * 1.5  # 50% increase during peak hours
        elif fare_choice.get() == "non-peak":
            total = rate * distance * 0.8  # 20% decrease during non-peak hours
        else:
            total = 0
        
        label_result.config(text=f"Total Fare: RM {total:.2f}") # display the total fare calculated
    except ValueError:
        label_result.config(text="Invalid input. Please enter numeric values.") # error handling for non-numeric input
        
window = tk.Tk()
window.geometry("400x400")

window.title("Fare Calculator")

design = tk.Label(window,text="Fare Calculator",fg="white",bg="green",
                  font=("Times New Roman",20),width=100)

design.pack()

# Initialize variables
fare_choice = tk.StringVar(value="standard")   # user inputs the choice for their ride here
 
tk.Label(window, text="Choose Fare Type:").pack(pady=5)  # user inputs the choice for their ride here
tk.Radiobutton(window, text="Standard", variable=fare_choice, value="standard").pack()
tk.Radiobutton(window, text="Peak Hours", variable=fare_choice, value="peak").pack()
tk.Radiobutton(window, text="Non-Peak Hours", variable=fare_choice, value="non-peak").pack()

# Rate per km input
tk.Label(window, text="Rate per km (RM):").pack(pady=5) # user inputs the rate
rate_input = tk.Entry(window)
rate_input.pack()

# Distance input
tk.Label(window, text="Distance (km):").pack(pady=5) #  user inputs their distance
distance_input = tk.Entry(window)
distance_input.pack()

# Calculate button
calculate_button = tk.Button(window, text="Calculate Fare", command=calculate_fare) # button to calculate fare based on the distance using rate per km input.
calculate_button.pack(pady=20)

label_result = tk.Label(window, text="Total Fare: RM 0.00", font=("Arial", 12, "bold"))  # result for now will display static string only
label_result.pack(pady=10)

window.mainloop()