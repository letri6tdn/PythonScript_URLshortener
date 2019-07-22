from tkinter import *

def show_instruction(root):
    
    f_root = Frame(root)
    instruction = Label(f_root, text = "Welcome to URL Shortener! Please paste your URL down below.", font=(14), anchor = N)
    f_root.pack()
    instruction.pack()
    
def show_copyright(root):
    
    f_root = Frame(root)
    copyright_note = Label(f_root, text = "\u00A9 2019 xyz.me", width = 700, height=200,  anchor = SE)
    f_root.pack()
    copyright_note.pack()    
    
def callback():
    print(url_entry.get())

    
 

if __name__ == '__main__':
    root = Tk()
    root.title("URL Shortener")
    
    show_instruction(root)
    
    #------------------------------------------------------------------------#
    # Create URL entry box here
    f_root = Frame(root)
    url_string = StringVar()
    url_entry = Entry(root, width = 100, text=url_string)
    url_entry.pack()
    url_entry.focus_set()
    
    #
    submit_button = Button(f_root, text = "Submit", command=callback)
    f_root.pack()
    submit_button.pack()    
    
    
    show_copyright(root)
    
    root.geometry("700x200")
    root.mainloop()
    