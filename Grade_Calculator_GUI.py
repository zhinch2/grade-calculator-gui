import tkinter as tk
from tkinter import messagebox
import time

def calculate_grade():
    user_input = entry_score.get()
    
    try:
        # Split the input string at the '/' character
        parts = user_input.split("/")
        if len(parts) != 2:
            raise ValueError("Invalid format")
            
        # Convert the text parts into numbers
        scored = float(parts[0].strip())
        total = float(parts[1].strip())
        
        if total == 0:
            raise ValueError("Total cannot be zero")

        # 1. Show a thinking message in the result area and update the window
        label_message_val.config(text="Thinking...", fg="#666666")
        label_percentage_val.config(text="--")
        label_grade_val.config(text="--")
        root.update()  # Forces the window to refresh so "Thinking..." appears immediately

        # 2. Pause for 2 seconds (just like your original script)
        time.sleep(2)

        # Calculate the percentage
        percentage = (scored / total) * 100

        # Determine the grade
        if percentage >= 90:
            grade = "A"
            message = "Amazing work!"
        elif percentage >= 80:
            grade = "B"
            message = "Good job!"
        elif percentage >= 70:
            grade = "C"
            message = "Nice try!"
        elif percentage >= 60:
            grade = "D"
            message = "Better luck next time!"
        else:
            grade = "F"
            message = "Oh no..."

        # 3. Display the final results
        label_percentage_val.config(text=f"{round(percentage, 2)}%")
        label_grade_val.config(text=grade)
        label_message_val.config(text=message, fg="#333333")

    except (ValueError, IndexError):
        label_message_val.config(text="")
        messagebox.showerror("Error", "Please enter your score in the correct format, e.g., 45/50")

# Initialize the main window
root = tk.Tk()
root.title("Grade Calculator")
root.geometry("320x350")
root.resizable(False, False)

# Title / Banner label
title_label = tk.Label(root, text="GRADE CALCULATOR", font=("Arial", 14, "bold"))
title_label.pack(pady=15)

# Score prompt and input field
label_prompt = tk.Label(root, text="Enter your score (e.g., 45/50):", font=("Arial", 10))
label_prompt.pack(pady=5)

entry_score = tk.Entry(root, font=("Arial", 11), justify="center", width=20)
entry_score.pack(pady=5)

# Calculate Button
btn_calculate = tk.Button(root, text="Calculate Grade", font=("Arial", 10, "bold"), bg="#4CAF50", fg="white", command=calculate_grade)
btn_calculate.pack(pady=12)

# Results Frame/Display
result_frame = tk.Frame(root)
result_frame.pack(pady=10)

# Percentage Result
tk.Label(result_frame, text="Percentage: ", font=("Arial", 10)).grid(row=0, column=0, sticky="e", pady=2)
label_percentage_val = tk.Label(result_frame, text="--", font=("Arial", 10, "bold"))
label_percentage_val.grid(row=0, column=1, sticky="w", pady=2)

# Grade Result
tk.Label(result_frame, text="Your Grade: ", font=("Arial", 10)).grid(row=1, column=0, sticky="e", pady=2)
label_grade_val = tk.Label(result_frame, text="--", font=("Arial", 10, "bold"))
label_grade_val.grid(row=1, column=1, sticky="w", pady=2)

# Motivational Message Result
label_message_val = tk.Label(root, text="", font=("Arial", 11, "italic"), fg="#333333")
label_message_val.pack(pady=10)

# Run the application loop
root.mainloop()