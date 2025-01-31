import tkinter as tk

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Αριθμομηχανή")
        self.root.resizable(False, False)

        # Διάταξη πλήκτρων
        self.button_layout = [
            ["C", "del", "", "d"],
            ["7", "8", "9", "/"],
            ["4", "5", "6", "*"],
            ["1", "2", "3", "-"],
            [".", "0", "=", "+"]
        ]

        # Δημιουργία της οθόνης εμφάνισης αποτελέσματος
        self.display = tk.StringVar()
        self.display.set("")
        self.display_label = tk.Label(
            root, 
            textvariable=self.display, 
            font=("Calibri", 30), 
            bg="white", 
            anchor="e", 
            padx=10, 
            pady=20
        )
        self.display_label.grid(row=0, column=0, columnspan=4, sticky="we")

        # Δημιουργία των κουμπιών
        for row_index, row in enumerate(self.button_layout, start=1):
            for col_index, symbol in enumerate(row):
                if symbol == "":
                    continue  # Παράλειψη κενών θέσεων
                self.create_button(symbol, row_index, col_index)

    def create_button(self, symbol, row, col):
        # Καθορισμός χρώματος κουμπιού βάσει του συμβόλου
        if symbol == "=":
            color = "#3399FF"
        elif symbol == "C":
            color = "#FF3333"
        elif symbol == "del":
            color = "#A0A0A0"
        elif symbol in ["/", "*", "-", "+"]:
            color = "orange"
        else:
            color = "white"

        # Δημιουργία και τοποθέτηση του κουμπιού
        button = tk.Button(
            self.root, 
            text=symbol, 
            font=("Calibri", 20, "bold"),
            bg=color, 
            height=2, 
            width=6,
            command=lambda: self.on_button_click(symbol)
        )
        button.grid(row=row, column=col, padx=5, pady=5)

    def on_button_click(self, symbol):
        current_text = self.display.get()

        if symbol == "=":
            try:
                # Αξιολόγηση της μαθηματικής έκφρασης
                answer = eval(current_text)
                self.display.set(str(round(float(answer), 6)))
            except:
                self.display.set("Error")
        elif symbol == "C":
            # Easter egg
            if current_text == "3744":
                print("\nMade by Nikos Gerontas\n")
            self.display.set("")
        elif symbol == "del":
            if current_text not in ["Υπερχείλιση!", "Error"]:
                self.display.set(current_text[:-1])
        else:
            if len(current_text) > 18:
                if current_text != "Error":
                    self.display.set("Υπερχείλιση!")
            else:
                self.display.set(current_text + symbol)

def main():
    root = tk.Tk()
    Calculator(root)
    root.mainloop()
    print("\n--Τέλος Προγράμματος--\n")

if __name__ == "__main__":
    main()
