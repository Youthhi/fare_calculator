import tkinter as tk

# --- Theming Data ---
current_theme = "light"
themes = {
    "light": {
        "bg": "white",
        "fg": "black",
        "header_bg": "green",
        "header_fg": "white",
        "button_bg": "SystemButtonFace",
        "button_fg": "black",
        "select_color": "white"
    },
    "dark": {
        "bg": "#2e2e2e",
        "fg": "white",
        "header_bg": "#1e1e1e",
        "header_fg": "white",
        "button_bg": "#444444",
        "button_fg": "white",
        "select_color": "#2e2e2e"
    }
}

# --- Functions ---

def toggle_theme():
    """Switches the application's color theme between light and dark."""
    global current_theme
    current_theme = "dark" if current_theme == "light" else "light"
    
    colors = themes[current_theme]
    
    window.config(bg=colors["bg"])
    design.config(bg=colors["header_bg"], fg=colors["header_fg"])
    
    for widget in window.winfo_children():
        if isinstance(widget, tk.Label):
            if "Fare Calculator" not in widget.cget("text"):
                widget.config(bg=colors["bg"], fg=colors["fg"])
        elif isinstance(widget, tk.Radiobutton):
            widget.config(bg=colors["bg"], fg=colors["fg"], selectcolor=colors["select_color"])
        elif isinstance(widget, tk.Button):
            widget.config(bg=colors["button_bg"], fg=colors["button_fg"])
    
    distance_input.config(bg="white", fg="black")
    tip_entry.config(bg="white", fg="black")
    label_result.config(bg=colors["bg"], fg=colors["fg"])

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

def toggle_tip_field():
    """Shows or hides the tip input frame based on the checkbox state."""
    if tip_checkbox_var.get():
        tip_frame.pack()
    else:
        tip_frame.pack_forget()
        tip_entry.delete(0, tk.END)

def calculate_fare():
    """Calculates and displays the total fare, including an optional tip."""
    try:
        distance = float(distance_input.get())
        tip_amount = 0.0
        if tip_checkbox_var.get():
            tip_input = tip_entry.get()
            tip_amount = float(tip_input) if tip_input else 0.0
        
        rate = 0.0
        if fare_choice.get() == "standard":
            rate = 1.2
        elif fare_choice.get() == "peak":
            rate = 1.5
        elif fare_choice.get() == "holiday":
            rate = 1.8
        
        total = (rate * distance) + tip_amount
        label_result.config(text=f"Total Fare: RM {total:.2f}")
    except ValueError:
        label_result.config(text="Invalid input. Please enter numeric values.", fg="red")

def reset_all():
    """Resets all input fields, radio buttons, and the result."""
    distance_input.delete(0, tk.END)
    tip_entry.delete(0, tk.END)
    fare_choice.set("standard")
    update_rate_label()
    tip_checkbox_var.set(False)
    toggle_tip_field()
    label_result.config(text="Total Fare: RM 0.00", fg=themes[current_theme]["fg"])

# --- GUI window ---
window = tk.Tk()
window.geometry("400x450")
window.title("Fare Calculator")

design = tk.Label(window, text="Fare Calculator", fg="white", bg="green",
                  font=("Times New Roman", 20), width=100)
design.pack()

# Initialize variables
fare_choice = tk.StringVar(value="standard")
tip_checkbox_var = tk.BooleanVar(value=False)

tk.Label(window, text="Choose Fare Type:").pack(pady=5)
tk.Radiobutton(window, text="Standard", variable=fare_choice, value="standard", command=update_rate_label).pack()
tk.Radiobutton(window, text="Peak Hours", variable=fare_choice, value="peak", command=update_rate_label).pack()
tk.Radiobutton(window, text="Public Holiday", variable=fare_choice, value="holiday", command=update_rate_label).pack()

rate_label = tk.Label(window, text="", font=("Arial", 10, "bold"))
rate_label.pack(pady=5)
update_rate_label()

tk.Label(window, text="Distance (km):").pack(pady=5)
distance_input = tk.Entry(window)
distance_input.pack()

# New: Checkbox for Tip and its frame
tip_checkbox = tk.Checkbutton(window, text="Add Tip", variable=tip_checkbox_var, command=toggle_tip_field)
tip_checkbox.pack(pady=5)

tip_frame = tk.Frame(window)
tip_label = tk.Label(tip_frame, text="Tip (RM):")
tip_entry = tk.Entry(tip_frame)
tip_label.pack(side=tk.LEFT, padx=(0, 5))
tip_entry.pack(side=tk.RIGHT)

button_frame = tk.Frame(window)
button_frame.pack(pady=20)

calculate_button = tk.Button(button_frame, text="Calculate Fare", command=calculate_fare)
calculate_button.pack(side=tk.LEFT, padx=5)

reset_button = tk.Button(button_frame, text="Reset All", command=reset_all)
reset_button.pack(side=tk.LEFT, padx=5)

theme_button = tk.Button(button_frame, text="Toggle Theme", command=toggle_theme)
theme_button.pack(side=tk.LEFT, padx=5)

label_result = tk.Label(window, text="Total Fare: RM 0.00", font=("Arial", 12, "bold"))
label_result.pack(pady=10)

window.mainloop()