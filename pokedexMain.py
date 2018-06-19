import tkinter as tk
import tkinter.ttk as ttk
import DataGathering.WebGrab as gather

bgMainTheme = 'black'
bgFrameTheme = '#B30E00'
bgButtonTheme = '#07BDF7'
#windowStyle = ttk.Style()
#windowStyle.configure('Pokedex.TNotebook', background = bgFrameTheme)

data = gather.Gather()

mainWindow = tk.Tk()
mainWindow.title("Improved Pokedex")
mainWindow.geometry('800x600')
mainWindow['bg'] = bgMainTheme

functionalTabs = ttk.Notebook(mainWindow)

mainFrame = tk.Frame(functionalTabs, background = bgFrameTheme, bd = 0)
movesFrame = tk.Frame(functionalTabs, background = bgFrameTheme, bd = 0)
functionalTabs.add(mainFrame, text = "Pokemon")
functionalTabs.add(movesFrame, text = "Moves")

searchLabel = tk.Label(mainFrame, text = "Enter Pokemon Name: ", background = bgButtonTheme)
searchEntry = tk.Entry(mainFrame)
searchLabel.place(x = 5, y = 2)
searchEntry.place(x = 5 + 130, y = 2)

functionalTabs.pack(fill = "both", expand = True, padx = 10, pady = 10)

searchEntry.bind("<Return>", lambda event: data.dataCheck(searchEntry.get()))

mainWindow.mainloop()