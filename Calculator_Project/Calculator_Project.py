import tkinter as tk

class Calculator:
    def __init__(self, display):
        self.display = display
        self.current_value = ""
        self.operator = ""
        self.clear = ""
        self.first_number = 0
        self.is_operator_pressed = False

    def add_number(self, num):
        if self.is_operator_pressed:
            self.display.delete(0, tk.END)
            self.is_operator_pressed = False
        current = self.display.get()
        self.display.delete(0, tk.END)
        self.display.insert(0, current + str(num))

    def set_operator(self, operator):
        self.first_number = int(self.display.get())
        self.operator = operator
        self.is_operator_pressed = True

    def set_clear(self, clear):
        self.res = int(self.display.get())
        self.clear = clear
        self.is_operator_pressed = True

    def calculate(self):
        second_number = int(self.display.get())
        print(second_number)
        result = 0
        if self.operator == "+":
            print("+ Pressed")
            result = self.first_number + second_number
        elif self.clear == "-":
            self.res = ""
            print("_")
            result = ""
        self.display.delete(0, tk.END)
        self.display.insert(0, str(result))


main_window = tk.Tk()
main_window.geometry("300x400")
main_window.title("Calculator")

calculator_display = tk.Entry(main_window, width=25, justify="right", font=("Arial", 14))
calculator_display.grid(row=0, column=0, columnspan=4)
calculator_display.insert(0, "0")

calculator = Calculator(calculator_display)

# Number buttons
buttons = [
    ('1', 1, 0), ('2', 1, 1), ('3', 1, 2),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2),
    ('7', 3, 0), ('8', 3, 1), ('9', 3, 2),
    ('0', 4, 0)
]

for (text, row, col) in buttons:
    tk.Button(main_window, text=text, width=5, height=2,
              command=lambda t=text: calculator.add_number(t)).grid(row=row, column=col)

# Operator buttons
tk.Button(main_window, text="+", width=5, height=2,
          command=lambda: calculator.set_operator("+")).grid(row=1, column=3)

tk.Button(main_window, text="=", width=5, height=2,
          command=calculator.calculate).grid(row=4, column=1)

tk.Button(main_window, text="C", width=5, height=2,
          command=lambda: calculator.set_clear("-")).grid(row=4, column=2)

main_window.mainloop()
