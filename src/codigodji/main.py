import tkinter as tk

def on_submit(event=None):
    user_input = entry.get()
    print("User typed:", user_input)

# Create the main window
root = tk.Tk()
root.title("Input Example")
root.geometry("400x300")

# Create o campo de entrada
entry = tk.Entry(root, width=30)
entry.pack(pady=20)
entry.bind("<Return>", on_submit)

# Create a submit button
submit_btn = tk.Button(root, text="Consultar EAN", command=on_submit)
submit_btn.pack()

# Start the GUI event loop
root.mainloop()
# This code creates a simple GUI application using Tkinter.
# It includes an entry field for user input and a button to submit the input.

