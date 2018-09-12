import math
import tkinter as tk                # python 3
from tkinter import font  as tkfont # python 3
#import Tkinter as tk     # python 2
#import tkFont as tkfont  # python 2

class RvmApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='Arial', size=18, weight="bold")

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, RecyclePage, PurchasePage):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, bg ="lightgreen", text="Please make a selection.", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        button1 = tk.Button(self, text="Recycle",
                            command=lambda: controller.show_frame("RecyclePage"))
        button2 = tk.Button(self, text="Purchase a Drink",
                            command=lambda: controller.show_frame("PurchasePage"))
        button1.pack()
        button2.pack()


class RecyclePage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, bg="lightgreen", text="What would you like to recycle?", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Return to Start Page",
                           command=lambda: controller.show_frame("StartPage"))
        button1 = tk.Button(self, text="Plastic Bottle",
                            command=lambda: controller.show_frame(""))
        button2 = tk.Button(self, text="Aluminum Can",
                            command=lambda: controller.show_frame(""))
        button1.pack()
        button2.pack()
        button.pack()

class PurchasePage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, bg="lightgreen", text="What would you like to purchase?", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Return to Start Page",
                           command=lambda: controller.show_frame("StartPage"))
        button1 = tk.Button(self, text="Bottled Beverage",
                            command=lambda: controller.show_frame(""))
        button2 = tk.Button(self, text="Canned Beverage",
                            command=lambda: controller.show_frame(""))
        button1.pack()
        button2.pack()
        button.pack()

		

if __name__ == "__main__":
	app = RvmApp()
	app.title("Recycling Vending Machine")
	app.geometry("425x150")
	app.mainloop()
    #test anthony