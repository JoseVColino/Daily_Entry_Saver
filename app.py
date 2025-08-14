import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from datetime import datetime
from datetime import timedelta
from pathlib import Path
import shutil
import os

root = tk.Tk()
window_width, window_height = 600, 500

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_displacement = (screen_width // 2) - (window_width // 2)
y_displacement = (screen_height // 2) - (window_height // 2)

root.geometry(f"{window_width}x{window_height}+{x_displacement}+{y_displacement}")

root.title("this is my lazy file saver")

file_path = tk.StringVar()

portuguese_month_dict = {
    1: 'Janeiro',
    2: 'Fevereiro',
    3: 'Marco',
    4: 'Abril',
    5: 'Maio',
    6: 'Junho',
    7: 'Julho',
    8: 'Agosto',
    9: 'Setembro',
    10: 'Outubro',
    11: 'Novembro',
    12: 'Dezembro',
}

def update_preview(file_path: str):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
        preview.delete("1.0", tk.END)
        preview.insert(tk.END, content)

def lazy_structure_saving(file_path: str, destination_folder: str):
    if (last_day):
        now = datetime.now() - timedelta(days=1)
    else:
        now = datetime.now()

    year = str(now.year)
    month = portuguese_month_dict[now.month]
    day = f'{now.day:02}'

    base = Path(destination_folder)
    dir_path = base / year / month
    dir_path.mkdir(parents=True, exist_ok=True)

    format_file_name = f'{year}.{now.month:02}.{day}_{Path(file_path).name}'

    shutil.copy2(file_path, dir_path / format_file_name)
    update_previous_file()

    messagebox.showinfo(
        title='Success!',
        message=f'File was successfully saved at {file_path}',
        icon='info',
        default='ok'
    )

def update_previous_file():
    with open('previous_file.txt', 'w', encoding='utf8') as file:
        file.writelines([file_path.get() + '\n', destination_folder.get()])

def retrieve_previous_file():
    try:
        with open('previous_file.txt', 'r', encoding='utf8') as file:
            file_from_previous = file.readline().strip()
            destination_folder_from_previous = file.readline().strip()

            file_path.set(file_from_previous)
            destination_folder.set(destination_folder_from_previous)

        update_preview(file_from_previous)
    except FileNotFoundError:
        pass

def handle_pick_file_button():
    file = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    
    if file:
        file_path.set(file)
        update_preview(file_path.get())

def handle_save_button():
    lazy_structure_saving(file_path.get(), destination_folder.get())

def handle_destination_folder_button():
    folder = filedialog.askdirectory()
    destination_folder.set(folder)

tk.Label(text="Select a destination folder:").pack()
destination_folder = tk.StringVar()

tk.Label(textvariable=destination_folder).pack()

tk.Button(
    text='pick folder',
    command=handle_destination_folder_button
).pack()

tk.Label(text="Is the destination folder okay?\n if so, pick a file by clicking the button bellow").pack()

tk.Label(root, textvariable=file_path).pack()
tk.Button(
    root,
    text='pick file',
    command=handle_pick_file_button
).pack()

tk.Button(
    root,
    text='save file', 
    command= handle_save_button, 
).pack()

last_day = tk.BooleanVar()
tk.Checkbutton(text="Past midnight? ", variable=last_day).pack()

tk.Label(root, text='Preview of text file:').pack()

preview = tk.Text(
    root
)
preview.pack()

retrieve_previous_file()

root.mainloop()