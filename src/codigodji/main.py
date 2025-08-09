import tkinter as tk
import glob
import pandas as pd

def on_submit(event=None):
    input_ean = entry.get()
    print("Input EAN:", input_ean)
    code400 = search_code400_by_ean(input_ean)
    print("Código 400:", code400)
    if code400:
        label_code400.config(text=f'Código Intelbras: {code400}')
    else:
        label_code400.config(text="Código Intelbras não encontrado.")
    entry.delete(0, tk.END) # Clear the input field

def read_excels():
    files = glob.glob("*.xlsx") + glob.glob("*.xls")
    dfs = []
    for file in files:
        df = pd.read_excel(file)
        dfs.append(df)
    all_data = pd.concat(dfs, ignore_index=True)
    return all_data

def search_code400_by_ean(ean):
    # This function would contain the logic to search for the EAN in the data
    print(f"Searching for EAN: {ean}")
    # Here you would implement the search logic, e.g., filtering a DataFrame
    data = read_excels() 
    trimmed = data['EAN DJI'].astype(str).str.strip()
    data_found = (data[trimmed == str(ean).strip()])

    if not data_found.empty:
        return(data_found['Código 400'].values[0])
    else:
        print(f'No data found for EAN: {ean}')

# Create the main window
root = tk.Tk()
root.title("Input Example")
root.geometry("400x300")

# Add a label
label_code400 = tk.Label(root, text="")
label_code400.pack(pady=10)

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

