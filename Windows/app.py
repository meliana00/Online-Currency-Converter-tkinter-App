from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import tkinter
import api

root = Tk()
root.title('Currency Converter')
root.geometry("600x600")

home = 0
exchange = 0
res = 0

def lock():
    if not amount_entry.get():
        messagebox.showwarning('WARNING', 'Fill out the money amount entry first!')
    else:
        result(home, exchange)

    if amount_entry.get() and not(bool((amount_entry.get()).isdigit())):
        messagebox.showwarning('WARNING', 'Input not valid. \nHint: Please fill out the entry using ONLY digits (0-9).')

def result(from_value, to_value):
    global display_result
    if len(amount_entry.get()) > 0 and bool((amount_entry.get()).isdigit()):
        display_result = round(float(amount_entry.get()) * float(to_value) / float(from_value), 2)
        set_result()

def set_result():
    global res
    res = display_result
    to_label.delete(0, 'end')
    to_label.insert(0, f'{res}')

#Selected Currency By User
def final_(home = None, exchange=None):
    initial_value = home
    final_value = exchange    
    result(initial_value, final_value) 

def initial_(home=None, exchange=None):
    initial_value = home
    final_(initial_value, exchange) 

def from_selected(event):
    global home 
    home = api.data_rates[from_chosen.get()]
    initial_(home, exchange)

def to_selected(event):
    global exchange
    exchange = api.data_rates[to_chosen.get()]
    final_(home, exchange)

#Tabs
note_book = ttk.Notebook(root)
note_book.pack(pady=5)

#Amount Frame
currency_frame = Frame(note_book, width=580, height=580)
currency_frame.pack(fill="both", expand=1)

#From Currency Frame
initial_frame = LabelFrame(currency_frame, text='Conversion')
initial_frame.pack(pady=20, padx=40)

#Add
note_book.add(currency_frame, text='Currencies')

#Money Amount Label
amount = LabelFrame(currency_frame, text='Money Amount')
amount.pack(pady=10)

#Initial Currency Label
from_label = Label(initial_frame, text='From Currency:')
from_label.pack(pady=10)

#Money Amount Entery Box
def on_click(event):
    event.widget.delete(0, tkinter.END)

amount_entry = Entry(amount, font=('Helvetica', 24))
amount_entry.bind("<Button-1>", on_click)
amount_entry.pack(padx=10, pady=10)

#Initial Currency Combobox
initial = tkinter.StringVar()
from_chosen = ttk.Combobox(initial_frame, width=44, textvariable=initial, state='readonly')
from_chosen['values'] = api.brain()
from_chosen.current()
from_chosen.bind("<<ComboboxSelected>>", from_selected)
from_chosen.pack(padx=10, pady=10)

#Final Currency Label
to_label = Label(initial_frame, text='To Currency:')
to_label.pack(pady=10)

#Final Currency Combobox
final = tkinter.StringVar()
to_chosen = ttk.Combobox(initial_frame, width=44, textvariable=final, state='readonly')
to_chosen['values'] = api.brain()
to_chosen.current()
to_chosen.bind("<<ComboboxSelected>>", to_selected)
to_chosen.pack(padx=10, pady=10)

#Button Frame
convert_frame = LabelFrame(currency_frame)
convert_frame.pack(pady=10)

#Convert Button
action = ttk.Button(convert_frame, text="Convert", width=24, command=lock)   
action.pack(padx=1, pady=1)

#If Convert Button is Clicked
def click():
    clicked = False
    action.configure(clicked = True)
    return clicked

#Result Frame
result_frame = LabelFrame(currency_frame, text='Result')
result_frame.pack(pady=20)

#Display Result
to_label = Entry(result_frame, width=20, font=('Helvetica', 20))
to_label.pack(padx=40, pady=40)

root.mainloop()