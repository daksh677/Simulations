import random
import numpy as np
import matplotlib.pyplot as plt
from tkinter import StringVar, Label, Tk, Entry, Button

def simulate(n, k, samples):
    same_choice_wins = 0
    switched_choice_wins = 0
    for _ in range(samples):
        doors = ["car"] * k + ["goat"] * (n - k)
        random.shuffle(doors)
        first_choice = random.choice(doors)
        if first_choice == "car":
            same_choice_wins += 1
        else:
            switched_choice_wins += 1
    return same_choice_wins / samples, switched_choice_wins / samples

def run_simulation():
    samples = int(no_sample.get())
    n = int(n_value.get())
    k = int(k_value.get())
    same_choice_result, switched_choice_result = simulate(n, k, samples)
    same_choice.set(same_choice_result)
    switched_choice.set(switched_choice_result)
    plot_simulation()

def plot_simulation():
    plt.figure(figsize=(12, 6))

    # Plot for varying n
    plt.subplot(1, 2, 1)
    for k in k_values:
        win_ratios_n = [simulate(n, k, 10000)[1] / simulate(n, k, 10000)[0] for n in n_values]
        plt.plot(win_ratios_n, n_values, label=f"k = {k}")
    plt.ylabel("Number of Doors (n)")
    plt.xlabel("P(win|W) / P(win|T)")
    plt.title("Variation with n")
    plt.legend()
    plt.grid(True)

    # Plot for varying k (only for integer values)
    plt.subplot(1, 2, 2)
    for n in n_values:
        win_ratios_k = [simulate(n, int(k), 10000)[1] / simulate(n, int(k), 10000)[0] for k in k_values]
        plt.plot(win_ratios_k, k_values, label=f"n = {n}")
    plt.ylabel("Number of Cars (k)")
    plt.xlabel("P(win|W) / P(win|T)")
    plt.title("Variation with k (integer values)")
    plt.legend()
    plt.grid(True)

    plt.tight_layout()
    plt.show()

# Tkinter GUI setup
window = Tk()
window.geometry("400x300")
window.title("Monty Hall Simulation")
window.resizable(0, 0)

same_choice = StringVar()
switched_choice = StringVar()
same_choice.set(0)
switched_choice.set(0)

Label(text="Same choice").place(x=80, y=8)
Label(text="Switched choice").place(x=80, y=40)
Label(textvariable=same_choice, font=(15)).place(x=180, y=8)
Label(textvariable=switched_choice, font=(15)).place(x=180, y=40)

Label(window, text="Number of Doors (n):").place(x=10, y=80)
Label(window, text="Number of Cars (k):").place(x=10, y=110)

n_value = Entry(window)
n_value.place(x=150, y=80)

k_value = Entry(window)
k_value.place(x=150, y=110)

no_sample = Entry(window)
no_sample.place(x=150, y=140)

Label(window, text="Number of Samples:").place(x=10, y=140)

run_button = Button(window, text="Run Simulation", command=run_simulation)
run_button.place(x=270, y=135)

# Values for plotting
n_values = range(3, 11)
k_values = range(1, 6)

window.mainloop()
