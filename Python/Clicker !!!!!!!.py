# Click Counter
# Demonstrates binding an event with an event handler

from tkinter import *

class Application(Frame):
    """ GUI application whih counts button clicks. """

    
    def __init__(self, master):
        """ Initialize the frame. """
        super(Application, self).__init__(master)
        self.grid()
        self.bttn_clicks = 0 # the number  of buttom clicks
        self.create_widget()


    def create_widget(self):
        """ Create button which displays number of clocks. """
        self.bttn = Button(self)
        self.bttn["text"] = "Total Clicks: 0"
        self.bttn["command"] = self.update_count
        self.bttn.grid()


    def update_count(self):
        """ Incrase click count and display new total. """
        self.bttn_clicks += 1
        self.bttn["text"] = "Total Clicks: " + str(self.bttn_clicks)


# main
root = Tk()
root.title("Click Counter")
root.geometry("1000x520")

app = Application(root)

root.mainloop()
