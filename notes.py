# from tkinter import *
# from tkinter import messagebox

# функция для сохранения введенного текста в файл
def save_note():
    note_text = note_entry.get(1.0, END)
    if note_text.strip() == "":
        messagebox.showwarning("Ошибка", "Введите текст заметки")
        return
    file = open("notes.txt", "a")
    file.write(note_text + "\n")
    file.close()
    messagebox.showinfo("Успех", "Заметка успешно сохранена")

# функция для чтения сохраненных заметок из файла и вывода их на экран
# def read_notes():
#     file = open("notes.txt", "r")
#     notes_text = file.read()
#     file.close()
#     notes_label.config(text=notes_text)

# создание главного окна
root = Tk()
root.title("Мои заметки")

# создание элементов интерфейса: метка для отображения заметок, поле для ввода новой заметки и кнопка для добавления заметки
# notes_label = Label(root, text="")
# notes_label.pack()

note_entry = Text(root)
note_entry.pack()

btn_save_note = Button(root, text="Сохранить заметку", command=save_note)
btn_save_note.pack()

# вызов функции для чтения сохраненных заметок при запуске программы
read_notes()

root.mainloop()