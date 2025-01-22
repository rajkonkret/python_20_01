import tkinter as tk

from numpy.ma.extras import average


class GradeCalculator:
    def __init__(self, master):
        self.master = master
        self.master.title("Kalkulator Ocen")

        self.student_var = tk.StringVar(master)
        self.student_var.set("Uczeń 1")  # domyślna wartość
        self.student_dropdown = tk.OptionMenu(
            master, self.student_var, "Uczeń 1", "Uczeń 2", "Uczeń 3")
        self.student_dropdown.pack()

        self.grade_entry = tk.Entry(master, width=10)
        self.grade_entry.pack()

        self.button = tk.Button(master, text="Dodaj ocenę", command=self.add_grade)
        self.button.pack()

        self.grades_label = tk.Label(master, text="Dotychczasowe oceny: ")
        self.grades_label.pack()

        self.average_label = tk.Label(master, text="Średnia: ")
        self.average_label.pack()

        self.grade_dict = {"Uczeń 1": [], "Uczeń 2": [], "Uczeń 3": []}

    def add_grade(self):
        grade = self.grade_entry.get()
        grade = float(grade)
        student = self.student_var.get()
        self.grade_dict[student].append(grade)

        self.grade_entry.delete(0, tk.END)

        self.grades_label.config(text="Dotychczasowe oceny: " + str(self.grade_dict[student]))

        average = sum(self.grade_dict[student]) / len(self.grade_dict[student])
        self.average_label.config(text="Średnia: " + str(average))


root = tk.Tk()
calculator = GradeCalculator(root)
root.mainloop()
