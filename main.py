import tkinter as tk

window = tk.Tk()
window.geometry("400x400")

window.title("Fare Calculator")

design = tk.Label(window,text="Fare Calculator",fg="blue",bg="green",
                  font=("Times New Roman",20),width=100)

design.pack()

fare_choice = tk.StringVar(value="standard")   # user inputs the choice for their ride here
tk.Label(window, text="Choose Fare Type:").pack(pady=5)
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
calculate_button = tk.Button(window, text="Calculate Fare") # button to calculate fare based on the distance using rate per km input.
calculate_button.pack(pady=20)

label_result = tk.Label(window, text="Total Fare: RM 0.00", font=("Arial", 12, "bold"))  # result for now will display static string only
label_result.pack(pady=10)

window.mainloop()