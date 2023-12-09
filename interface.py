import tkinter as tk
from tkinter import ttk

def calculate_depression_score():
    # Calculate the depression score (example calculation)
    total_score = 0
    for i, entry in enumerate(questions_entries):
        answer = entry.get()
        if answer == 'Not at all':
            score = 0
        elif answer == 'Several days':
            score = 1
        elif answer == 'More than half the days':
            score = 2
        elif answer == 'Nearly every day':
            score = 3
        else:
            total_score=-1
            break
        total_score += score

    # Display the depression score with a more user-friendly message
    if total_score == -1:
        result_message = "Please complete all questions before calculating."
    elif total_score == 0:
        result_message = "You appear to have minimal symptoms of depression."
    elif total_score <= 9:
        result_message = "You may be experiencing mild symptoms of depression. Consider seeking support."
    elif total_score <= 19:
        result_message = "Your depression symptoms are moderate. It's advisable to consult a healthcare professional."
    else:
        result_message = "Your depression symptoms are severe. Please seek immediate help."
    if total_score > 0:
        result_message = result_message + "\nIf you need help, you can reach you can reach out to the IMH Mental Health helpline at 6389 2222 or contacting imh_appt@imh.com.sg."
    if total_score != -1:
        calculate_button.destroy()
    result_label.config(text=result_message)



# Create the main application window
root = tk.Tk()
root.title("Depression Screening Test")

# Set a more soothing background color
root.configure(bg='#89CFF0')

# Set the initial size of the main window
root.geometry("900x700")  # Width x Height

# Define the questions
questions = [
    "Little interest or pleasure in doing things?",
    "Feeling down, depressed, or hopeless?",
    "Trouble falling asleep, staying asleep, or sleeping too much?",
    "Feeling tired or having little energy?",
    "Poor appetite or overeating?",
    "Feeling bad about yourself - or that you are a failure or have let yourself or your family down?",
    "Trouble concentrating on things, such as reading the newspaper or watching television",
    "Moving or speaking so slowly that other people could have noticed? Or the opposite - being\nso fidgety or restless that you have been moving around a lot more than usual?",
    "Thoughts that you would be better off dead, or of hurting yourself",
    "If you checked off any problems, how difficult have these\nproblems made it for you at work, home, or with other people?",
]

title_label = ttk.Label(root, text="", font=("Arial", 18, "bold"), wraplength=400, background='#89CFF0')
title_label.pack(pady=(5, 5))
title_label.config(text="Depression Test")

# Create input fields for questions
questions_entries = []
for question in questions:
    label = ttk.Label(root, text=question, font=("Arial", 14))
    label.pack(pady=(1, 0))
    answer = ttk.Combobox(root, values=["Not at all", "Several days", "More than half the days", "Nearly every day"],
                          font=("Arial", 12))
    answer['state'] = 'readonly'
    answer.pack(pady=1)
    questions_entries.append(answer)

# Create a button to calculate the depression score
calculate_button = ttk.Button(root, text="Calculate Depression Score", command=calculate_depression_score)
calculate_button.pack(pady=20)

# Create a label to display the depression score
result_label = ttk.Label(root, text="", font=("Arial", 14, "bold"), wraplength=400, background='#89CFF0')
result_label.pack(pady=(0, 20))
# Create a titled frame for writing a message on the right

# Start the GUI application
root.mainloop()