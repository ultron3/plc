import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedTk
import time
import threading
import random

class PLCApp:
    def __init__(self, master):
        self.master = master
        self.master.title("PLC Linea di Produzione Demo")

        self.start_button = ttk.Button(master, text="Avvia Linea di Produzione", command=self.start_production)
        self.start_button.pack(pady=20)

        self.status_label = ttk.Label(master, text="", font=("Helvetica", 14))
        self.status_label.pack(pady=20)

        self.progress_bar = ttk.Progressbar(master, orient='horizontal', length=300, mode='determinate')
        self.progress_bar.pack(pady=20)

    def start_production(self):
        self.start_button.config(state=tk.DISABLED)
        self.status_label.config(text="Linea di produzione avviata, inserimento pezzo...")
        self.progress_bar['value'] = 0

        # Simulare il processo in un thread separato per evitare di bloccare l'interfaccia
        threading.Thread(target=self.run_production_process).start()

    def run_production_process(self):
        # Simulare il processo di produzione con una barra di avanzamento
        for i in range(21):
            time.sleep(1)  # Simula il tempo di attesa
            self.progress_bar['value'] = i * 5  # Aggiorna la barra di avanzamento
            self.master.update_idletasks()  # Aggiorna l'interfaccia grafica

        # Determinare casualmente se il pezzo è conforme o non conforme
        result = random.choice(["conforme", "non conforme"])
        
        # Aggiornare l'interfaccia grafica con il risultato
        self.update_status(result)

    def update_status(self, result):
        self.status_label.config(text=f"Il pezzo è {result}.")
        self.start_button.config(state=tk.NORMAL)
        self.progress_bar['value'] = 100  # Assicurarsi che la barra sia piena

def main():
    root = ThemedTk(theme="arc")
    app = PLCApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
