import tkinter as tk 
from tkinter import messagebox
import random
import string 
import pyperclip

#cree la funcion para generar la fortaleza de la contraseña 
def evaluar_fortaleza(contraseña): 
    if len(contraseña) <8:
        return "Debil"
    elif len(contraseña) < 12:
        return "fuerte" 
    #verifica si tiene letras mayuscculas, minusculas y numeros y simbolos 
    if (any(c.islower() for c in contraseña) and 
        any(c.isupper() for c in contraseña) and 
        any(c.isdigit() for c in contraseña) and 
        any(c in string.punctuation for c in contraseña)):
       return "fuerte"
    else: 
        return "medio"
    return "fuerte" 
# Crear la entrada para mostrar el resultado
entrada_resultado = tk.Entry()

# Crear la etiqueta para mostrar la fortaleza de la contraseña
label_fortaleza = tk.Label(text="Fortaleza: ")
label_fortaleza.pack()

# Crear el slider para la longitud de la contraseña
slider_longitud = tk.Scale(from_=8, to=12, orient=tk.HORIZONTAL, label="Longitud")
slider_longitud.set(10)  # Valor predeterminado

# Crear variables para las opciones de generación de contraseña
var_mayus = tk.BooleanVar()
var_minus = tk.BooleanVar()
var_numeros = tk.BooleanVar()
var_simbolos = tk.BooleanVar()

#generador de contraseña 
def generar_contraseña():
    longitud = int(slider_longitud.get())
    if longitud <8 or longitud >12: 
        messagebox.showerror("error", "la contraseña debe tener entre 8 y 12 caracteres.")
        return
    caracteres = ""
    if var_mayus.get():
        caracteres += string.ascii_uppercase
    if var_minus.get():
        caracteres += string.ascii_lowercase
    if var_numeros.get():
        caracteres += string.digits
    if var_simbolos.get(): 
        caracteres += string.punctuation
        
    if not caracteres:
        messagebox.showerror("advertencia", "selecciona una opcion valida")
        return
    contraseña= ''.join(random.choice(caracteres) for _ in range(longitud))
    entrada_resultado.delete(0, tk.END)
    entrada_resultado.insert(0, contraseña)
    #evaluar la fortaleza de la contraseña 
    fortaleza=evaluar_fortaleza(contraseña)
    label_fortaleza.config(text=f"Fortaleza: {fortaleza}")
    #funcion para copiar la contraseña al portapapeles
    def copiar_contraseña(): 
        contraseña = entrada_resultado.get()
        if contraseña: 
            pyperclip.copy(contraseña)
            messagebox.showinfo("copiada", "contraseña copiada al portapapeles")
#funcion de interfaz 
ventana = tk.Tk()
ventana.title("Generador de Contraseñas")
ventana.geometry("400x550")
ventana.config(bg="#f8e1f4")

#funcion robot  con placeholder 
label_robot = tk.Label(ventana, text="🤖", font=("Arial", 60), bg="#f8e1f4")
label_robot.pack(pady=10)

#funcion de slider longitud 
tk.Label(ventana, text="longitud de la contraseña", bg="#f8e1f4").pack()
slider_longitud = tk.Scale(ventana, from_=4, to=32, orient="horizontal", bg="#f8e1f4")
slider_longitud.set(12)
slider_longitud.pack(pady=5)

# Checkboxes
var_mayus = tk.BooleanVar()
var_minus = tk.BooleanVar()
var_numeros = tk.BooleanVar()
var_simbolos = tk.BooleanVar()

tk.Checkbutton(ventana, text="Incluir mayúsculas", variable=var_mayus, bg="#f8e1f4").pack(anchor="w", padx=40)
tk.Checkbutton(ventana, text="Incluir minúsculas", variable=var_minus, bg="#f8e1f4").pack(anchor="w", padx=40)
tk.Checkbutton(ventana, text="Incluir números", variable=var_numeros, bg="#f8e1f4").pack(anchor="w", padx=40)
tk.Checkbutton(ventana, text="Incluir símbolos", variable=var_simbolos, bg="#f8e1f4").pack(anchor="w", padx=40)

#boton de generar la contraseña 
tk.Button(ventana, text="Generar contraseña", command=generar_contraseña, bg="#e085d9", fg="white").pack(pady=15)

#campo de resultado
entrada_resultado = tk.Entry(ventana, width=30, font=("Arial", 14), justify="center")
entrada_resultado.pack(pady=10)

# Etiqueta para mostrar la fortaleza
label_fortaleza = tk.Label(ventana, text="Fortaleza: ", bg="#f8e1f4", font=("Arial", 12))
label_fortaleza.pack(pady=5)

# Botón copiar
# Función para copiar la contraseña al portapapeles
def copiar_contraseña():
    contraseña = entrada_resultado.get()
    if contraseña:
        pyperclip.copy(contraseña)
        messagebox.showinfo("Copiado", "¡Contraseña copiada al portapapeles!")

tk.Button(ventana, text="Copiar", command=copiar_contraseña, bg="#d36ed1", fg="white").pack()

ventana.mainloop()
