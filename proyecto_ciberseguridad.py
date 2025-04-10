import tkinter as tk 
from tkinter import messagebox 
import random
import string 

# Crear la ventana principal
root = tk.Tk()
root.title("Generador de Contraseñas")

# Crear el campo de entrada para la longitud
entry_longitud = tk.Entry(root)
entry_longitud.pack()

def generar_contraseña(): 
    try: 
        longitud = int(entry_longitud.get())
        if longitud < 8: 
            messagebox.showerror("Error", "La longitud debe ser al menos 8 caracteres.")
            return
        
        caracteres = string.ascii_letters + string.digits + string.punctuation  
        contraseña= ''.join(random.choice(caracteres) for i in range(longitud))
        messagebox.showinfo("contraseña generada", f"tu nueva contraseña es: {contraseña}")
        
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingrese un número válido.")
        
        ventana = tk.Tk()
        ventana.title("Generador de Contraseñas")
        ventana.geometry("400x200")
        ventana.resizable(False, False)
        
        label = tk.label(ventana, text="ingrese la longitud de la contraseña:")
        label.pack(pady=10)
        
        entry_longitud = tk.entry(ventana)
        entry_longitud.pack(pady=5)
        
        boton = tk.Button(ventana,text="generar contraseña", command=generar_contraseña)
        boton.pack(pady=20)
        boton.config(bg="pink", fg="white", font=("Arial", 12))
        
        ventana.mainloop()
        