import os
import pygame
from mutagen.id3 import ID3
from ttkthemes import themed_tk as tk
from tkinter import *
from mutagen.mp3 import MP3
from tkinter import filedialog
from tkinter import ttk
from tkinter import messagebox


def Music_Player_GUI(song_dir_path,icon = None):
    global root,listbox,index,count,ctr,MUSIC_END,listofsongs,\
    realnames,statusbar,pausebutton,length,volu

    root = tk.ThemedTk()
    root.get_themes()
    root.set_theme("radiance")
    root.title('MUSIC PLAYER')
    root.configure(background='#000000')

    root.minsize(500, 500)
    root.resizable(0, 0)

    def show_value(val):
        global volu
        try:
            volume_val = round(float(val)) / 50
            dis_val = round(float(val))
            pygame.mixer.music.set_volume(volume_val)
            volu.config(text = "Volume "+str(dis_val),fg = 'white')
        except:
            pass

    ## Init Listbox
    listbox = Listbox(root, selectmode=ACTIVE, width=100, height=20, bg="#1ecf5f", fg="black")
    listbox.pack(fill=X)

    listofsongs = []
    realnames = []

    index = 0
    count = 0
    ctr = 0
    MUSIC_END = 0
    length = Label(root, text="",bg = 'black',fg = 'white', font='Times 14 bold')
    length.pack(side=BOTTOM, fill=X)
    length.place(x=10, y=445)

    le = Label(root, text="Welcome to PyMusic_Player",bg = '#000000',fg='white', font='Times 14 bold')
    le.pack(side=BOTTOM, fill=X)
    le.place(x=417, y=445)

    to_song = Label(root, text="Total number of Songs: 150",bg = '#000000',fg='white', font='Times 14 bold')

    up_song = Label(root,bg = '#000000',fg='white', font='Times 14 bold')

    def on_closing():

        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            pygame.init()
            pygame.mixer.music.stop()
            root.destroy()
    root.protocol("WM_DELETE_WINDOW", on_closing)

    vol = ttk.Scale(root, from_=0, to=100,orient=HORIZONTAL, command=show_value)

    volu = Label(root, text="Volume",bg = '#000000', font='Times 13 bold')
    volu.place(x=845, y=445)

    statusbar = Label(root, text="",bg = '#000000',fg = 'black', relief=SUNKEN, anchor=W, background='#1ecf5f',
                      font='Times 14 bold italic')
    statusbar.pack(side=BOTTOM, fill=X)

    previousbutton_color = Frame(root,borderwidth = 1, background="#1ecf5f")
    previousbutton = Button(previousbutton_color, text="◄◄", bg='#1ecf5f',activebackground = '#1ecf5f',fg = '#000000', width=15, height=2)
    previousbutton.pack(padx=1, pady=1)
    previousbutton_color.pack(side=LEFT)


    addplay_color = Frame(root,borderwidth = 1, background="#1ecf5f")
    addplay = Button(addplay_color, text="Repeat",bg = '#000000',activebackground = '#1ecf5f',fg = 'white', width=15, height=2)
    addplay.pack(padx=1, pady=1)
    addplay_color.pack(side=LEFT)

    play_song_color = Frame(root,borderwidth = 1, background="#1ecf5f")
    play_song = Button(play_song_color, text="Play",bg = '#000000',activebackground = '#1ecf5f',fg = 'white', width=15, height=2)
    play_song.pack(padx=1, pady=1)
    play_song_color.pack(side=LEFT)

    pausebutton_color = Frame(root,borderwidth = 1, background="red")
    pausebutton = Button(pausebutton_color , bg='red', text="║║",  width=15, height=2)
    pausebutton.pack(padx=1, pady=1)
    pausebutton_color.pack(side=LEFT)

    del_button_color = Frame(root,borderwidth = 1, background="#1ecf5f")
    del_button = Button(del_button_color , text="Delete",bg = '#000000',fg = 'white',activebackground = '#1ecf5f', width=15, height=2)
    del_button.pack(padx=1, pady=1)
    del_button_color.pack(side=LEFT)

    add_button_color = Frame(root,borderwidth = 1, background="#1ecf5f")
    add_button = Button(add_button_color, text="Add Song",activebackground = '#1ecf5f',bg = '#000000',fg = 'white', width=15, height=2)
    add_button.pack(padx=1, pady=1)
    add_button_color.pack(side=LEFT)

    nextbutton_color = Frame(root,borderwidth = 1, background="#1ecf5f")
    nextbutton = Button(nextbutton_color, text="►►", bg='#1ecf5f',activebackground = '#1ecf5f',fg = 'black', width=15, height=2)
    nextbutton.pack(padx=1, pady=1)
    nextbutton_color.pack(side=LEFT)


    def pausesong(event):
        global ctr
        ctr += 1
        if (ctr % 2 != 0):
            pygame.mixer.music.pause()
            statusbar['text'] = "Song Pause"
            pausebutton['text'] = '►'

        if (ctr % 2 == 0):
            pygame.mixer.music.unpause()
            try:
                statusbar['text'] = "Playing" + ' - ' + os.path.basename(listofsongs[index])
                pausebutton['text'] = '║║'
            except Exception as e:
                print(e)


    def playsong(event):
        pygame.mixer.music.play()

    def nextsong(event):
        global index,x
        index += 1
        # if (index < count):
        pygame.mixer.music.load(listofsongs[index])
        pygame.mixer.music.play()
        statusbar['text'] = "Playing" + ' - ' + os.path.basename(listofsongs[index])
        audio = MP3(listofsongs[index])
        x = audio.info.length
        mins, secs = divmod(x, 60)
        mins = round(mins)
        secs = round(secs)
        timeformat2 = '{:02d}:{:02d}'.format(mins, secs)
        length['text'] = "Total Length" + ' - ' + timeformat2
        try:
            listbox.itemconfig(index, bg='black',fg='white')
        except:
            pass
        loop_songs()
        upcoming_song()

    def previoussong(event):
        global index,pt
        index -= 1
        pygame.mixer.music.load(listofsongs[index])
        pygame.mixer.music.play()
        statusbar['text'] = "Playing" + ' - ' + os.path.basename(listofsongs[index])
        audio = MP3(listofsongs[index])
        x = audio.info.length
        mins, secs = divmod(x, 60)
        mins = round(mins)
        secs = round(secs)
        timeformat1 = '{:02d}:{:02d}'.format(mins, secs)
        length['text'] = "Total Length" + ' - ' + timeformat1
        ll = len(listofsongs) + index
        try:
            listbox.itemconfig(ll, bg='black',fg='white')
        except:
            listbox.itemconfig(index, bg='black',fg='white')
        loop_songs()
        upcoming_song()

    def loop_songs():
        jo = pygame.mixer.music.get_busy()
        if jo == 0:
            nextsong(jo)
        root.after(100, loop_songs)

    def play_songs():
        global items, timeformat, count
        try:
            # directory = filedialog.askdirectory()
            os.chdir(song_dir_path)
            root.title("Music Player: " + song_dir_path)

            for files in os.listdir(song_dir_path):
                try:
                    if files.endswith(".mp3"):
                        realdir = os.path.realpath(files)
                        audio = ID3(realdir)
                        realnames.append(audio['TIT2'].text[0])
                        listofsongs.append(files)
                except:
                    pass

            listbox.delete(0, END)
            realnames.reverse()
            for items in realnames:
                listbox.insert(0, items)
            for i in listofsongs:
                count = count + 1

            pygame.mixer.init()
            pygame.mixer.music.load(listofsongs[index])
            pygame.mixer.music.play()
            listbox.itemconfig(index, bg='black',fg='white')
            audio = MP3(listofsongs[index])
            x = audio.info.length
            mins, secs = divmod(x, 60)
            mins = round(mins)
            secs = round(secs)
            timeformat = '{:02d}:{:02d}'.format(mins, secs)
            statusbar['text'] = "Playing" + ' - ' + os.path.basename(listofsongs[index])
            length['text'] = "Total Length" + ' - ' + timeformat
            to_song['text'] = 'Total Songs: '+str(len(listofsongs))
            to_song.pack(side=BOTTOM, fill=X)
            to_song.place(x=10, y=365)
            vol.place(x=940, y=450)

            vol.set(80)
            pygame.mixer.music.set_volume(0.8)
            loop_songs()
            upcoming_song()
        except Exception as e:
            print(e)
            length['text'] = 'No Songs Found'

    def del_music(self):
        items = map(int, listbox.curselection())
        for item in items:
            listbox.delete(item)
            listofsongs.pop(item)
        to_song['text'] = 'Total Songs: ' + str(len(listofsongs))
        to_song.pack(side=BOTTOM, fill=X)
        to_song.place(x=10, y=365)

    def play_music(self):
        global MUSIC_END
        items = map(int, listbox.curselection())
        global x,index
        for index in items:
            index = int(index)
            pygame.mixer.init()
            pygame.mixer.music.load(listofsongs[index])
            statusbar['text'] = "Playing" + ' - ' + os.path.basename(listofsongs[index])
            audio = MP3(listofsongs[index])
            x = audio.info.length
            mins, secs = divmod(x, 60)
            mins = round(mins)
            secs = round(secs)
            timeformat1 = '{:02d}:{:02d}'.format(mins, secs)
            length['text'] = "Total Length" + ' - ' + timeformat1
            pygame.mixer.music.play()
            listbox.itemconfig(index, bg='black',fg='white')
        loop_songs()
        upcoming_song()

    def upcoming_song():
        next_song = index+1
        up_song['text'] = 'Next song : '+listofsongs[next_song]
        up_song.pack(side=BOTTOM, fill=X)
        up_song.place(x=350, y=365)

    def add_music(self):
        global filename
        rt = Tk()
        rt.withdraw()
        filename = filedialog.askopenfilename(filetypes=(("Audio file", "*.mp3 *.wav"), ("All files", "*.*")))
        if filename == '':
            pass
        else:
            filen = os.path.basename(filename)
            listofsongs.insert(index, filename)
            listbox.insert(index, filen)
            to_song['text'] = 'Total Songs: '+str(len(listofsongs))
            to_song.pack(side=BOTTOM, fill=X)
            to_song.place(x=10, y=365)
            rt.mainloop()


    play_songs()

    nextbutton.bind("<Button-1>", nextsong)
    addplay.bind("<Button-1>", playsong)
    previousbutton.bind("<Button-1>", previoussong)
    play_song.bind("<Button-1>", play_music)
    pausebutton.bind("<Button-1>", pausesong)
    del_button.bind("<Button-1>", del_music)
    add_button.bind("<Button-1>", add_music)

    root.mainloop()