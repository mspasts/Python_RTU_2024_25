import tkinter as tk # this is in standard library - it comes with python


class Application(tk.Frame): # we inherit from tk.Frame
    count = 5
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        # finally we call our own method to create widgets
        self.create_widgets()
        self.create_menu()

    # let's create a method to add file menu
    def create_menu(self):
        # create menu object
        self.menu = tk.Menu(self.master)
        # add menu to master window
        self.master.config(menu=self.menu)
        # create file menu
        self.filemenu = tk.Menu(self.menu)
        # add file menu to menu
        self.menu.add_cascade(label="File", menu=self.filemenu)
        # add menu items
        self.filemenu.add_command(label="New", command=self.new_file)
        self.filemenu.add_command(label="Open...", command=self.open_file)
        self.filemenu.add_separator()
        self.filemenu.add_command(label="Exit", command=self.master.quit)

    def new_file(self):
        print("New file")
        # TODO actually create new file

    def open_file(self):
        print("Open file")
        # TODO actually open file


    def create_widgets(self):
        # so I create hi_there button which is object created from tk.Button class
        self.hi_there = tk.Button(self)
        # following you need to know exact methods and properties of tk.Button
        # documentation: https://docs.python.org/3/library/tkinter.html#button
        self.hi_there["text"] = "Hello World\n(click me)"
        # next part we bind the button to method say_hi
        # note there are no brackets after say_hi!
        self.hi_there["command"] = self.say_hi #binding say_hi method to click
        # so we take advantage of fact that function is first class object in python
        # we can use variable to store reference to function
        self.hi_there.pack(side="top") # we place the button on top of the window

        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit.pack(side="bottom")
        self.result = tk.Label(self)
        self.result["text"] = f"Result {self.count}"
        self.result.pack(side="bottom")

    def say_hi(self):
        print("hi there, everyone!")
        self.count += 1
        self.result["text"] = f"Result {self.count}" # hand made binding of hi button and result label


root = tk.Tk()
app = Application(master=root)
app.mainloop()
