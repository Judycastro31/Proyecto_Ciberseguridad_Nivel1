import tkinter as tk 
from tkinter import messagebox 
import random
import string 

# Cree la ventana principal
root = tk.Tk()
root.title("Generador de Contraseñas")
root.geometry("400x250")
root.resizable(False, False)

# Cree la etiqueta
label = tk.Label(root, text="Ingrese la longitud de la contraseña:")
label.pack(pady=10)

# Entrada
entry_longitud = tk.Entry(root)
entry_longitud.pack(pady=5)
entry_longitud.focus()

# Etiqueta resultado
label_resultado = tk.Label(root, text="", font=("Arial", 12), fg="green")
label_resultado.pack(pady=10)

# Función para generar la contraseña
def generar_contraseña():
    try:
        longitud = int(entry_longitud.get())
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingrese un número válido.")
        return
    
    if longitud < 8:
        messagebox.showerror("Error", "La longitud mínima de la contraseña es 8.")
        return
         
    caracteres = string.ascii_letters + string.digits + string.punctuation
    contraseña = ''.join(random.choice(caracteres) for _ in range(longitud))
    
    label_resultado.config(text=f"Contraseña generada: {contraseña}")
    
    root.clipboard_clear()
    root.clipboard_append(contraseña)
    messagebox.showinfo("Contraseña Copiada", "La contraseña ha sido copiada al portapapeles.")
    entry_longitud.focus()

# Botón (fuera de la función)
boton = tk.Button(root, text="Generar Contraseña", command=generar_contraseña)
boton.pack(pady=10)
boton.config(bg="pink", fg="white", font=("Arial", 12))

# Ejecutar la app
root.mainloop() 
    
                 
                 