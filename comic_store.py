import customtkinter as ctk


class GUI:
    def __init__(self):
        self.root = ctk.CTk()
        self.root.title("Comic Book Store")
        mainframe = ctk.CTkFrame(self.root, fg_color="transparent")
        mainframe.grid()
        self.header_lbl = ctk.CTkLabel(
            mainframe, text="Comic Book Store", font=(
                "Calibri", 24, "bold"))
        self.header_lbl.grid(row=0, column=0, columnspan=3, padx=150, pady=10)

        self.dude_stock = 8
        self.lizard_stock = 12
        self.woman_stock = 3
        self.sold = 0

        self.dude_lbl = ctk.CTkLabel(
            mainframe,
            text=f"Super Dude: number in stock: {self.dude_stock}")
        self.dude_lbl.grid(row=1, column=0, sticky='w', padx=30, pady=5)

        self.lizard_lbl = ctk.CTkLabel(
            mainframe,
            text=f"Lizard Man: number in stock: {self.lizard_stock}")
        self.lizard_lbl.grid(row=2, column=0, sticky='w', padx=30, pady=5)

        self.woman_lbl = ctk.CTkLabel(
            mainframe,
            text=f"Water Woman: number in stock: {self.woman_stock}")
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
            column=1,
            sticky='w')

        ctk.CTkLabel(
            mainframe,
            text="Number of comics:").grid(
            row=2,
            column=1,
            sticky='w')

        self.comic_opt = ctk.CTkOptionMenu(
            mainframe, values=[
                "Super Dude", "Lizard Man", "Water Woman"])
        self.comic_opt.grid(row=1, column=2, sticky='w', padx=10)

        self.num_comics = ctk.StringVar(mainframe)
        self.comics_entry = ctk.CTkEntry(
            mainframe, width=100, textvariable=self.num_comics)
        self.comics_entry.grid(row=2, column=2, sticky='ew', padx=10)

        self.sell_btn = ctk.CTkButton(
            mainframe,
            text="Sell Comic(s)",
            width=0,
            height=20,
            fg_color="green",
            hover_color="#006400")
        self.sell_btn.grid(
            row=3,
            column=1,
            ipadx=5,
            ipady=10,
            sticky='w',
            pady=5)

        self.restock_btn = ctk.CTkButton(
            mainframe, text="Restock Comic(s)", width=0, height=20)
        self.restock_btn.grid(
            row=3,
            column=2,
            ipadx=5,
            ipady=10,
            sticky='w',
            padx=10,
            pady=5)
        self.root.mainloop()


def main():
    GUI()


if __name__ == "__main__":
    main()
