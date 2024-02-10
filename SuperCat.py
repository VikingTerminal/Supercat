import time
import random
import os
from colorama import init, Fore, Style

init(autoreset=True)

def print_typewriter_colored(text):
    for char in text:
        print(Fore.CYAN + Style.BRIGHT + char, end='', flush=True)
        time.sleep(0.03)  

while True:
  
    file_path = input(Fore.GREEN + "Inserisci il percorso del file ('exit' per uscire): ")

    if file_path.lower() == 'exit':
        print(Fore.MAGENTA + "Grazie per aver utilizzato lo script! Seguimi su t.me/VikingTerminal. Arrivederci!")
        break

    try:
        
        full_path = file_path if "." in file_path else file_path + ".txt"

        if not os.path.isfile(full_path):
            raise FileNotFoundError

        with open(full_path, 'r') as file:
           
            content = file.read()

            
            print_typewriter_colored(content)

    except FileNotFoundError:
        print(Fore.RED + "File non trovato. Assicurati di inserire un percorso valido.")
    except Exception as e:
        print(Fore.RED + "Si è verificato un errore:", e)
