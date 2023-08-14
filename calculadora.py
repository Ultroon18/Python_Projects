from tkinter import *
window = Tk()
window.title("Calculadora")

i = 0

#Entrada de de texto para los calculos
text_enter = Entry(window, font=("Consolas 20"))
text_enter.grid(row = 0, column = 0, columnspan = 4, padx = 10, pady = 10)

#FUNCIONES
def click_tecla(valor):
    global i
    text_enter.insert(i, valor)
    i += 1

def delete_text():
    text_enter.delete(0, END)

def operacion():
    expresion = text_enter.get()
    operacion = eval(expresion)
    text_enter.delete(0, END)
    text_enter.insert(0, operacion)

#Creacion de Botones
#DIGITOS 0 - 9
tecla0 = Button(window, text="0", width = 16, height = 2, command = lambda: click_tecla(0))
tecla1 = Button(window, text="1", width = 5, height = 2, command = lambda: click_tecla(1))
tecla2 = Button(window, text="2", width = 5, height = 2, command = lambda: click_tecla(2))
tecla3 = Button(window, text="3", width = 5, height = 2, command = lambda: click_tecla(3))
tecla4 = Button(window, text="4", width = 5, height = 2, command = lambda: click_tecla(4))
tecla5 = Button(window, text="5", width = 5, height = 2, command = lambda: click_tecla(5))
tecla6 = Button(window, text="6", width = 5, height = 2, command = lambda: click_tecla(6))
tecla7 = Button(window, text="7", width = 5, height = 2, command = lambda: click_tecla(7))
tecla8 = Button(window, text="8", width = 5, height = 2, command = lambda: click_tecla(8))
tecla9 = Button(window, text="9", width = 5, height = 2, command = lambda: click_tecla(9))

#TECLAS ESPECIALES
tecla_AC = Button(window, text="AC", width = 5, height = 2, command = lambda: delete_text())
tecla_parentesis_abre = Button(window, text="(", width = 5, height = 2, command = lambda: click_tecla("("))
tecla_parentesis_cierra = Button(window, text=")", width = 5, height = 2, command = lambda: click_tecla(")"))
tecla_punto = Button(window, text="·", width = 5, height = 2, command = lambda: click_tecla("."))
tecla_igual = Button(window, text="=", width = 5, height = 2, command = lambda: operacion())

#TECLAS OPERACIONES ARITMETICAS
tecla_div = Button(window, text="/", width = 5, height = 2, command = lambda: click_tecla("/"))
tecla_mult = Button(window, text="*", width = 5, height = 2, command = lambda: click_tecla("*"))
tecla_suma = Button(window, text="+", width = 5, height = 2, command = lambda: click_tecla("+"))
tecla_resta = Button(window, text="-", width = 5, height = 2, command = lambda: click_tecla("-"))

#VISUALIZAR BOTONES EN PANTALLA
tecla_AC.grid(row = 1, column = 0, padx = 10, pady = 10)
tecla_parentesis_abre.grid(row = 1, column = 1, padx = 10, pady = 10)
tecla_parentesis_cierra.grid(row = 1, column = 2, padx = 10, pady = 10)
tecla_div.grid(row = 1, column = 3, padx = 10, pady = 10)

tecla7.grid(row = 2, column = 0, padx = 10, pady = 10)
tecla8.grid(row = 2, column = 1, padx = 10, pady = 10)
tecla9.grid(row = 2, column = 2, padx = 10, pady = 10)
tecla_mult.grid(row = 2, column = 3, padx = 10, pady = 10)

tecla4.grid(row = 3, column = 0, padx = 10, pady = 10)
tecla5.grid(row = 3, column = 1, padx = 10, pady = 10)
tecla6.grid(row = 3, column = 2, padx = 10, pady = 10)
tecla_suma.grid(row = 3, column = 3, padx = 10, pady = 10)

tecla1.grid(row = 4, column = 0, padx = 10, pady = 10)
tecla2.grid(row = 4, column = 1, padx = 10, pady = 10)
tecla3.grid(row = 4, column = 2, padx = 10, pady = 10)
tecla_resta.grid(row = 4, column = 3, padx = 10, pady = 10)

tecla0.grid(row = 5, column = 0, columnspan = 2, padx = 10, pady = 10)
tecla_punto.grid(row = 5, column = 2, padx = 10, pady = 10)
tecla_igual.grid(row = 5, column = 3, padx = 10, pady = 10)




window.mainloop()