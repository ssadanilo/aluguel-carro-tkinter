# Importando Tkinter
import tkinter as tk
from tkinter import messagebox

# Criando janela
root = tk.Tk()
root.title('Aluguel de Carro')
root.geometry('300x100')


# Criando a função
def calcular_aluguel():
    dias_digitados = entry_dia.get().replace(',', '.') # Coloca na variável a entrada da string que vem do campo entry, e troca a vírgula por ponto para não haver erro no float
    km_digitados = entry_km.get().replace(',', '.')
    
    # Verificando se os valores são números
    if dias_digitados.replace('.', '').isdigit() and km_digitados.replace('.', '').isdigit(): # Troca o ponto por uma string vazia para verificar se o que vem antes e depois do que seria o ponto são números
        dias_usados = float(dias_digitados)
        km_rodado = float(km_digitados)
        valor_pagar = (dias_usados * 60) + (km_rodado * 0.15)
        messagebox.showinfo('Preço a pagar', f'Valor devido é de R${valor_pagar:.2f} reais') # Criando uma mensagem do valor obtido
    else:
        messagebox.showerror('Erro!', 'Digite apenas números nos campos!') # Criando uma mensagem de erro caso o usuário digite algo indevido

# Criando widgates
label_explicacao = tk.Label(root, text='Calcule o valor do aluguel', font=('Tahoma', 10)) # Criando uma explicação para facilitar o manuseio do usuário
label_explicacao.grid(row=0, column=0)

label_dia = tk.Label(root, text='Qto dias usados?', font=('Tahoma', 10)) # Label para o usuário inserir a informação necessária ao cálculo
label_dia.grid(row=1, column=0) # Posicionamento da Label
entry_dia = tk.Entry(root)
entry_dia.grid(row=1, column=1)

label_km = tk.Label(root, text='Qto km rodados?', font=('Tahoma', 10))
label_km.grid(row=2, column=0)
entry_km = tk.Entry(root)
entry_km.grid(row=2, column=1)

# Criando botão
botao_calcular = tk.Button(root, text='Calcular', command=calcular_aluguel) # Criando botão e usando a função command para executar o cálculo
botao_calcular.grid(row=3, column=0)

# Criando loop
root.mainloop()

