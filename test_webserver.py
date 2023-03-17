import tkinter as tk
import webbrowser
import os

def open_browser():
    webbrowser.open('http://localhost:8000')

def start_server():
    global server_process
    server_process = os.popen('python3 -m http.server')

def stop_server():
    os.system('kill $(lsof -t -i :8000)')

root = tk.Tk()
root.title('Web Server')
root.geometry('300x250')

start_button = tk.Button(root, text='Start Server', command=start_server)
start_button.pack(pady=10)

stop_button = tk.Button(root, text='Stop Server', command=stop_server)
stop_button.pack(pady=10)

status_label = tk.Label(root, text='Server not running', fg='red')
status_label.pack(side='bottom', pady=10)

def check_status():
    if os.system('lsof -i :8000 > /dev/null') == 0:
        status_label.config(text='Server running', fg='green')
    else:
        status_label.config(text='Server not running', fg='red')
    root.after(1000, check_status)

check_status()

open_button = tk.Button(root, text='Open Browser', command=open_browser)
open_button.pack(pady=10)

root.mainloop()