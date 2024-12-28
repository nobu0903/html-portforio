import tkinter
import tkinter.messagebox
from PIL import Image, ImageTk

def fuck_you():
  tkinter.messagebox.showinfo('fuck you', message = 'go to hell')
  messagebox.configure(font=("Helvetica", 20), bg="red", fg="white")


def say_helloworld():
  tkinter.messagebox.showinfo(title = 'say', message = 'helloworld')
  messagebox.configure(font=("Helvetica", 20), bg="blue", fg="white")
root = tkinter.Tk()
root.title('Hello World')

root.geometry("1800x1800")
large_font = ("Helvetica, 100")

image_path = 'nakayubi.png'
image = Image.open(image_path)
phto = ImageTk.PhotoImage(image)

label = tkinter.Label(root, image=phto)
label.pack()

button = tkinter.Button(root, text='Click me', command = say_helloworld)
button.pack(pady=100)

button = tkinter.Button(root, text = 'fuck off!', command = fuck_you, font = ('Helvetica', 25))
button.pack(pady=100)

root.mainloop()

