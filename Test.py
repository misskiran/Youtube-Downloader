import tkinter as tk
from tkinter import messagebox
from pytube import YouTube

def download_video():
    url = url_entry.get()
    try:
        youtube = YouTube(url)
        if resolution_choice.get() == "1080p":
            video = youtube.streams.filter(res="1080p").first()
        else:
            video = youtube.streams.get_by_resolution(resolution_choice.get())
        video.download()
        messagebox.showinfo(title="Video Downloaded", message="Video has been downloaded successfully!")
    except:
        messagebox.showerror(title="Error", message="An error occurred while downloading the video.")
        

# Create the main window
window = tk.Tk()
window.title("YouTube Downloader")
window.geometry("600x600")
window.configure(bg="gray29")

# Create the URL label and entry
url_label = tk.Label(window, text="Enter YouTube URL:", font=("Britannic Bold", 16), bg="#F2F2F2")
url_label.pack(pady=20)

url_entry = tk.Entry(window, width=40, font=("Britannic Bold", 14), bg="#FFF")
url_entry.pack()

# Create the video quality label and radio buttons
quality_label = tk.Label(window, text="Choose video quality:", font=("Britannic Bold", 16), bg="#F2F2F2")
quality_label.pack(pady=20)

resolution_choice = tk.StringVar()
resolution_choice.set("720p")

quality_frame = tk.Frame(window, bg="#F2F2F2")

quality_radio_1080p = tk.Radiobutton(quality_frame, text="1080p", variable=resolution_choice, value="1080p", font=("Britannic Bold", 14), bg="#F2F2F2")
quality_radio_1080p.pack(side="left", padx=20)


quality_radio_720p = tk.Radiobutton(quality_frame, text="720p", variable=resolution_choice, value="720p", font=("Britannic Bold", 14), bg="#F2F2F2")
quality_radio_720p.pack(side="left", padx=20)

quality_radio_480p = tk.Radiobutton(quality_frame, text="480p", variable=resolution_choice, value="480p", font=("Britannic Bold", 14), bg="#F2F2F2")
quality_radio_480p.pack(side="left", padx=20)

quality_radio_360p = tk.Radiobutton(quality_frame, text="360p", variable=resolution_choice, value="360p", font=("Britannic Bold", 14), bg="#F2F2F2")
quality_radio_360p.pack(side="left", padx=20)

quality_radio_240p = tk.Radiobutton(quality_frame, text="240p", variable=resolution_choice, value="240p", font=("Britannic Bold", 14), bg="#F2F2F2")
quality_radio_240p.pack(side="left", padx=20)


quality_frame.pack()

# Create the download button
download_button = tk.Button(window, text="Download Video", font=("Britannic Bold",13), bg="red3", fg="#FFF", command=download_video)
download_button.pack(pady=20)

# Start the GUI
window.mainloop()
