import tkinter as tk
from tkinter import filedialog
from moviepy.editor import VideoFileClip
from moviepy.editor import *
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip

# Function to play video
def play_video():
    video_path = filedialog.askopenfilename(filetypes=[("Video Files", "*.mp4 *.avi *.mov")])
    if video_path:
        video_clip = VideoFileClip(video_path)
        video_clip.preview()  # Plays the video in an external window

# Function to set impersonalization effect (this is placeholder)
def set_imparson(val):
    print(f"Impersonation effect set to: {val}")

# Function to set waxonation effect (this is placeholder)
def set_waxonator(val):
    print(f"Waxonator effect set to: {val}")

# Creating the main window
root = tk.Tk()
root.title("YTP+ Clone Program")

# Create sliders for "Imparson" and "Waxonator"
label_imparson = tk.Label(root, text="Imparson:")
label_imparson.pack()
imparson_slider = tk.Scale(root, from_=0, to=100, orient=tk.HORIZONTAL, command=set_imparson)
imparson_slider.pack()

label_waxonator = tk.Label(root, text="Waxonator:")
label_waxonator.pack()
waxonator_slider = tk.Scale(root, from_=0, to=100, orient=tk.HORIZONTAL, command=set_waxonator)
waxonator_slider.pack()

# Create buttons for video selection and playback
play_button = tk.Button(root, text="Play Video", command=play_video)
play_button.pack()

# Reset button
reset_button = tk.Button(root, text="Reset", command=lambda: [imparson_slider.set(0), waxonator_slider.set(0)])
reset_button.pack()

# Create OK and Cancel buttons
ok_button = tk.Button(root, text="OK", command=root.quit)
ok_button.pack()

cancel_button = tk.Button(root, text="Cancel", command=root.quit)
cancel_button.pack()

# Start the main loop
root.mainloop()
