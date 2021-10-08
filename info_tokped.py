import tkinter

class DataTokopedia:
    def __init__(self):
        self.window = tkinter.Tk()

    def sumbit_info(self):
        self.username = self.user_name.get()
        self.pass_word = self.password.get()
        self.shop = self.type_shopping.get()
        self.window.destroy()

    def user_pass(self):
        self.window.title("Your Information")
        self.window.config(padx=50, pady=50)

        self.rule = tkinter.Label(text="Before you login in Tokopedia, please read this first!\n"
                                       "This secret word for you, in Shopping label if you wanted a discount item type 'discount' \n "
                                       "and if you want find the item you needed type 'manually'\n")
        self.rule.grid(column=1, row=0, columnspan=3)

        self.user_label = tkinter.Label(text="Username : ")
        self.user_label.grid(column=1, row=1)
        self.user_name = tkinter.Entry(width=50)
        self.user_name.grid(column=2, row=1, columnspan=1)

        self.pass_label = tkinter.Label(text="Password : ")
        self.pass_label.grid(column=1, row=2)
        self.password = tkinter.Entry(width=50)
        self.password.grid(column=2, row=2, columnspan=1)

        self.shopping = tkinter.Label(text="Shopping : ")
        self.shopping.grid(column=1, row=3)
        self.type_shopping = tkinter.Entry(width=50)
        self.type_shopping.grid(column=2, row=3, columnspan=1)

        self.sumbit_button = tkinter.Button(text="Submit", command=self.sumbit_info)
        self.sumbit_button.grid(column=1, row=4, columnspan=3)

        self.window.mainloop()
