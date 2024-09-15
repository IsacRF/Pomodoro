from pomodoro import timer, short_break, long_break, pomodoro_cycle
# Código da interface com tkinter aqui

import tkinter as tk

def start_timer():
    print("Iniciar timer")

def reset_timer():
    print("Resetar timer")

# Criando a janela principal
root = tk.Tk()  # Cria a janela
root.title("Pomodoro Timer")  # Define o título da janela
root.geometry("400x300")  # Define o tamanho da janela (largura x altura)

# Rótulo para exibir o tempo (cronômetro)
timer_label = tk.Label(root, text="25:00", font=("Helvetica", 48))
timer_label.pack(pady=20)

# Botão para iniciar o cronômetro
start_button = tk.Button(root, text="Iniciar", command=start_timer)
start_button.pack(pady=10)

# Botão para resetar o cronômetro
reset_button = tk.Button(root, text="Resetar", command=reset_timer)
reset_button.pack(pady=10)

# Exibindo a janela
root.mainloop()  # Mantém a janela aberta até que seja fechada