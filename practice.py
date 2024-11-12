import tkinter as tk
window = tk.Tk()
window.geometry("500x500")
window.title("Video downloader")


window.mainloop()

import yt_dlp
import tkinter as tk
from tkinter import messagebox

# Function to download audio
def download_audio():
    url = url_entry.get()  # Get the URL from the input field
    if not url:
        messagebox.showwarning("Input Error", "Please enter a URL.")
        return
    
    output_path = "downloaded_audio.mp3"  # Default output file name

    # Set up options for yt-dlp to download only audio
    ydl_opts = {
        'format': 'bestaudio/best',  # Download the best audio format
        'outtmpl': output_path,      # Output path for the audio file
        'postprocessors': [{         # Convert to MP3 if necessary
            'key': 'FFmpegAudioConvertor',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }

    try:
        # Create a yt-dlp object with the specified options
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])  # Download the audio
        messagebox.showinfo("Download Complete", "The audio has been downloaded successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to download audio: {e}")

# Create the Tkinter window
root = tk.Tk()
root.title("Audio Downloader")

# Create a label and input field for the URL
url_label = tk.Label(root, text="Enter the Video URL:")
url_label.pack(pady=10)

url_entry = tk.Entry(root, width=50)
url_entry.pack(pady=10)

download_button = tk.Button(root, text="Download Audio", command=download_audio)
download_button.pack(pady=20)

root.mainloop()


import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

def open_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        with open(file_path, 'r') as file:
            text_editor.delete(1.0, tk.END)
            text_editor.insert(tk.END, file.read())
        root.title(f"Text Editor - {file_path}")

def save_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                             filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if file_path:
        with open(file_path, 'w') as file:
            file.write(text_editor.get(1.0, tk.END))
        root.title(f"Text Editor - {file_path}")

def clear_text():
    text_editor.delete(1.0, tk.END)

root = tk.Tk()
root.title("Text Editor")
root.geometry("600x400")

text_editor = tk.Text(root, wrap="word", undo=True)
text_editor.pack(expand=True, fill="both")

menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Clear", command=clear_text)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)
menu_bar.add_cascade(label="File", menu=file_menu)

root.mainloop()






##download video from youtube
import tkinter as tk
from tkinter import filedialog, messagebox
import yt_dlp

# Define the download function using yt-dlp
def download_video():
    url = url_entry.get()
    if not url:
        messagebox.showwarning("Warning", "Please enter a video URL.")
        return

    # Prompt the user to select a download location
    filepath = filedialog.askdirectory()
    if not filepath:
        messagebox.showwarning("Warning", "No download directory selected.")
        return

    # yt-dlp options
    ydl_opts = {
        'format': 'best',  # Download the best quality
        'outtmpl': f"{filepath}/%(title)s.%(ext)s",  # Output template for filename
    }

    # Download video
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
            messagebox.showinfo("Success", "Video downloaded successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to download video: {e}")

# Initialize Tkinter
root = tk.Tk()
root.title("YouTube Video Downloader")
root.geometry("500x200")

# GUI Layout
url_label = tk.Label(root, text="YouTube Video URL:")
url_label.pack(pady=10)

url_entry = tk.Entry(root, width=50)
url_entry.pack(pady=5)

download_button = tk.Button(root, text="Download Video", command=download_video)
download_button.pack(pady=20)

root.mainloop()


import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

def open_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        with open(file_path, 'r') as file:
            text_editor.delete(1.0, tk.END)
            text_editor.insert(tk.END, file.read())
        root.title(f"Text Editor - {file_path}")

def save_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                             filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if file_path:
        with open(file_path, 'w') as file:
            file.write(text_editor.get(1.0, tk.END))
        root.title(f"Text Editor - {file_path}")

def clear_text():
    text_editor.delete(1.0, tk.END)

# Initialize Tkinter root window
root = tk.Tk()
root.title("Text Editor")
root.geometry("600x400")

# Create a Text widget for editing
text_editor = tk.Text(root, wrap="word", undo=True)
text_editor.pack(expand=True, fill="both")

# Create a menu bar
menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

# Add File menu
file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Clear", command=clear_text)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)
menu_bar.add_cascade(label="File", menu=file_menu)

# Run the Tkinter main loop
root.mainloop()

##download video from youtube
import tkinter as tk
from tkinter import filedialog, messagebox
import yt_dlp

# Define the download function using yt-dlp
def download_video():
    url = url_entry.get()
    if not url:
        messagebox.showwarning("Warning", "Please enter a video URL.")
        return

    # Prompt the user to select a download location
    filepath = filedialog.askdirectory()
    if not filepath:
        messagebox.showwarning("Warning", "No download directory selected.")
        return

    # yt-dlp options
    ydl_opts = {
        'format': 'best',  # Download the best quality
        'outtmpl': f"{filepath}/%(title)s.%(ext)s",  # Output template for filename
    }

    # Download video
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
            messagebox.showinfo("Success", "Video downloaded successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to download video: {e}")

# Initialize Tkinter
root = tk.Tk()
root.title("YouTube Video Downloader")
root.geometry("500x200")

# GUI Layout
url_label = tk.Label(root, text="YouTube Video URL:")
url_label.pack(pady=10)

url_entry = tk.Entry(root, width=50)
url_entry.pack(pady=5)

download_button = tk.Button(root, text="Download Video", command=download_video)
download_button.pack(pady=20)

root.mainloop()
