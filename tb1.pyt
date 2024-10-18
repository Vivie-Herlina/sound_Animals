import tkinter as tk
from tkinter import ttk, Label
from PIL import Image, ImageTk
from gtts import gTTS
import pygame
import os

# Data hewan
pygame.init()
viewval1 = False
viewval2 = False
hewan = {
    1: {
        "nama_hewan": "COW",
        "gambar_hewan": "FotoHewan/Cow.jpg",
    },
    2: {
        "nama_hewan": "FROG",
        "gambar_hewan": "FotoHewan/Frog.jpg",
    },
    3: {
        "nama_hewan": "GOAT",
        "gambar_hewan": "FotoHewan/Goat.jpeg",
    },
    4: {
        "nama_hewan": "LION",
        "gambar_hewan": "FotoHewan/Lion.jpg",
    },
    5: {
        "nama_hewan": "MONKEY",
        "gambar_hewan": "FotoHewan/Monkey.jpg",
    },
    6: {
        "nama_hewan": "WOLF",
        "gambar_hewan": "FotoHewan/Wolf.png",
    },
}
warna = {
    1: {
        "nama_gambar": "Black",
        "gambar_gambar": "warna/black.jpg",
    },
    2: {
        "nama_gambar": "Blue",
        "gambar_gambar": "warna/blue.png",
    },
    3: {
        "nama_gambar": "Red",
        "gambar_gambar": "warna/red.jpg",
    },
    4: {
        "nama_gambar": "Purple",
        "gambar_gambar": "warna/ungu.png",
    },
    5: {
        "nama_gambar": "Yellow",
        "gambar_gambar": "warna/yellow.png",
    }
}


def tampilview(event):
    global viewval1
    global viewval2
    if menuselected.get() == "Animals":
        if viewval1 == False:
            tampilAnimals()
            viewval1 = True
        elif viewval1 == True:
            pass
    elif menuselected.get() == "Color":
        if viewval2 == False:
            tampilColor()
            viewval2 = True
        elif viewval2 == True:
            pass


def createVoice(name_file, text):
    audio_path =  name_file + '.mp3'
    if not os.path.isfile(audio_path):
        say = gTTS(text=text, lang='en')
        say.save(audio_path)


def Playvoice(name_of_file, direc=""):
    pygame.mixer.init()
    pygame.mixer.music.load(direc+name_of_file + '.mp3')
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(5)


def eventani(hewan_id):
        createVoice(hewan_id, hewan_id)
        Playvoice(hewan_id)
        test=Playvoice(hewan_id, "hewansuara/")
        

def evengambar(gambar_id):
    createVoice(gambar_id, gambar_id)
    Playvoice(gambar_id)


def tampilAnimals():
    tampilhewan = ttk.Frame(window)
    for i in range(1, len(hewan) + 1):
        image = Image.open(hewan[i]['gambar_hewan'])
        photo = ImageTk.PhotoImage(image)
        resized_image = image.resize((150, 150))
        photo = ImageTk.PhotoImage(resized_image)
        image_label = Label(tampilhewan, image=photo, padx=50, pady=50)
        image_label.photo = photo
        image_label.bind('<Button-1>', lambda event,
                         hewan_id=hewan[i]['nama_hewan']: eventani(hewan_id))
        image_label.pack(side=tk.LEFT)
    tampilhewan.pack(padx=10,pady=10)


def tampilColor():
    tampilgambar = ttk.Frame(window)
    for i in range(1, len(warna) + 1):
        image = Image.open(warna[i]['gambar_gambar'])
        photo = ImageTk.PhotoImage(image)
        resized_image = image.resize((200, 200))
        photo = ImageTk.PhotoImage(resized_image)
        image_label = Label(tampilgambar, image=photo,padx=10,pady=10)
        image_label.photo = photo
        image_label.bind('<Button-1>', lambda event,
                         gambar_id=warna[i]['nama_gambar']: evengambar(gambar_id))
        image_label.pack(side=tk.LEFT)
    tampilgambar.pack(padx=10,pady=10)


window = tk.Tk()
window.geometry('800x600')
window.title("Tugas Besar 1")

Kelompok = ttk.Frame(window)
label = Label(Kelompok, text='Kelompok 10')
label.pack()
Kelompok.pack()

menu = ttk.Frame(window,width=10,height=10,padding=5)
label = Label(menu, text='Pilih menu:')
label.pack()
option_menu = ["Animals", "Color"]
menuselected = tk.StringVar(window)
option_menus = ttk.OptionMenu(
    menu,
    menuselected,
    option_menu[0],
    *option_menu,
    command=tampilview)
menu.pack()
option_menus.pack(side="top",fill="x")
window.configure(background="grey") 
# yellow bisa di ganti ke warna yang lainn
window.mainloop()
