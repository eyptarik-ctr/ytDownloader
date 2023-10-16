from pytube import YouTube
from tkinter import*
# window
main_window = Tk()
main_window.title("YOUTUBE DOWNLOADER")
main_window.minsize(height=150,width=400)
#label
label1 = Label(text="WELCOME TO YTDOWNLADER",bg="#000000",fg="#FFFFFF")
label1.pack()
#label2
label2 = Label(text="ENTER LİNK : ")
label2.pack()
# get value
def link_entered():

    link = str(link1.get())

    def downloader(link):
        video = YouTube(link)
        video = video.streams.get_highest_resolution()
        try:
            video.download()
        except:

            print("erorr!!! video hasn't been downloaded")
        print("Downloaad complated sucesfuly")

    downloader(link)

# entry
link1 = Entry()
link1.pack()

#button
buton1 = Button(text="DOWNLOAD",command=link_entered,bg="#000000",fg="#FFFFFF")
buton1.pack()
buton1.config(width=30,height=2)


main_window.mainloop()
# downloader
