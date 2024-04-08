# Music player Made with Tkinter GUI from python 


from tkinter import *
from tkinter import filedialog
from pygame import mixer
from PIL import Image,ImageTk
import os


root=Tk()
root.resizable(False,False)
root.geometry("1180x730")
root.title("Music Player")

mixer.init()
def open_folder():
    path=filedialog.askdirectory()
    if path:
        os.chdir(path)
        songs=os.listdir(path)
        for song in songs:
            if song.endswith(".mp3"):
                playlist.insert(END,song)

def play_song():
    music_name=playlist.get(ACTIVE)
    mixer.music.load(playlist.get(ACTIVE))
    mixer.music.play()
    music_name.config(text=music_name[1:-4])
    
root.overrideredirect()
icon = "icon.ico"
root.wm_iconbitmap(icon)

image = Image.open("music player.png") 
photo1 = ImageTk.PhotoImage(image)
bg_img = Label(root, image=photo1)
bg_img.place(x=0, y=0, relwidth=1, relheight=1)

play_icon=Image.open("play.png")
photo2 = ImageTk.PhotoImage(play_icon)
Button(root,image=photo2,border="0",command=play_song).place(x=150,y=420)

resume_icon=Image.open("resume.png")
photo4 = ImageTk.PhotoImage(resume_icon)
Button(root,image=photo4,border="0",bg="#D9D9D9",command=mixer.music.unpause).place(x=200,y=530)

pause_icon=Image.open("pause.png")
photo3 = ImageTk.PhotoImage(pause_icon)
Button(root,image=photo3,border="0",bg="#D9D9D9",command=mixer.music.pause).place(x=90,y=530)

music_frame=Frame(root,bd=2,relief=RAISED)
music_frame.place(x=500,y=350,width=580,height=330)

Button(root,text="Open Folder",width=15,height=2,font="bold 10",command=open_folder).place(x=520,y=290)

scroll=Scrollbar(music_frame)
playlist=Listbox(music_frame,width=100,cursor="hand2",bd=0,yscrollcommand=scroll.set)
scroll.config(command=playlist.yview)
scroll.pack(side=RIGHT,fill=Y)
playlist.pack(side=LEFT,fill=BOTH)

root.mainloop()
