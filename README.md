# 📂 Smart File Saver
Originated for my personal use and curiosity to build something usefull using tkinter and python!

A simple but smart **Python desktop app** (built with \`tkinter\`) that saves a copy of a \`.txt\` file into a date-organized folder structure — **with Portuguese month names** — and keeps a preview right in the app.  
It remembers your last selected file and destination folder, so you can easily use it daily.

---

## ✨ Features
- 📅 **Automatic date-based organization** with folders like:
```

destination_folder/  
	2025/  
		Agosto/  
			2025.08.10\_myfile.txt

```
- 🗂 **Portuguese month names** instead of numbers  
- 🖼 **Preview pane** to see the file’s contents before saving  
- 💾 **Remembers your last file & folder** between runs  
- 🛡 **Keeps file metadata** with \`shutil.copy2\`  
- 🎯 **Simple GUI** for picking the destination folder and file

---

## 📸 Screenshot
<img width="600" height="530" alt="image" src="https://github.com/user-attachments/assets/a99fac61-dfe9-426b-8d9d-fa6b6937adb6" />


---

## 🚀 How to Run
1. **Clone this repository**
```bash
git clone https://github.com/JoseVColino/Daily_Entry_Saver.git
cd Daily_Entry_Saver
```
2. **Install Python if you haven't** (3.8+ recommended)
3. **Run the app**
```bash
python app.py
```

---

## 🛠 Dependencies

Only Python’s **standard library** is used:

- `tkinter` – GUI elements & dialogs
- `pathlib` – path handling
- `datetime` – date formatting
- `shutil` – file copying
- `os` – screen and path utilities

---

## 💡 How It Works

1. You pick a **destination folder**
2. You pick a `.txt` file
3. The app:
	- Reads today’s **year, month (Portuguese), day**
	- Creates the folder path inside your chosen destination if needed
	- Saves a copy of the file with the format `YYYY.MM.DD_filename.txt`
4. The last used file & folder are saved to `previous_file.txt` so they can be reloaded next time

---

## 📜 License

MIT License – feel free to use, modify, and share.

---

## 🙌 Author

Developed by **José Victor Colino** — because coding is fun and saving files isn't.
