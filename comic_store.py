"""Refactorization: making the code more efficient
Jack Andrews
27/3/23"""
import customtkinter as ctk
from customtkinter import filedialog
# This allows us to open a file dialog window


class GUI:
    def __init__(self):
        self.root = ctk.CTk()
        self.root.title("Comic Book Store")
        mainframe = ctk.CTkFrame(self.root, fg_color="transparent")
        mainframe.grid()
        self.vcmd = mainframe.register(self.validate)
        # This allows us to validate the user's input when they enter how many
        # copies they want to restock/sell
        self.header_lbl = ctk.CTkLabel(
            mainframe, text="Comic Book Store", font=(
                "Calibri", 24, "bold"))
        self.header_lbl.grid(
            row=0,
            column=0,
            columnspan=4,
            padx=150,
            pady=10,
            sticky='ew')
        self.comics = {"Super Dude": 8, "Lizard Man": 12, "Water Woman": 3}

        self.sold = 0

        self.dude_lbl = ctk.CTkLabel(
            mainframe,
            text=f"Super Dude: number in stock: {self.comics['Super Dude']}")
        self.dude_lbl.grid(row=1, column=0, sticky='w', padx=30, pady=5)

        self.lizard_lbl = ctk.CTkLabel(
            mainframe,
            text=f"Lizard Man: number in stock: {self.comics['Lizard Man']}")
        self.lizard_lbl.grid(row=2, column=0, sticky='w', padx=30, pady=5)

        self.woman_lbl = ctk.CTkLabel(
            mainframe,
            text=f"Water Woman: number in stock: {self.comics['Water Woman']}")
        self.woman_lbl.grid(row=3, column=0, sticky='w', padx=30, pady=5)

        self.sold_lbl = ctk.CTkLabel(
            mainframe,
            text=f"Total number of comics sold today: {self.sold}",
            text_color="blue")
        self.sold_lbl.grid(row=4, column=0, sticky='w', padx=30, pady=5)

        ctk.CTkLabel(
            mainframe,
            text="Select comic title:").grid(
            row=1,
            column=2,
            sticky='w')

        ctk.CTkLabel(
            mainframe,
            text="Number of comics:").grid(
            row=3,
            column=2,
            sticky='w')

        self.comic_var = ctk.StringVar(mainframe, value="Super Dude")
        self.comic_opt = ctk.CTkOptionMenu(
            mainframe,
            values=[*self.comics],
            variable=self.comic_var)
        self.comic_opt.grid(row=1, column=3, sticky='w', padx=10)

        self.num_comics_var = ctk.StringVar(mainframe)
        self.bad_text_lbl = ctk.CTkLabel(
            mainframe, text_color="red", font=(
                "Calibri", 10), text='')
        # This label is for when the user inputs an invalid character
        self.bad_text_lbl.grid(row=2, column=3)
        self.comics_entry = ctk.CTkEntry(
            mainframe, width=100, textvariable=self.num_comics_var)
        self.comics_entry.configure(
            validate="key", validatecommand=(
                self.vcmd, "%P"))
        # Configuring how the validation command is run
        self.comics_entry.grid(row=3, column=3, sticky='ew', padx=10)

        self.sell_btn = ctk.CTkButton(
            mainframe,
            text="Sell Comic(s)",
            width=0,
            height=20,
            fg_color="green",
            hover_color="#006400",
            command=self.sell_comics)
        self.sell_btn.grid(
            row=4,
            column=2,
            ipadx=5,
            ipady=10,
            sticky='ew',
            pady=5)

        self.restock_btn = ctk.CTkButton(
            mainframe,
            text="Restock Comic(s)",
            width=0,
            height=20,
            command=self.stock_comics)
        self.restock_btn.grid(
            row=4,
            column=3,
            ipadx=5,
            ipady=10,
            sticky='ew',
            padx=10,
            pady=5)

        self.export_btn = ctk.CTkButton(
            mainframe,
            text="Export stats",
            width=0,
            height=20,
            command=self.export)
        self.export_btn.grid(
            row=4,
            column=1,
            ipadx=5,
            ipady=10,
            sticky='ew',
            padx=10,
            pady=5)
        self.root.mainloop()

    def stock_comics(self):
        amnt = self.num_comics_var.get().replace(' ', '')
        # Allows user to input values like '1 000'
        if amnt == '':
            return
        elif int(amnt) == 0:
            return
        # Checking the amount is a valid integer
        amnt = int(amnt)
        comic = self.comic_var.get()
        self.comics[comic] += amnt
        self.update_labels()

    def update_labels(self):
        self.dude_lbl.configure(
            text=f"Super Dude: number in stock: {self.comics['Super Dude']}")
        self.lizard_lbl.configure(
            text=f"Lizard Man: number in stock: {self.comics['Lizard Man']}")
        self.woman_lbl.configure(
            text=f"Water Woman: number in stock: {self.comics['Water Woman']}")
        self.sold_lbl.configure(
            text=f"Total number of comics sold today: {self.sold}")

    def sell_comics(self):
        amnt = self.num_comics_var.get().replace(' ', '')
        if amnt == '':
            return
        elif int(amnt) == 0:
            return
        amnt = int(amnt)
        comic = self.comic_var.get()
        self.confirm = False
        if self.comics[comic] - amnt < 0:
            Confirm(self, f"Can only sell at most {self.comics[comic]} comics")
            if self.confirm:
                self.sold += self.comics[comic]
                self.comics[comic] = 0
            else:
                return
        else:
            self.comics[comic] -= amnt
            self.sold += amnt
        self.update_labels()

    def validate(self, text):  # Prevents the user from entering a non-integer
        text = text.replace(" ", '')
        if text == "":
            return True
        try:
            int(text)
            self.bad_text_lbl.configure(text="")
            return True
        except ValueError:
            self.bad_text_lbl.configure(text=f"Bad character '{text[-1]}'")
            print('\a', end='', flush=True)
            # Telling the user exactly what was invalid, and giving them an
            # error sound
            return False

    def export(self):
        self.history = [f"Super Dude: {self.comics['Super Dude']}",
                        f"Lizard Man: {self.comics['Lizard Man']}",
                        f"Water Woman: {self.comics['Water Woman']}",
                        f"Total Sold: {self.sold}"]
        # This is the data that will be written to a file
        Export(self)


class Confirm:
    # Window that appears when you try to sell too much stock
    def __init__(self, parent, warning):
        print('\a', end='')
        self.parent = parent
        # This allows us to access the attributes of the parent class
        self.warning = warning
        self.warning_box = ctk.CTkToplevel(self.parent.root)
        self.warning_box.title("Confirm")
        self.warning_box.wait_visibility()
        self.warning_box.grab_set()
        # Forces the user to interact with this window
        self.header_lbl = ctk.CTkLabel(
            self.warning_box, text=self.warning, font=(
                "Calibri", 15))
        self.header_lbl.grid(
            row=0,
            column=0,
            columnspan=2,
            padx=50,
            pady=10,
            sticky='ew')

        self.confirm_btn = ctk.CTkButton(
            self.warning_box, text="Sell all stock", command=self.confirm)
        self.confirm_btn.grid(row=1, column=0, sticky='ew', padx=5, pady=5)

        self.cancel_btn = ctk.CTkButton(
            self.warning_box, text="Cancel", command=self.cancel)
        self.cancel_btn.grid(row=1, column=1, sticky='ew', padx=5, pady=5)

        self.parent.root.wait_window(self.warning_box)

    def confirm(self):
        self.parent.confirm = True
        self.warning_box.destroy()

    def cancel(self):
        self.parent.confirm = False
        self.warning_box.destroy()


class Export:
    # This window allows the user to save stock data to a specified file
    def __init__(self, parent):
        self.parent = parent
        self.export_box = ctk.CTkToplevel(self.parent.root)
        self.export_box.title("Export")
        self.export_box.wait_visibility()
        self.export_box.grab_set()
        self.text = ctk.CTkTextbox(
            self.export_box, height=80, width=150, font=(
                "Calibri", 12), state="disabled")
        self.text.grid(row=0, column=0, sticky='nsew', padx=10, pady=10)
        self.text.configure(state="normal")
        self.text.insert("1.0", "\n".join(self.parent.history))
        self.text.configure(state="disabled")
        # Making the text read-only
        self.export_btn = ctk.CTkButton(
            self.export_box,
            text="Save stats",
            command=self.save_stats)
        self.export_btn.grid(row=1, column=1, sticky='se', padx=10, pady=10)

    def save_stats(self):
        # Using this to make the default save directory the current directory
        from os import getcwd
        # Opens file dialog window so the user can save the data
        try:
            with filedialog.asksaveasfile(initialdir=getcwd()) as f:
                f.write("\n".join(self.parent.history))
            self.export_box.destroy()
        except AttributeError:
            # Happens when the user closes the window without saving
            pass


def main():
    GUI()


if __name__ == "__main__":
    main()
