import random
import tkinter as tk

class User:
    def __init__(self, name, age, height, weight):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight

    def generate_exercise(self):
        exercises = ['Agachamento', 'Supino', 'Flexão de Braço', 'Abdominal', 'Corda', 'Barra Fixa']
        return random.choice(exercises)

class Gym:
    def __init__(self):
        self.users = []

    def add_user(self, user):
        self.users.append(user)

    def generate_exercises(self):
        for user in self.users:
            exercise = user.generate_exercise()
            print(f"{user.name} deve fazer {exercise} hoje.")

def add_user():
    name = name_entry.get()
    age = age_entry.get()
    height = height_entry.get()
    weight = weight_entry.get()

    user = User(name, age, height, weight)
    gym.add_user(user)

def generate_exercises():
    gym.generate_exercises()

gym = Gym()

window = tk.Tk()
window.title ('Cadastro Alunos Academia')

name_label = tk.Label(window, text='Nome:')
name_label.grid(row=0, column=0)
name_entry = tk.Entry(window)
name_entry.grid(row=0, column=1)

age_label = tk.Label(window, text='Idade:')
age_label.grid(row=1, column=0)
age_entry = tk.Entry(window)
age_entry.grid(row=1, column=1)

height_label = tk.Label(window, text='Altura:')
height_label.grid(row=2, column=0)
height_entry = tk.Entry(window)
height_entry.grid(row=2, column=1)

weight_label = tk.Label(window, text='Peso:')
weight_label.grid(row=3, column=0)
weight_entry = tk.Entry(window)
weight_entry.grid(row=3, column=1)

add_button = tk.Button(window, text='Adicionar Usuário', command=add_user)
add_button.grid(row=4, column=0)

generate_button = tk.Button(window, text='Gerar Exercícios', command=generate_exercises)
generate_button.grid(row=4, column=1)

window.mainloop()
