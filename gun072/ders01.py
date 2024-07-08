from tkinter import *
def yazdir():
    print("buton tıklandı")

pencere = Tk()
pencere.geometry('400x300')
pencere.title("BTK Akademi Python Kursu")
buton1 = Button(text="Buton Bir", fg="red", bg="blue", command=yazdir)
buton2 = Button(text="Buton iki", fg="red", bg="blue")
buton3 = Button(text="Buton uc", fg="red", bg="blue")

buton1.pack(side=LEFT)
buton2.pack()
buton3.pack(side=RIGHT)

yazi = Label(pencere, text="Merhaba BTK Öğrencileri", font=("Arial",25))
yazi.pack()



pencere.mainloop()