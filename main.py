import tkinter as tk

def calcular(op):
    "Calcula la operación seleccionada y actualiza la etiqueta de resultado."
    try:
        n1 = float(numero1.get())
        n2 = float(numero2.get())
        if op == "sumar":
            resultado.set(n1 + n2)
        elif op == "restar":
            resultado.set(n1 - n2)
        elif op == "multiplicar":
            resultado.set(n1 * n2)
    except ValueError:
        resultado.set("Error: Ingresa números válidos")

def add_placeholder(entry, placeholder_text):
    entry.insert(0, placeholder_text)
    entry.config(fg="grey")
    def on_focus_in(event):
        if entry.get() == placeholder_text:
            entry.delete(0, tk.END)
            entry.config(fg="white")
    def on_focus_out(event):
        if entry.get() == "":
            entry.insert(0, placeholder_text)
            entry.config(fg="grey")
    entry.bind("<FocusIn>", on_focus_in)
    entry.bind("<FocusOut>", on_focus_out)


ventana = tk.Tk()
ventana.title("Calculadora Moderna")
ventana.configure(bg="#2b2b2b")
ventana.geometry("320x300")
ventana.minsize(300, 300)  

numero1 = tk.StringVar()
numero2 = tk.StringVar()
resultado = tk.StringVar()


tk.Label(ventana, text="Número 1:", fg="white", bg="#2b2b2b", font=("Arial", 12)).grid(row=0, column=0, padx=10, pady=10, sticky="w")
entry1 = tk.Entry(ventana, textvariable=numero1, font=("Arial", 12), bg="#3c3c3c", fg="white", relief="flat", insertbackground="white")
entry1.grid(row=0, column=1, padx=10, pady=10, sticky="ew")
add_placeholder(entry1, "Ingresa un número")

tk.Label(ventana, text="Número 2:", fg="white", bg="#2b2b2b", font=("Arial", 12)).grid(row=1, column=0, padx=10, pady=10, sticky="w")
entry2 = tk.Entry(ventana, textvariable=numero2, font=("Arial", 12), bg="#3c3c3c", fg="white", relief="flat", insertbackground="white")
entry2.grid(row=1, column=1, padx=10, pady=10, sticky="ew")
add_placeholder(entry2, "Ingresa un número")


btn_sumar = tk.Button(ventana, text="Sumar", command=lambda: calcular("sumar"), bg="#555555", fg="white", relief="flat", font=("Arial",12))
btn_sumar.grid(row=2, column=0, padx=10, pady=10, sticky="ew")

btn_restar = tk.Button(ventana, text="Restar", command=lambda: calcular("restar"), bg="#555555", fg="white", relief="flat", font=("Arial",12))
btn_restar.grid(row=2, column=1, padx=10, pady=10, sticky="ew")

btn_mult = tk.Button(ventana, text="Multiplicar", command=lambda: calcular("multiplicar"), bg="#555555", fg="white", relief="flat", font=("Arial",12))
btn_mult.grid(row=3, column=0, columnspan=2, padx=10, pady=10, sticky="ew")

tk.Label(ventana, text="Resultado:", fg="white", bg="#2b2b2b", font=("Arial", 12, "bold")).grid(row=4, column=0, padx=10, pady=10, sticky="w")
tk.Label(ventana, textvariable=resultado, fg="white", bg="#2b2b2b", font=("Arial", 14)).grid(row=4, column=1, padx=10, pady=10, sticky="w")


ventana.grid_columnconfigure(0, weight=1)
ventana.grid_columnconfigure(1, weight=2)

ventana.mainloop()
