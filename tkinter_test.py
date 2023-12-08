import tkinter
from tkinter import messagebox

tk = tkinter.Tk()



'''
# My main view

class MainView():
  def __init__(self, tk) -> None:
    # Geometry

    tk.geometry('250x70')
    tk.resizable(False, False) # x axis, y axis

    # Icon

    tk.wm_iconbitmap('data/images/icon.ico')

    # Title

    tk.title('My own GUI')

    # Label

    self.label = tkinter.Label(tk, text = 'Type your name below:', bg = '#f0f0fd')
    self.label.pack()

    # Entry

    self.entry = tkinter.Entry(tk)
    self.entry.pack()

    # Button

    def on_press_button():
      name = self.entry.get()
      if name == '':
        messagebox.showerror('Error', 'Type your name first.')
        return
      messagebox.showinfo('Hello', f'Hello, {name}!')

    self.button = tkinter.Button(tk, text = 'Hello', command = on_press_button)
    self.button.pack()

    tk.bind('<Return>', lambda e: on_press_button())

MainView(tk)
'''



# With frames

'''
# My main view

class MainView():
  def __init__(self, tk) -> None:
    # Geometry

    tk.geometry('250x50')
    tk.resizable(False, False) # x axis, y axis

    # Icon

    tk.wm_iconbitmap('data/images/icon.ico')

    # Title

    tk.title('My own GUI')

    # Frames
    self.frames = []
    self.frames.append(tkinter.Frame(tk)) # Label + Entry
    self.frames.append(tkinter.Frame(tk)) # Button
    for frame in self.frames:
      frame.pack()

    # Label

    self.label = tkinter.Label(self.frames[0], text = 'Type your name:', bg = '#f0f0fd')
    self.label.pack(side = tkinter.LEFT)

    # Entry

    self.entry = tkinter.Entry(self.frames[0])
    self.entry.pack(side = tkinter.LEFT)

    # Button

    def on_press_button():
      name = self.entry.get()
      if name == '':
        messagebox.showerror('Error', 'Type your name first.')
        return
      messagebox.showinfo('Hello', f'Hello, {name}!')

    self.button = tkinter.Button(self.frames[1], text = 'Say hello', command = on_press_button)
    self.button.pack()

    tk.bind('<Return>', lambda e: on_press_button())

MainView(tk)
'''



# With font

'''
# My main view

class MainView():
  def __init__(self, tk) -> None:
    # Geometry

    tk.geometry('250x50')
    tk.resizable(False, False) # x axis, y axis

    # Icon

    tk.wm_iconbitmap('data/images/icon.ico')

    # Title

    tk.title('My own GUI')

    # Font
    self.font_label = ('Consolas', '8')
    self.font_entry = ('Consolas', '8')
    self.font_button = ('Consolas', '8', 'bold')

    # Frames
    self.frames = []
    self.frames.append(tkinter.Frame(tk)) # Label + Entry
    self.frames.append(tkinter.Frame(tk)) # Button
    for frame in self.frames:
      frame.pack()

    # Label

    self.label = tkinter.Label(self.frames[0], text = 'Type your name:', bg = '#f0f0fd', font = self.font_label)
    self.label.pack(side = tkinter.LEFT)

    # Entry

    self.entry = tkinter.Entry(self.frames[0], font = self.font_entry)
    self.entry.pack(side = tkinter.LEFT)

    # Button

    def on_press_button():
      name = self.entry.get()
      if name == '':
        messagebox.showerror('Error', 'Type your name first.')
        return
      messagebox.showinfo('Hello', f'Hello, {name}!')

    self.button = tkinter.Button(self.frames[1], text = 'Say hello', command = on_press_button, font = self.font_button)
    self.button.pack()

    tk.bind('<Return>', lambda e: on_press_button())

MainView(tk)
'''



# With image

'''
# My main view

class MainView():
  def __init__(self, tk) -> None:
    # Geometry

    tk.geometry('250x100')
    tk.resizable(False, False) # x axis, y axis

    # Icon

    tk.wm_iconbitmap('data/images/icon.ico')

    # Title

    tk.title('My own GUI')

    # Font
    self.font_label = ('Consolas', '8')
    self.font_entry = ('Consolas', '8')
    self.font_button = ('Consolas', '8', 'bold')

    # Frames
    self.frames = []
    self.frames.append(tkinter.Frame(tk)) # Image
    self.frames.append(tkinter.Frame(tk)) # Label + Entry
    self.frames.append(tkinter.Frame(tk)) # Button
    for frame in self.frames:
      frame.pack()

    # Image

    logo = tkinter.PhotoImage(file = 'data/images/icon.png')

    self.logo = tkinter.Label(self.frames[0])
    self.logo['image'] = logo
    self.logo.image = logo
    self.logo.pack()

    # Label

    self.label = tkinter.Label(self.frames[1], text = 'Type your name:', bg = '#f0f0fd', font = self.font_label)
    self.label.pack(side = tkinter.LEFT)

    # Entry

    self.entry = tkinter.Entry(self.frames[1], font = self.font_entry)
    self.entry.pack(side = tkinter.LEFT)

    # Button

    def on_press_button():
      name = self.entry.get()
      if name == '':
        messagebox.showerror('Error', 'Type your name first.')
        return
      messagebox.showinfo('Hello', f'Hello, {name}!')

    self.button = tkinter.Button(self.frames[2], text = 'Say hello', command = on_press_button, font = self.font_button)
    self.button.pack()

    tk.bind('<Return>', lambda e: on_press_button())

MainView(tk)
'''



# With Checkbutton

# My main view

'''
class MainView():
  def __init__(self, tk) -> None:
    # Geometry

    tk.geometry('250x120')
    tk.resizable(False, False) # x axis, y axis

    # Icon

    tk.wm_iconbitmap('data/images/icon.ico')

    # Title

    tk.title('My own GUI')

    # Font
    self.font_label = ('Consolas', '8')
    self.font_entry = ('Consolas', '8')
    self.font_checkbutton = ('Consolas', '8')
    self.font_button = ('Consolas', '8', 'bold')

    # Frames
    self.frames = []
    self.frames.append(tkinter.Frame(tk)) # Image
    self.frames.append(tkinter.Frame(tk)) # Label + Entry
    self.frames.append(tkinter.Frame(tk)) # Checkbutton
    self.frames.append(tkinter.Frame(tk)) # Button
    for frame in self.frames:
      frame.pack()

    # Image

    logo = tkinter.PhotoImage(file = 'data/images/icon.png')

    self.logo = tkinter.Label(self.frames[0])
    self.logo['image'] = logo
    self.logo.image = logo
    self.logo.pack()

    # Label

    self.label = tkinter.Label(self.frames[1], text = 'Type your name:', font = self.font_label)
    self.label.pack(side = tkinter.LEFT)

    # Entry

    self.entry = tkinter.Entry(self.frames[1], font = self.font_entry)
    self.entry.pack(side = tkinter.LEFT)

    # Checkbutton

    def on_press_checkbutton():
      print(f'The hello message is going to be in {'upper case' if self.check_button_state.get() == 1 else 'default case'} from now on.')

    self.check_button_state = tkinter.IntVar()
    self.check_button = tkinter.Checkbutton(self.frames[2], text = 'Uppercase', command = on_press_checkbutton, font = self.font_checkbutton, variable = self.check_button_state)
    self.check_button.pack()

    # Button

    def on_press_button():
      name = self.entry.get()
      if name == '':
        messagebox.showerror('Error', 'Type your name first.')
        return
      hello_msg = f'Hello, {name}!'
      messagebox.showinfo('Hello', hello_msg.upper() if self.check_button_state.get() == 1 else hello_msg)

    self.button = tkinter.Button(self.frames[3], text = 'Say hello', command = on_press_button, font = self.font_button, bg = '#f0f0fd')
    self.button.pack()

    tk.bind('<Return>', lambda e: on_press_button())

MainView(tk)
'''



# Start main loop

tk.mainloop()
