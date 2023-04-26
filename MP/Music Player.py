# Imports tkinter, fnmatch, os, and pygame modules
import tkinter as tk
import fnmatch
import os
from pygame import mixer

# Initializes tkinter window and defines its dimensions, title, and its ability to be resized
player = tk.Tk()
player.geometry("300x400")
player.title("Music Player")
player.resizable(False, False)

# Defines path for songs and its file type. Also initializes the mixer module
path = "C:\songs"
pattern = "*.mp3"
mixer.init()
mixer.music.set_volume(0.1)

# Button Images
play_img = tk.PhotoImage(file="Music-Player\MP\play_img.png")
pause_img = tk.PhotoImage(file="Music-Player\MP\pause_img.png")
skip_img = tk.PhotoImage(file="Music-Player\MP\skip_img.png")
rewind_img = tk.PhotoImage(file="Music-Player/MP/rewind_img.png")
stop_img = tk.PhotoImage(file="Music-Player\MP\stop_img.png")


def play():
    # Plays current selected song
    mixer.music.unpause()
    now_playing.config(text=f"{track_list.get('anchor')}")
    mixer.music.load(path + "//" + track_list.get('anchor'))
    mixer.music.play()


def pause():
    # Pauses and unpauses current song
    if pause_button["text"] == "Pause":
        mixer.music.pause()
        pause_button["text"] = "Play"
    else:
        mixer.music.unpause()
        pause_button["text"] = "Pause"


def stop():
    # Stops playback
    mixer.music.stop()
    now_playing.config(text="Now Playing: Idle")


def next_song():
    # Plays next song
    next_song = track_list.curselection()
    next_song = next_song[0] + 1
    next_song_name = track_list.get(next_song)
    now_playing.config(text=f"Now Playing: {next_song_name}")
    mixer.music.load(path + "//" + track_list.get(next_song))
    mixer.music.play()
    track_list.select_clear(0, "end")
    track_list.activate(next_song)
    track_list.select_set(next_song)


def prev_song():
    # Plays previous song
    prev_song = track_list.curselection()
    prev_song = prev_song[0] - 1
    prev_song_name = track_list.get(prev_song)
    now_playing.config(text=f"Now Playing: {prev_song_name}")
    mixer.music.load(path + "//" + track_list.get(prev_song))
    mixer.music.play()
    track_list.select_clear(0, "end")
    track_list.activate(prev_song)
    track_list.select_set(prev_song)


now_playing = tk.Label(player, text="Now Playing: ",
                       font=("Ariel", 13, "bold"))
now_playing.place(x=0, y=110)

track_list = tk.Listbox(player, bg="#d1c6a7", width=42,
                        height=6, font=("Ariel", 10))
track_list.place(x=1, y=0)

# Gets songs and puts them in the track list
for root, dirs, files in os.walk(path):
    for filename in fnmatch.filter(files, pattern):
        track_list.insert(tk.END, filename)

play_button = tk.Button(player, image=play_img,
                        borderwidth=0, command=play)
play_button.place(x=138, y=200)

pause_button = tk.Button(player, image=pause_img,
                         borderwidth=0, width=30, height=30, command=pause)
pause_button.place(x=195, y=200)

skip_button = tk.Button(player, image=skip_img,
                        borderwidth=0, width=30, height=30, command=next_song)
skip_button.place(x=250, y=200)

rewind_button = tk.Button(player, image=rewind_img,
                          borderwidth=0, width=30, height=30, command=prev_song)
rewind_button.place(x=18, y=200)

stop_button = tk.Button(player, image=stop_img,
                        borderwidth=0, width=20, height=20, command=stop)
stop_button.place(x=80, y=205)

player.mainloop()
