import tkinter as tk
import subprocess


def shutdown():
    subprocess.call(['shutdown', '-f', '-s', '-t', a.get()])


def restart():
    subprocess.call(['restart', '-f', '-r', '-t', a.get()])


window = tk.Tk()
window.title('Shutdown timer')

frame = tk.Frame(master=window, width=500, height=400, bg='blue').pack()
but1 = tk.Button(master=frame, text='Shut Down', command=shutdown).place(relx=0.14, rely=0.300, height=30, relwidth=0.700)
but2 = tk.Button(master=frame, text='Restart', command=restart).place(relx=0.14, rely=0.400, height=30, relwidth=0.700)
but3 = tk.Button(master=frame, text='Quit', command=quit).place(relx=0.14, rely=0.500, height=30, relwidth=0.700)

info = tk.Label(master=frame, text="Control your PC!!", bg='blue',
                font=('Ariel 12 bold')).place(relx=0.24, rely=0.200, height=30, relwidth=0.500)

a = tk.StringVar()
entry = tk.Entry(textvariable=a).place(relx=0.45, rely=0.600, height=25, width=120)
info2 = tk.Label(master=frame, text="Enter Time", bg='blue',
                font=('Ariel 12 bold')).place(relx=0.24, rely=0.604)

window.mainloop()