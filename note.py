import tkinter as tk


class NoteApp:
    def __init__(self):
        self.notes = []

        # Создание главного окна
        self.root = tk.Tk()
        self.root.title("Заметки")

        # Создание поля ввода
        self.entry = tk.Entry(self.root, width=50)
        self.entry.pack()

        # Создание кнопки добавления заметки
        self.button = tk.Button(self.root, text="Добавить заметку", command=self.add_note)
        self.button.pack()

        # Создание списка заметок
        self.listbox = tk.Listbox(self.root)
        self.listbox.pack(expand=True, fill=tk.BOTH)

        # Загрузка заметок из файла
        self.load_notes()

        # Обновление списка заметок
        self.update_list()

        # Обработка закрытия окна
        self.root.protocol("WM_DELETE_WINDOW", self.save_and_exit)

        # Запуск главного цикла
        self.root.mainloop()

    def add_note(self):
        text = self.entry.get()
        if text:
            self.notes.append(text)
            self.entry.delete(0, tk.END)
            self.update_list()

    def update_list(self):
        self.listbox.delete(0, tk.END)
        for note in self.notes:
            self.listbox.insert(tk.END, note)

    def load_notes(self):
        try:
            with open("notes.txt", "r") as f:
                self.notes = f.read().splitlines()
        except FileNotFoundError:
            pass

    def save_notes(self):
        with open("notes.txt", "w") as f:
            f.write("\n".join(self.notes))




if __name__ == "__main__":
    note_app = NoteApp()