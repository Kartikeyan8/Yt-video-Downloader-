from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from pytube import YouTube
root=Tk()
root.title("Youtube video downloader")
root.geometry("400x500")
#label
Foldername=" "
def openlocation():
    global Foldername
    Foldername=filedialog.askdirectory()
    if(len(Foldername)>1):
        locationerror.config(text=Foldername,fg="green")
    else:
        locationerror.config(text="choose wisely")

def down():
    choice=ytchoice.get()
    url=ytenter.get()
    if(len(url)>1):
        yterror.config(text=" ")
        yt=YouTube(url)

        if(choice==choice[0]):
            select=yt.streams.filter(progressive=True).last()
        elif(choice==choice[1]):
            select=yt.streams.filter(progressive=True,file_extension='mp4')
        elif(choice==choice[2]):
            select=yt.streams.filter(progressive=True,file_extension='hd')
        elif(choice==choice[3]):
            select=yt.streams.filter(progressive=True).first()
    select.download(Foldername)
    yterror.config(text="Download completed")

root.columnconfigure(0,weight=1) #center
ytlabel=Label(root,text="Enter URL")
ytlabel.grid()
#entry
ytenterlink=StringVar()
ytenter=Entry(root,width=60,textvariable=ytenterlink)
ytenter.grid()

#error
yterror=Label(root,text="ERRRR",fg="red")
yterror.grid()
#save label
ytsave=Label(root,text="Save the file")
ytsave.grid()
#save button
savebutton=Button(root,width=20,bg="red",fg="white",text="Choose path",command=openlocation)
savebutton.grid()

#lovation error
locationerror=Label(root,text="errrr",fg='red')
locationerror.grid()

#download quality
qual=Label(root,text="select quality")
qual.grid()

#download button
downbutton=Button(root,text=" Download ",bg="red",command=down)
downbutton.grid()

#choice
choices=["144p","240p","360p","720p"]
ytchoice=ttk.Combobox(root,values=choices)
ytchoice.grid()

label=Label(root,text="Kartikeyan Bhatt")
label.grid()
root.mainloop()