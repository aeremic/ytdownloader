import os
from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
from pytube import YouTube

#os.chdir("C:\\Users\\Andrija\\Documents\\python\\ytdownloader")
iconpath = os.getcwd() + "\\media\\down-arrow.png"
desktoppath = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop') 
os.chdir(desktoppath)
if not os.path.exists('Downloaded Videos'):
    os.makedirs('Downloaded Videos')
os.chdir("./Downloaded Videos")

def do_popup(event):
    try:
        w = event.widget
        m.entryconfig("Paste", command=lambda: w.event_generate("<<Paste>>"))
        m.tk_popup(event.x_root, event.y_root)
    finally:
        m.grab_release()
def download(input, checkValue):
    yt = YouTube(input)
    print("Title of video: " + str(yt.title))
    print("Video downloading...")
    if(checkValue.get() == 1):
        streamList = yt.streams.filter(only_audio=True).all()
        stream = streamList[0]
    else:    
        stream = yt.streams.get_highest_resolution()
    stream.download()
    print("Video downloaded.")
    messagebox.showinfo("Youtube Downloader","Video successfully downloaded")

root = Tk()
root.title("Youtube Downloader")
root.resizable(False, False)
photo = PhotoImage(file = iconpath)
root.iconphoto(False, photo)
root.geometry("317x75")

m = Menu(root, tearoff=0)
m.add_command(label="Paste")

Label(root, text="Enter a link: ").grid(row=0)
input = Entry(root, width=40)
input.bind("<Button-3>", do_popup)
input.grid(row=0, column=1)
checkValue = IntVar()
Checkbutton(root, text = "Audio only", variable = checkValue).grid(row=2, columnspan=2)
Button(root, text="Download", command= lambda: [download(input.get(), checkValue)]).grid(row=3, columnspan=2)

root.mainloop()
