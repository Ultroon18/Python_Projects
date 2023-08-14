from tkinter import *
from tkinter import ttk
import math

def dark_theme(*args):
    style_frame.configure('main_frame.TFrame', background = "#010924")
    style_label_one.configure('LabelOne.TLabel', background = "#010924", foreground = "white")
    style_label_two.configure('LabelTwo.TLabel', background = "#010924", foreground = "white")
    style_button_numbers.configure('Button_Numbers.TButton', background = "#00044A", foreground = "white")
    style_button_numbers.map('Button_Numbers.TButton', background = [('active', '#020A90')])
    style_button_delete.configure('ButtonDelete.TButton', background = "#010924", foreground = "white")
    style_button_delete.map('ButtonDelete.TButton', background = [('active', '#000AB1')])
    style_button_others.configure('ButtonOthers.TButton', background = "#010924", foreground = "white")
    style_button_others.map('ButtonOthers.TButton', background = [('active', '#000AB1')])

def clear_theme(*args):
    style_frame.configure('main_frame.TFrame', background = "#DBDBDB", foreground = "black")
    style_label_one.configure('LabelOne.TLabel', background = "#DBDBDB", foreground = "black")
    style_label_two.configure('LabelTwo.TLabel', background = "#DBDBDB", foreground = "black")
    style_button_numbers.configure('Button_Numbers.TButton', background = "#FFFFFF", foreground = "black")
    style_button_numbers.map('Button_Numbers.TButton', background = [('active', '#B9B9B9')])
    style_button_delete.configure('ButtonDelete.TButton', background = "#CECECE", foreground = "black")
    style_button_delete.map('ButtonDelete.TButton', foreground = [('active', '#FF0000')], background = [('active', '#858585')])
    style_button_others.configure('ButtonOthers.TButton', background = "#CECECE", foreground = "black")
    style_button_others.map('ButtonOthers.TButton', background = [('active', '#858585')])


def read_text(valor):
    if valor >= '0' and valor <= '9' or valor == '(' or valor == ')' or valor == '.':
        text_two.set(text_two.get() + valor)
    if valor == '/' or valor == '*' or valor == '+' or valor == '-':
        if valor == '/':
            text_one.set(text_two.get() + '/')
        elif valor == '*':
            text_one.set(text_two.get() + '*')
        elif valor == '+':
            text_one.set(text_two.get() + '+')
        elif valor == '-':
            text_one.set(text_two.get() + '-')
        text_two.set('')
    

def operation(*args):
    text_one.set(text_one.get() + text_two.get())
    operacion = eval(text_one.get())
    text_two.set(operacion)

def read_text_keyboard(event):
    valor = event.char
    if valor >= '0' and valor <= '9' or valor == '(' or valor == ')' or valor == '.':
        text_two.set(text_two.get() + valor)
    if valor == '/' or valor == '*' or valor == '+' or valor == '-':
        if valor == '/':
            text_one.set(text_two.get() + '/')
        elif valor == '*':
            text_one.set(text_two.get() + '*')
        elif valor == '+':
            text_one.set(text_two.get() + '+')
        elif valor == '-':
            text_one.set(text_two.get() + '-')
        text_two.set('')

def sqrt_text(valor):
    if text_two.get() < '0' and text_two.get() != '':
        text_one.set('Math ERROR')
    elif text_two.get() >= '0':
        auxiliar = text_two.get()
        operacion = math.sqrt(float(text_two.get()))
        text_one.set(valor + auxiliar)
        text_two.set(operacion)

def delete(*args):
    start = 0
    final = len(text_two.get())
    text_two.set(text_two.get()[start:final - 1])

def delete_all(*args):
    text_one.set('')
    text_two.set('')

window = Tk()
window.title("Calculadora")
window.geometry("+500+500")
window.columnconfigure(0, weight = 1)
window.rowconfigure(0, weight = 1)

#ESTILOS
#ESTILOS DEL FRAME
style_frame = ttk.Style()
style_frame.configure('main_frame.TFrame', background = "#DBDBDB")
style_frame.theme_use('clam')
#ESTILOS DE LABEL
style_label_one = ttk.Style()
style_label_one.configure('LabelOne.TLabel', font = "Arial 20", anchor = "e")
style_label_two = ttk.Style()
style_label_two.configure('LabelTwo.TLabel', font = "Arial 40", anchor = "e")
#ESTILOS PARA LOS BOTONES 0 - 9
style_button_numbers = ttk.Style()
style_button_numbers.configure('Button_Numbers.TButton', font = "Arial 16", width = 5, background = "#FFFFFF", relief = "flat")
style_button_numbers.map('Button_Numbers.TButton', background = [('active', '#B9B9B9')])
#ESTILO BOTONES BORRAR
style_button_delete = ttk.Style()
style_button_delete.configure('ButtonDelete.TButton', font = "Arial 16", width = 5, background = "#CECECE", relief = "flat")
style_button_delete.map('ButtonDelete.TButton', foreground = [('active', '#FF0000')], background = [('active', '#858585')])
#ESTILOS BOTONES PARENTESIS, OPERACIONES E IGUAL
style_button_others = ttk.Style()
style_button_others.configure('ButtonOthers.TButton', font = "Arial 16", width = 5, background = "#CECECE", relief = "flat")
style_button_others.map('ButtonOthers.TButton', background = [('active', '#858585')])

#Este frame va a estar contenido en nuestra raiz "window"
main_frame = ttk.Frame(window, style = "main_frame.TFrame")
main_frame.grid(row = 0, column = 0, sticky = (W, N, E, S))
main_frame.columnconfigure(0, weight = 1)
main_frame.columnconfigure(1, weight = 1)
main_frame.columnconfigure(2, weight = 1)
main_frame.columnconfigure(3, weight = 1)
main_frame.rowconfigure(0, weight = 1)
main_frame.rowconfigure(1, weight = 1)
main_frame.rowconfigure(2, weight = 1)
main_frame.rowconfigure(3, weight = 1)
main_frame.rowconfigure(4, weight = 1)
main_frame.rowconfigure(5, weight = 1)
main_frame.rowconfigure(6, weight = 1)
main_frame.rowconfigure(7, weight = 1)

text_one = StringVar()
text_enter_one = ttk.Label(main_frame, textvariable = text_one, style = "LabelOne.TLabel")

#POSICION (0,0) EN EL main_frame NO EN window
text_enter_one.grid(row = 0, column = 0, columnspan = 4, sticky = (W, N, E, S))

text_two = StringVar()
text_enter_two = ttk.Label(main_frame, textvariable = text_two, style = "LabelTwo.TLabel")

text_enter_two.grid(row = 1, column = 0, columnspan = 4, sticky = (W, N, E, S))

#CREACION DE BOTONES
#DIGITOS DEL 0 - 9
boton0 = ttk.Button(main_frame, text = "0", style = "Button_Numbers.TButton", command = lambda: read_text('0'))
boton1 = ttk.Button(main_frame, text = "1", style = "Button_Numbers.TButton", command = lambda: read_text('1'))
boton2 = ttk.Button(main_frame, text = "2", style = "Button_Numbers.TButton", command = lambda: read_text('2'))
boton3 = ttk.Button(main_frame, text = "3", style = "Button_Numbers.TButton", command = lambda: read_text('3'))
boton4 = ttk.Button(main_frame, text = "4", style = "Button_Numbers.TButton", command = lambda: read_text('4'))
boton5 = ttk.Button(main_frame, text = "5", style = "Button_Numbers.TButton", command = lambda: read_text('5'))
boton6 = ttk.Button(main_frame, text = "6", style = "Button_Numbers.TButton", command = lambda: read_text('6'))
boton7 = ttk.Button(main_frame, text = "7", style = "Button_Numbers.TButton", command = lambda: read_text('7'))
boton8 = ttk.Button(main_frame, text = "8", style = "Button_Numbers.TButton", command = lambda: read_text('8'))
boton9 = ttk.Button(main_frame, text = "9", style = "Button_Numbers.TButton", command = lambda: read_text('9'))

#BOTONES ESPECIALES
boton_delete = ttk.Button(main_frame, text = chr(9003), style = "ButtonDelete.TButton", command = lambda: delete())
boton_delete_all = ttk.Button(main_frame, text="C", style = "ButtonDelete.TButton", command = lambda: delete_all())
boton_parentesis_on = ttk.Button(main_frame, text="(", style = "ButtonOthers.TButton", command = lambda: read_text('('))
boton_parentesis_off = ttk.Button(main_frame, text=")", style = "ButtonOthers.TButton", command = lambda: read_text(')'))
boton_punto = ttk.Button(main_frame, text="·", style = "ButtonOthers.TButton", command = lambda: read_text('.'))
boton_igual = ttk.Button(main_frame, text="=", style = "ButtonOthers.TButton", command = lambda: operation())

#BOTONES OPERACIONES
boton_div = ttk.Button(main_frame, text=chr(247), style = "ButtonOthers.TButton", command = lambda: read_text('/'))
boton_mult = ttk.Button(main_frame, text="*", style = "ButtonOthers.TButton", command = lambda: read_text('*'))
boton_suma = ttk.Button(main_frame, text="+", style = "ButtonOthers.TButton", command = lambda: read_text('+'))
boton_resta = ttk.Button(main_frame, text="-", style = "ButtonOthers.TButton", command = lambda: read_text('-'))
boton_sqrt = ttk.Button(main_frame, text="√", style = "ButtonOthers.TButton", command = lambda: sqrt_text('√'))

#VISUALIZAR BOTONES EN PANTALLA
boton_parentesis_on.grid(row = 2, column = 0, sticky = (W, N, E, S))
boton_parentesis_off.grid(row = 2, column = 1, sticky = (W, N, E, S))
boton_delete_all.grid(row = 2, column = 2, sticky = (W, N, E, S))
boton_delete.grid(row = 2, column = 3, sticky = (W, N, E, S))
boton7.grid(row = 3, column = 0, sticky = (W, N, E, S))
boton8.grid(row = 3, column = 1, sticky = (W, N, E, S))
boton9.grid(row = 3, column = 2, sticky = (W, N, E, S))
boton_div.grid(row = 3, column = 3, sticky = (W, N, E, S))
boton4.grid(row = 4, column = 0, sticky = (W, N, E, S))
boton5.grid(row = 4, column = 1, sticky = (W, N, E, S))
boton6.grid(row = 4, column = 2, sticky = (W, N, E, S))
boton_mult.grid(row = 4, column = 3, sticky = (W, N, E, S))
boton1.grid(row = 5, column = 0, sticky = (W, N, E, S))
boton2.grid(row = 5, column = 1, sticky = (W, N, E, S))
boton3.grid(row = 5, column = 2, sticky = (W, N, E, S))
boton_suma.grid(row = 5, column = 3, sticky = (W, N, E, S))
boton0.grid(row = 6, column = 0, columnspan = 2, sticky = (W, N, E, S))
boton_punto.grid(row = 6, column = 2, sticky = (W, N, E, S))
boton_resta.grid(row = 6, column = 3, sticky = (W, N, E, S))
boton_igual.grid(row = 7, column = 0, columnspan = 3, sticky = (W, N, E, S))
boton_sqrt.grid(row = 7, column = 3, sticky = (W, N, E, S))

for child in main_frame.winfo_children():
    child.grid_configure(ipady = 10, padx = 1, pady = 1)


window.bind('<KeyPress-o>', dark_theme)
window.bind('<KeyPress-c>', clear_theme)
window.bind('<Key>', read_text_keyboard)
window.bind('<KeyPress-BackSpace>', delete)
window.bind('<KeyPress-Escape>', delete_all)
window.bind('<KeyPress-Return>', operation)
window.mainloop()