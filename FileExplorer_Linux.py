#Source code from: https://www.geeksforgeeks.org/file-explorer-in-python-using-tkinter/

# Python program to create  
# a file explorer in Tkinter 
   
# import all components 
# from the tkinter library 
from tkinter import *
   
# import filedialog module 
from tkinter import filedialog 

# Function for opening the  
# file explorer window 
       
def explorer():

    def browseFiles(): 
        filename = filedialog.askopenfilename(initialdir = "/", 
                                            title = "Select a File", 
                                            filetypes = (("Text files", 
                                                            "*.txt*"), 
                                                        ("all files", 
                                                            "*.*"))) 
        
        # Change label contents 
        label_file_explorer.configure(text=filename) 
       
                                                                                                   
    # Create the root window 
    window = Tk() 
    
    # Set window title 
    window.title('File Explorer') 
    
    # Set window size 
    window.geometry("500x500") 
    
    #Set window background color 
    window.config(background = "white") 
    
    original_text = "File Explorer using Tkinter"
    # Create a File Explorer label 
    label_file_explorer = Label(window,  
                                text = original_text, 
                                width = 100, height = 4,  
                                fg = "blue") 
    
        
    button_explore = Button(window,  
                            text = "Browse Files", 
                            command = browseFiles)  
    
    button_exit = Button(window,  
                        text = "Exit", 
                        command = exit)  
    
    # Grid method is chosen for placing 
    # the widgets at respective positions  
    # in a table like structure by 
    # specifying rows and columns 
    label_file_explorer.grid(column = 1, row = 1) 
    
    button_explore.grid(column = 1, row = 2) 
    
    button_exit.grid(column = 1,row = 3) 
    
    # Let the window wait for any events 
    new_text = label_file_explorer.cget("text")
    if original_text == new_text:
        print(new_text)
        window.mainloop() 
    else:
        return label_file_explorer.cget("text")
