import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title('Aluguel de Carro')
root.geometry('300x100')

def calcular_aluguel():
    dias_digitados = entry_dia.get().replace(',', '.')
    km_digitados = entry_km.get().replace(',', '.')

    if dias_digitados.replace('.', '').isdigit() and km_digitados.replace('.', '').isdigit():
        dias_usados = float(dias_digitados)
        km_rodado = float(km_digitados)
        valor_pagar = (dias_usados * 60) + (km_rodado * 0.15)
        messagebox.showinfo('Preço a pagar', f'Valor devido é de R${valor_pagar:.2f} reais')
    else:
        messagebox.showerror('Erro!', 'Digite apenas números nos campos!')

label_explicacao = tk.Label(root, text='Calcule o valor do aluguel', font=('Tahoma', 10))
label_explicacao.grid(row=0, column=0)

label_dia = tk.Label(root, text='Qto dias usados?', font=('Tahoma', 10))
label_dia.grid(row=1, column=0)
entry_dia = tk.Entry(root)
entry_dia.grid(row=1, column=1)

label_km = tk.Label(root, text='Qto km rodados?', font=('Tahoma', 10))
label_km.grid(row=2, column=0)
entry_km = tk.Entry(root)
entry_km.grid(row=2, column=1)

botao_calcular = tk.Button(root, text='Calcular', command=calcular_aluguel)
botao_calcular.grid(row=3, column=0)

root.mainloop()

