'''
Author : Artur Assis Alves
Date   : 09/06/2020
Title  : Bank Software
'''
import dbm, pickle
import tkinter as tk

BANK_NAME = "BancoABC"



class Sistema:
    ''' Bank system.'''
    def __init__(self, name):
        self.name = name
        is_in_db = False
        self.db = dbm.open(BANK_NAME, 'c')
        for i in self.db:
            decoded_name = pickle.loads(i)
            if (decoded_name == name):
                self.client_data = pickle.loads(self.db[i])
                is_in_db = True
        if (not is_in_db):
            self.client_data = {"name":name, "balance":0, "bank_statement":[]}
        self.db.close()

    def cash_withdraw (self, amount):
        if (self.client_data["balance"] >= amount):
            self.client_data["balance"] -= amount
            length = len(self.client_data["bank_statement"])
            total = self.client_data["balance"]
            self.client_data["bank_statement"].append("Operation {0} Withdraw of : {1:.2f}. Total : {2:.2f}".format(length + 1, amount, total))
        else:
            print("DENIED")
    def return_bank_statement(self):
        print("Bank Statement :")
        for i in self.client_data["bank_statement"]:
            print(i)

    def cash_deposit (self, amount):
        self.client_data["balance"] += amount
        length = len(self.client_data["bank_statement"])
        total = self.client_data["balance"]
        self.client_data["bank_statement"].append("Operation {0} Deposit of : {1:.2f}. Total : {2:.2f}".format(length + 1, amount, total))

    def return_balance(self):
        print("Bank balance :")
        print("Total : R${0:.2f}".format(self.client_data["balance"]))

    def close_terminal(self):
        print("##########################CLOSED##########################")
        self.db = dbm.open(BANK_NAME, 'c')
        coded_name = pickle.dumps(self.name)
        self.db[coded_name] = pickle.dumps(self.client_data)
        self.db.close()

class Invoker():
    def __init__(self):
        self.history_commands = []
        self.list_commands    = []

    def set_command (self, command):
        self.list_commands.append(command)

    def execute_command (self):
        command_to_execute = self.list_commands.pop()
        self.history_commands.append(command_to_execute)
        return command_to_execute.execute()

    def show_history_commands(self):
        counter = len(self.history_commands)
        print("Command List : ")
        for i in self.history_commands:
            print("{0}- command: {1}".format(counter, i.__class__.__name__))
            counter -= 1


class CommandInterface():
    def execute(self):
        pass



class CashWithdraw(CommandInterface):
    def __init__(self, amount, client):
        self.amount = amount
        self.client = client
    def execute(self):
        self.client.cash_withdraw(self.amount)

class ReturnBankStatement (CommandInterface):
    def __init__(self, client):
        self.client = client

    def execute(self):
        return self.client.return_bank_statement()

class CashDeposit(CommandInterface):
    def __init__(self, amount, client):
        self.amount = amount
        self.client = client
    def execute(self):
        self.client.cash_deposit(self.amount)

class ReturnBalance(CommandInterface):
    def __init__(self, client):
        self.client = client

    def execute(self):
        return self.client.return_balance()

class CloseTerminal(CommandInterface):
    def __init__(self, client):
        self.client = client
    def execute(self):
        self.client.close_terminal()



#TKinter module:



class Application(tk.Frame):
    def __init__(self, name, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()
        self.invoker = Invoker()
        self.client  = Sistema(name)

    def create_widgets(self):
        #Return Balance Button:
        self.btt_1 = tk.Button(self)
        self.btt_1["text"] = "Return Balance\n"
        self.btt_1["command"] = self.return_balance_button
        self.btt_1.pack(side="top")

        #Cash Withdraw Button:
        self.btt_2 = tk.Button(self)
        self.btt_2["text"] = "Cash Withdraw\n"
        self.btt_2["command"] = self.cash_withdraw_button
        self.btt_2.pack(side="top")

        #Return Statement Button:
        self.btt_3 = tk.Button(self)
        self.btt_3["text"] = "Return Bank Statement\n"
        self.btt_3["command"] = self.return_bank_statement_button
        self.btt_3.pack(side="top")

        #Cash Deposit Button:
        self.btt_4 = tk.Button(self)
        self.btt_4["text"] = "Cash Deposit\n"
        self.btt_4["command"] = self.cash_deposit_button
        self.btt_4.pack(side="top")

        #History commands Button:
        self.btt_4 = tk.Button(self)
        self.btt_4["text"] = "History Commands\n"
        self.btt_4["command"] = self.history_commands_button
        self.btt_4.pack(side="top")

        #Close Terminal Button:
        self.btt_4 = tk.Button(self)
        self.btt_4["text"] = "Close Terminal\n"
        self.btt_4["command"] = self.close_terminal_button
        self.btt_4.pack(side="bottom")


    def cash_withdraw_button(self):
        print("Withdraw menu ")
        amount = float(input("Enter with the amount : "))
        new_command = CashWithdraw(amount, self.client)
        self.invoker.set_command(new_command)

    def return_bank_statement_button(self):
        new_command = ReturnBankStatement(self.client)
        self.invoker.set_command(new_command)

    def cash_deposit_button(self):
        print("Deposit menu ")
        amount = float(input("Enter with the amount : "))
        new_command = CashDeposit(amount, self.client)
        self.invoker.set_command(new_command)

    def return_balance_button(self):
        new_command = ReturnBalance(self.client)
        self.invoker.set_command(new_command)


    def close_terminal_button(self):
        new_command = CloseTerminal(self.client)
        self.invoker.set_command(new_command)
        while len(self.invoker.list_commands)>0:
            self.invoker.execute_command()
        self.master.destroy()

    def history_commands_button(self):
        self.invoker.show_history_commands()


if __name__=="__main__":
    name = input("Enter with the client's name before accessing the system :")
    root = tk.Tk()
    app = Application(name, master=root)
    while True:
        if(len(app.invoker.list_commands)>0):
            app.invoker.execute_command()
        app.update_idletasks()
        app.update()
