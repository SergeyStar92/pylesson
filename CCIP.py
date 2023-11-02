from tkinter import *
from tkinter import ttk
from main import krypt
from tkinter.messagebox import showerror


res = ''

root = Tk()
root.title("Шифр цезаря")
root.geometry("650x215")

lbl5 = ttk.Label(text='Введите текст')
lbl5.grid(row=0, column=0, columnspan=3)

lbl = ttk.Label(text='Результат')
lbl.grid(row=0, column=3, columnspan=3)
ent = ttk.Entry(width=20)
ent.grid(row=2, column=1)

lbl3 = ttk.Label(text='Сдвиг')
lbl3.grid(row=2, column=0)
btn = ttk.Button(text="Кодирование", command=lambda: code())
btn.grid(row=2, column=2)
btn2 = ttk.Button(text="Копировать результат", command=lambda: copy())
btn2.grid(row=2, column=4)
btn3 = ttk.Button(text="Вставить результат", command=lambda: paste())
btn3.grid(row=0, column=0)
btn4 = ttk.Button(text="Очистить", command=lambda: clear())
btn4.grid(row=0, column=2)
txt = Text(height=10, width=40)
txt.grid(row=1, column=0, columnspan=3)
txt2 = Text(height=10, width=40)
txt2.grid(row=1, column=3, columnspan=3)



def code():
    txt2.delete("1.0", "end")
    if txt.get("1.0", "end") == '' or ent.get() == '':
        showerror(title="Ошибка", message="Не введен текст или сдвиг")
    else:
        text = txt.get("1.0", "end")
        sdv = ent.get()
        txt2.insert("1.0", krypt(text, int(sdv)))


def copy():
    global res
    res = txt2.get("1.0", "end")


def paste():
    txt.delete("1.0", "end")
    txt.insert("1.0", res)


def clear():
    txt.delete("1.0", "end")
    txt2.delete("1.0", "end")



root.mainloop()