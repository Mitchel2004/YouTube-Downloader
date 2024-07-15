# Copyright © Mitchel Klijn
# License: Mozilla Public License 2.0 (https://www.mozilla.org/MPL/2.0/)

import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from pytube import YouTube
from mutagen.id3 import ID3, TIT1, TIT2, TIT3, TOAL, TALB, TCOM, TOPE, TPE1, TPE2, TPE3, TPE4, TLAN
import re
import os
import sys
import subprocess

root = tk.Tk()
root.title("YTDL")
root.resizable(0, 0)
root.iconbitmap(sys.executable)
root.attributes("-topmost", True)
root.configure(background="#DCDAD5")

style = ttk.Style(root)
style.theme_use("clam")
style.configure("TLabel", font=("Microsoft Sans Serif", 10))
style.configure("TButton", font=("Microsoft Sans Serif", 10))

fieldContainer = ttk.Frame(root)
fieldContainer.pack(fill="x")

URLLabel = ttk.Label(fieldContainer, text="YouTube URL:").grid(row=0, column=1, sticky="e", pady=(0, 10))
URLVar = tk.StringVar()
URLEntry = ttk.Entry(fieldContainer, textvariable=URLVar, width=64).grid(row=0, column=2, sticky="we", pady=(0, 10))

TIT1TagLabel = ttk.Label(fieldContainer, text="[TIT1]").grid(row=1, column=0, sticky="w", pady=(0, 10))
TIT1Label = ttk.Label(fieldContainer, text="Musical Section:").grid(row=1, column=1, sticky="e", pady=(0, 10))
TIT1Var = tk.StringVar()
TIT1Entry = ttk.Entry(fieldContainer, textvariable=TIT1Var, width=64).grid(row=1, column=2, sticky="we", pady=(0, 10))

TIT2TagLabel = ttk.Label(fieldContainer, text="[TIT2]").grid(row=2, column=0, sticky="w", pady=(0, 10))
TIT2Label = ttk.Label(fieldContainer, text="Title:").grid(row=2, column=1, sticky="e", pady=(0, 10))
TIT2Var = tk.StringVar()
TIT2Entry = ttk.Entry(fieldContainer, textvariable=TIT2Var, width=64).grid(row=2, column=2, sticky="we", pady=(0, 10))

TIT3TagLabel = ttk.Label(fieldContainer, text="[TIT3]").grid(row=3, column=0, sticky="w", pady=(0, 10))
TIT3Label = ttk.Label(fieldContainer, text="Subtitle:").grid(row=3, column=1, sticky="e", pady=(0, 10))
TIT3Var = tk.StringVar()
TIT3Entry = ttk.Entry(fieldContainer, textvariable=TIT3Var, width=64).grid(row=3, column=2, sticky="we", pady=(0, 10))

TOALTagLabel = ttk.Label(fieldContainer, text="[TOAL]").grid(row=4, column=0, sticky="w", pady=(0, 10))
TOALLabel = ttk.Label(fieldContainer, text="Original Album:").grid(row=4, column=1, sticky="e", pady=(0, 10))
TOALVar = tk.StringVar()
TOALEntry = ttk.Entry(fieldContainer, textvariable=TOALVar, width=64).grid(row=4, column=2, sticky="we", pady=(0, 10))

TALBTagLabel = ttk.Label(fieldContainer, text="[TALB]").grid(row=5, column=0, sticky="w", pady=(0, 10))
TALBLabel = ttk.Label(fieldContainer, text="Album:").grid(row=5, column=1, sticky="e", pady=(0, 10))
TALBVar = tk.StringVar()
TALBEntry = ttk.Entry(fieldContainer, textvariable=TALBVar, width=64).grid(row=5, column=2, sticky="we", pady=(0, 10))

TCOMTagLabel = ttk.Label(fieldContainer, text="[TCOM]").grid(row=6, column=0, sticky="w", pady=(0, 10))
TCOMLabel = ttk.Label(fieldContainer, text="Composer(s) (Separate with '/'):").grid(row=6, column=1, sticky="e", pady=(0, 10))
TCOMVar = tk.StringVar()
TCOMEntry = ttk.Entry(fieldContainer, textvariable=TCOMVar, width=64).grid(row=6, column=2, sticky="we", pady=(0, 10))

TOPETagLabel = ttk.Label(fieldContainer, text="[TOPE]").grid(row=7, column=0, sticky="w", pady=(0, 10))
TOPELabel = ttk.Label(fieldContainer, text="Original Artist(s) (Separate with '/'):").grid(row=7, column=1, sticky="e", pady=(0, 10))
TOPEVar = tk.StringVar()
TOPEEntry = ttk.Entry(fieldContainer, textvariable=TOPEVar, width=64).grid(row=7, column=2, sticky="we", pady=(0, 10))

TPE1TagLabel = ttk.Label(fieldContainer, text="[TPE1]").grid(row=8, column=0, sticky="w", pady=(0, 10))
TPE1Label = ttk.Label(fieldContainer, text="Artist(s) (Separate with '/'):").grid(row=8, column=1, sticky="e", pady=(0, 10))
TPE1Var = tk.StringVar()
TPE1Entry = ttk.Entry(fieldContainer, textvariable=TPE1Var, width=64).grid(row=8, column=2, sticky="we", pady=(0, 10))

TPE2TagLabel = ttk.Label(fieldContainer, text="[TPE2]").grid(row=9, column=0, sticky="w", pady=(0, 10))
TPE2Label = ttk.Label(fieldContainer, text="Band/Orchestra:").grid(row=9, column=1, sticky="e", pady=(0, 10))
TPE2Var = tk.StringVar()
TPE2Entry = ttk.Entry(fieldContainer, textvariable=TPE2Var, width=64).grid(row=9, column=2, sticky="we", pady=(0, 10))

TPE3TagLabel = ttk.Label(fieldContainer, text="[TPE3]").grid(row=10, column=0, sticky="w", pady=(0, 10))
TPE3Label = ttk.Label(fieldContainer, text="Conductor:").grid(row=10, column=1, sticky="e", pady=(0, 10))
TPE3Var = tk.StringVar()
TPE3Entry = ttk.Entry(fieldContainer, textvariable=TPE3Var, width=64).grid(row=10, column=2, sticky="we", pady=(0, 10))

TPE4TagLabel = ttk.Label(fieldContainer, text="[TPE4]").grid(row=11, column=0, sticky="w", pady=(0, 10))
TPE4Label = ttk.Label(fieldContainer, text="Remixed/Modified By:").grid(row=11, column=1, sticky="e", pady=(0, 10))
TPE4Var = tk.StringVar()
TPE4Entry = ttk.Entry(fieldContainer, textvariable=TPE4Var, width=64).grid(row=11, column=2, sticky="we", pady=(0, 10))

def BlockEntryInput(entry):
    return re.search(r"^(.*)$", entry) == None

TLANTagLabel = ttk.Label(fieldContainer, text="[TLAN]").grid(row=12, column=0, sticky="w")
TLANLabel = ttk.Label(fieldContainer, text="Language (ISO-639-2):").grid(row=12, column=1, sticky="e")
TLANVar = tk.StringVar()
TLANEntry = ttk.Combobox(fieldContainer, textvariable=TLANVar, validate="key", validatecommand=(root.register(BlockEntryInput), "%P"))
TLANEntry["values"] = ("[und] Undetermined",
                       "[zxx] None",
                       "[mul] Multilingual",
                       "[mis] Miscellaneous",
                       "[art] Artificial",
                       "",
                       "[afr] Afrikaans",
                       "[ara] Arabic",
                       "[bel] Belarusian",
                       "[ben] Bengali",
                       "[bos] Bosnian",
                       "[bul] Bulgarian",
                       "[cat] Catalan",
                       "[ces] Czech",
                       "[cym] Welsh",
                       "[dan] Danish",
                       "[deu] German",
                       "[ell] Greek",
                       "[eng] English",
                       "[est] Estonian",
                       "[fas] Persian",
                       "[fil] Filipino",
                       "[fin] Finnish",
                       "[fra] French",
                       "[fry] Western Frisian",
                       "[gla] Scottish Gaelic",
                       "[gle] Irish",
                       "[gsw] Swiss German",
                       "[haw] Hawaiian",
                       "[heb] Hebrew",
                       "[hin] Hindi",
                       "[hrv] Croatian",
                       "[hun] Hungarian",
                       "[hye] Armenian",
                       "[ind] Indonesian",
                       "[isl] Icelandic",
                       "[ita] Italian",
                       "[jpn] Japanese",
                       "[kat] Georgian",
                       "[kaz] Kazakh",
                       "[kor] Korean",
                       "[lat] Latin",
                       "[lav] Latvian",
                       "[lit] Lithuanian",
                       "[ltz] Luxembourgish",
                       "[mon] Mongolian",
                       "[nld] Dutch",
                       "[nno] Nynorsk Norwegian",
                       "[nob] Bokmål Norwegian",
                       "[pap] Papiamento",
                       "[pol] Polish",
                       "[por] Portuguese",
                       "[roh] Romansh",
                       "[ron] Romanian",
                       "[rus] Russian",
                       "[sco] Scots",
                       "[slk] Slovak",
                       "[slv] Slovenian",
                       "[spa] Spanish",
                       "[sqi] Albanian",
                       "[srp] Serbian",
                       "[swa] Swahili",
                       "[swe] Swedish",
                       "[tha] Thai",
                       "[tur] Turkish",
                       "[ukr] Ukrainian",
                       "[vie] Vietnamese",
                       "[xho] Xhosa",
                       "[yid] Yiddish",
                       "[zho] Chinese",
                       "[zul] Zulu")
TLANEntry.grid(row=12, column=2, sticky="we")
TLANEntry.current(0)

separator = ttk.Separator(fieldContainer).grid(row=13, columnspan=3, sticky="we", padx=10, pady=10)

def BrowseDirectories(event):
    targetDirectoryVar.set(filedialog.askdirectory(initialdir=os.path.sep, mustexist=True))

targetDirectoryLabel = ttk.Label(fieldContainer, text="Target Directory:").grid(row=14, column=0, sticky="e", pady=(0, 10))
targetDirectoryVar = tk.StringVar()
targetDirectoryEntry = ttk.Entry(fieldContainer, textvariable=targetDirectoryVar, validate="key", validatecommand=(root.register(BlockEntryInput), "%P"))
targetDirectoryEntry.grid(row=14, column=1, columnspan=2, sticky="we", pady=(0, 10))
targetDirectoryEntry.bind("<Button-1>", BrowseDirectories)
targetDirectoryEntry.bind("<Key>", BrowseDirectories)

def ResourcePath(relativePath):
    basePath = getattr(sys, "_MEIPASS", os.path.dirname(os.path.abspath(__file__)))

    return os.path.join(basePath, relativePath)

def DownloadAudio():
    try:
        yt = YouTube(URLVar.get())
        stream = yt.streams.filter(only_audio=True).order_by("abr").last()

        root.config(cursor="watch")
        root.update()
        
        title = f"{TIT1Var.get()} {TIT2Var.get()} {TIT3Var.get()}".strip()

        # Check for illegal filename characters in title and replace them
        if title != "" and re.search(r"[\x00-\x1F\x22\x2A\x2F\x3A\x3C\x3E\x3F\x5C\x7C\x7F]", title) != None:
            title = re.sub(r"[\x00-\x1F\x7F]", "", title)

            matches = re.findall(r"[\x22\x2A\x2F\x3A\x3C\x3E\x3F\x5C\x7C]", title)

            for char in matches:
                match char:
                    case "\x22": # "
                        title = title.replace(char, "\x27")
                    case "\x2A": # *
                        title = title.replace(char, "\u2217")
                    case "\x2F": # /
                        title = title.replace(char, "")
                    case "\x3A": # :
                        title = title.replace(char, "\uA789")
                    case "\x3C": # <
                        title = title.replace(char, "\u2039")
                    case "\x3E": # >
                        title = title.replace(char, "\u203A")
                    case "\x3F": # ?
                        title = title.replace(char, "")
                    case "\x5C": # \
                        title = title.replace(char, "")
                    case "\x7C": # |
                        title = title.replace(char, "\u2502")

        title = title.strip()

        artists = [TPE2Var.get(), TPE3Var.get(), TPE4Var.get()]

        artists[:0] = TPE1Var.get().split("/")
        artists[:0] = TCOMVar.get().split("/")

        # Check for illegal filename characters in artist list and replace them
        for i in range(len(artists)):
            artists[i] = artists[i].strip()

            if artists[i] != "" and re.search(r"[\x00-\x1F\x22\x2A\x2F\x3A\x3C\x3E\x3F\x5C\x7C\x7F]", artists[i]) != None:
                artists[i] = re.sub(r"[\x00-\x1F\x7F]", "", artists[i])

                matches = re.findall(r"[\x22\x2A\x2F\x3A\x3C\x3E\x3F\x5C\x7C]", artists[i])

                for char in matches:
                    match char:
                        case "\x22": # "
                            artists[i] = artists[i].replace(char, "\x27")
                        case "\x2A": # *
                            artists[i] = artists[i].replace(char, "\u2217")
                        case "\x2F": # /
                            artists[i] = artists[i].replace(char, "")
                        case "\x3A": # :
                            artists[i] = artists[i].replace(char, "\uA789")
                        case "\x3C": # <
                            artists[i] = artists[i].replace(char, "\u2039")
                        case "\x3E": # >
                            artists[i] = artists[i].replace(char, "\u203A")
                        case "\x3F": # ?
                            artists[i] = artists[i].replace(char, "")
                        case "\x5C": # \
                            artists[i] = artists[i].replace(char, "")
                        case "\x7C": # |
                            artists[i] = artists[i].replace(char, "\u2502")

        artists = list(filter(None, artists))

        while len(artists) > 0:
            if len(artists) == 1:
                artists = artists[0]
                break
            elif len(artists) == 2:
                artists = " & ".join(artists)
                break
            else:
                temp = ", ".join(artists[:2])
                artists.pop(0)
                artists[0] = temp
        else:
            artists = ""
        
        filename = f"{title} \u2013 {artists}".strip()

        # Create mp3 file with FFmpeg and add metadata tags (ID3v2.3)
        if targetDirectoryVar.get() != "" and targetDirectoryVar.get() != "Choose a target directory to save the file in!":
            subprocess.call(f'"{ResourcePath("ffmpeg.exe")}" -y -i "{stream.url}" "{os.path.join(targetDirectoryVar.get(), filename)}.mp3"', shell=True)

            file = ID3(f"{os.path.join(targetDirectoryVar.get(), filename)}.mp3")

            tags = {
                TIT1Var.get(): TIT1,
                TIT2Var.get(): TIT2,
                TIT3Var.get(): TIT3,
                TOALVar.get(): TOAL,
                TALBVar.get(): TALB,
                TCOMVar.get(): TCOM,
                TOPEVar.get(): TOPE,
                TPE1Var.get(): TPE1,
                TPE2Var.get(): TPE2,
                TPE3Var.get(): TPE3,
                TPE4Var.get(): TPE4,
                TLANVar.get()[1:4]: TLAN
            }

            for tagVar, tag in tags.items():
                if tagVar != "":
                    if tag == TCOM or tag == TOPE or tag == TPE1:
                        file.add(tag(encoding=3, text=tagVar.split("/")))
                    else:
                        file.add(tag(encoding=3, text=tagVar))
            
            file.save()

            root.config(cursor="")
            root.update()

            ClearFields()
        else:
            targetDirectoryVar.set("Choose a target directory to save the file in!")

            root.config(cursor="")
            root.update()
    except:
        URLVar.set("Enter a valid YouTube URL!")

        root.config(cursor="")
        root.update()

def ClearFields():
    URLVar.set("")
    TIT1Var.set("")
    TIT2Var.set("")
    TIT3Var.set("")
    TOALVar.set("")
    TALBVar.set("")
    TCOMVar.set("")
    TOPEVar.set("")
    TPE1Var.set("")
    TPE2Var.set("")
    TPE3Var.set("")
    TPE4Var.set("")
    TLANEntry.current(0)

buttonContainer = ttk.Frame(root)
buttonContainer.pack(fill="x")

downloadButton = ttk.Button(buttonContainer, text="Download", command=DownloadAudio).pack(side="left", fill="x", expand=True)
clearButton = ttk.Button(buttonContainer, text="Clear", command=ClearFields).pack(side="right", fill="x", expand=True)

root.mainloop()