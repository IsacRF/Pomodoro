import time

def timer(duration):
    """Função responsável por contar o tempo dado em minutos."""
    seconds = duration * 60  # Converte os minutos para segundos
    while seconds:
        mins, secs = divmod(seconds, 60)  # Calcula minutos e segundos restantes
        timer_format = f'{mins:02d}:{secs:02d}'  # Formata o tempo no estilo MM:SS
        print(timer_format, end="\r")  # Exibe o tempo e sobrescreve a linha anterior
        time.sleep(1)  # Pausa de 1 segundo
        seconds -= 1  # Decrementa o contador

    print("Tempo acabou!")  # Mensagem ao final do temporizador

def short_break(duration):
    """Função responsável por contar o tempo de pausa em minutos."""
    print(f"Iniciando uma pausa de {duration} minutos.")
    timer(duration)  # Reutiliza a função 'timer' para a pausa
    print("Pausa acabou! Vamos voltar ao trabalho.")

def pomodoro_cycle(work_duration, short_break_duration, cycles):
    """Função responsável por executar ciclos de trabalho e pausas curtas."""
    for i in range(cycles):
        print(f"\nCiclo {i + 1} de {cycles}:")
        print("Hora de trabalhar!")
        timer(work_duration)  # Período de trabalho

        if i < cycles - 1:
            short_break(short_break_duration)  # Pausa curta após o ciclo de trabalho
        else:
            print("Todos os ciclos concluídos! Bom trabalho!")

def long_break(duration):
    """Função responsável por contar o tempo de pausa longa em minutos."""
    print(f"Iniciando uma pausa longa de {duration} minutos.")
    timer(duration)  # Reutiliza a função 'timer' para a pausa longa
    print("Pausa longa acabou! Parabéns pelo progresso!")

def pomodoro_cycle(work_duration, short_break_duration, long_break_duration, cycles):
    """Executa ciclos de trabalho e pausas curtas, seguidos por uma pausa longa."""
    for i in range(cycles):
        print(f"\nCiclo {i + 1} de {cycles}:")
        print("Hora de trabalhar!")
        timer(work_duration)  # Período de trabalho

        if i < cycles - 1:
            short_break(short_break_duration)  # Pausa curta após o ciclo de trabalho
        else:
            print("Todos os ciclos concluídos! Hora da pausa longa.")
            long_break(long_break_duration)  # Pausa longa após o último ciclo

pomodoro_cycle(25, 5, 15, 4)  # 25 minutos de trabalho, 5 minutos de pausa curta, 15 minutos de pausa longa após 4 ciclos