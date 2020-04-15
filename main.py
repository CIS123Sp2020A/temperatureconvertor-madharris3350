#Madison Harris 
#This GUI -- converts temps in fahrenheit to temps in celsius
import tkinter
import tkinter.messagebox

class FahrenheitConverterGUI:
    def __init__(self):

        #Create the main window
        self.main_window = tkinter.Tk()

        #Create two frames to group widgets
        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        #Create the widgets for the top frame.
        #we need a prompt label and a entry box
        self.prompt_label = tkinter.Label(self.top_frame,
                                          text = 'Enter a temperature in Fahrenheit:')
        self.fahrenheit_entry = tkinter.Entry(self.top_frame,
                                       width = 10)
        
        #Pack the top frame's widgets
        self.prompt_label.pack(side = 'left')
        self.fahrenheit_entry.pack(side = 'left')

        #Create the button widgets for the bottom frame
        self.calc_button = tkinter.Button(self.bottom_frame,
                                          text = 'Convert',
                                          command = self.convert)
        self.quit_button = tkinter.Button(self.bottom_frame,
                                          text = 'Quit',
                                          command = self.main_window.destroy)

        #Pack the buttons
        self.calc_button.pack(side = 'left')
        self.quit_button.pack(side = 'left')

        #Pack the frames
        self.top_frame.pack()
        self.bottom_frame.pack()

        #Enter the tkinter main loop
        tkinter. mainloop()

    #The convert method is a callback function for the Calculate button
    def convert(self):
        #Get the value entered by the user into the fahrenheit_entry widget
        fahrenheit = float(self.fahrenheit_entry.get())

        #Convert fahrenheit to celsius
        celsius = ((fahrenheit -32) * 5) /9

        #Display the results in an info dialog box
        tkinter.messagebox.showinfo('Results',
                                 str(fahrenheit) +
                                 ' Fahrenheit is equal to ' +
                                 str(celsius) + ' Celsius.')


#Create an instance of the FahrenheitConverterGUI class
fahrenheit_conv = FahrenheitConverterGUI()


