from tkinter import *
from datetime import datetime
import random



class Wallet:
    ticker = "BTC"
    amtCoins = 0.0
    balance = 0.0
    formatted_bal = "{:.2f}".format(balance)

    def addBitcoinOwn(self, coins, isEnough, bitcoinPrice):

        if isEnough:
            self.amtCoins += float(coins)
            self.balance -= float(bitcoinPrice)*float(coins)
            self.formatted_bal = "{:.2f}".format(self.balance)

    def addToBalance(self, newBal, goodInput):

        if goodInput:
            self.balance += float(newBal)
            self.formatted_bal = "{:.2f}".format(self.balance)

    def print(self):
        print("you have " + str(self.amtCoins) + " " + self.ticker)


class Ledger:
    transactions = []

    def addToHistory(self, seelOrBuy, isEnough, date, bitCoin):

        if isEnough:
            transaction = "you " + seelOrBuy + " " + bitCoin + " BTC on " + date
            self.transactions.append(transaction)

    def printHistory(self):

        window = Tk()
        window.configure(bg="black")
        window.geometry("300x300")
        hist = Label(window,
                     text="History\n",
                     height=200,
                     width=200,
                     bg="black",
                     fg="green")

        close = Button(window,
                       text="Close",
                       width=5,
                       height=1,
                       background="white",
                       foreground="black",
                       font=("Courier", 10, "bold"),
                       command=lambda: [window.destroy()]
                       )

        for x in self.transactions:
            hist["text"] += x + "\n"

        hist.pack()
        close.place(x=125, y=255)
        window.mainloop()


class MyDate:

    def currentTime(self):
        now = datetime.now()
        date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
        return date_time


class GetLive:

    def currentVal(self):
        bitcoinWorth = random.uniform(35000.0, 40000.0)
        formatted_bitcoin = "{:.2f}".format(bitcoinWorth)
        return formatted_bitcoin


def main():

    myWallet = Wallet()
    bitCoin = GetLive()
    date = MyDate()
    transaction = Ledger()

    # **************Beginning of GUI ********************************************************************

    window = Tk()
    window.configure(bg="black")
    window.geometry("450x350")
    add_var = StringVar()
    buy_var = StringVar()
    sell_var = StringVar()


    label=Label(
        window,
        text="Bitcoin?",
        foreground="green",  # Set the text color to white
        background="black",  # Set the background color to black
        font=("Courier", 30, "bold"),
        width=10,
        height=2
    )

    balance = Label(
        window,
        text="Balance: ",
        foreground="green",  # Set the text color to white
        background="black",  # Set the background color to black
        font=("Courier", 20, "bold"),
        width=10,
        height=1,
    )

    balanceVal = Label(
        window,
        text="",
        foreground="green",  # Set the text color to white
        background="black",  # Set the background color to black
        font=("Courier", 20, "bold"),
        width=13,
        height=1,
    )

    bitCoinPrice = Label(
        window,
        text="BitCoin Price: ",
        foreground="green",  # Set the text color to white
        background="black",  # Set the background color to black
        font=("Courier", 20, "bold"),
        width=15,
        height=1,
    )

    bitCoinEntry = Label(
        window,
        text=bitCoin.currentVal(),
        foreground="green",  # Set the text color to white
        background="black",  # Set the background color to black
        font=("Courier", 20, "bold"),
        width=10,
        height=1,
    )

    buyEntry = Entry(
        window,
        width=15,
        textvariable=buy_var
    )

    sellEntry = Entry(
        window,
        width=15,
        textvariable=sell_var
    )

    addEntry = Entry(
        window,
        width=19,
        textvariable=add_var
    )

    buy = Button(
        window,
        text="Buy",
        width=7,
        height=1,
        background="white",
        foreground="black",
        font=("Courier", 15, "bold"),
        command=lambda: [transaction.addToHistory("bought", isEnough(rightInput(buyEntry.get()), myWallet.balance, buyEntry.get(), float(bitCoinEntry["text"])), date.currentTime(), buyEntry.get()),
                         myWallet.addBitcoinOwn(buyEntry.get(), isEnough(rightInput(buyEntry.get()), myWallet.balance, buyEntry.get(), float(bitCoinEntry["text"])), bitCoinEntry["text"]),
                         balanceVal.config(text=myWallet.formatted_bal), buy_var.set(""), bitCoinEntry.config(text=bitCoin.currentVal())]

    )

    sell = Button(
        window,
        text="Sell",
        width=7,
        height=1,
        background="white",
        foreground="black",
        font=("Courier", 15, "bold"),
        command=lambda: [transaction.addToHistory("Sold", isEnoughBitCoins(rightInput(sellEntry.get()), myWallet.amtCoins, sellEntry.get()), date.currentTime(), sellEntry.get()),
                         myWallet.addBitcoinOwn(-float(sellEntry.get()), isEnoughBitCoins(rightInput(sellEntry.get()), myWallet.amtCoins, sellEntry.get()), bitCoinEntry["text"]),
                         balanceVal.config(text=myWallet.formatted_bal), sell_var.set(""), bitCoinEntry.config(text=bitCoin.currentVal())]
    )

    add = Button(
        window,
        text="Add Funds",
        width=9,
        height=1,
        background="white",
        foreground="black",
        font=("Courier", 15, "bold"),
        command=lambda: [myWallet.addToBalance(addEntry.get(), rightInput(addEntry.get())), balanceVal.config(text=myWallet.formatted_bal), add_var.set("")]
    )

    history = Button(
        window,
        text="History",
        width=7,
        height=1,
        background="white",
        foreground="black",
        font=("Courier", 15, "bold"),
        command=lambda: [transaction.printHistory()]
    )

    label.pack()
    balance.place(x=15, y=120)
    bitCoinPrice.place(x=25, y=180)
    balanceVal.place(x=170, y=120)
    buyEntry.place(x=5, y=275)
    sellEntry.place(x=110, y=275)
    addEntry.place(x=215, y=275)
    bitCoinEntry.place(x=275, y=180)
    add.place(x=215, y=300)
    buy.place(x=5, y=300)
    sell.place(x=110, y=300)
    history.place(x=345, y=300)
    window.mainloop()


# *****************End of GUI ***********************************************************


def isEnoughBitCoins(gooInput, ownCoins, sellingCoins):

    if gooInput:
        if ownCoins >= float(sellingCoins):
            return True
        else:
            return False


def isEnough(goodInput, balance, coins, bitCoinPrice):

    if goodInput:

        price = float(coins)*bitCoinPrice
        if balance >= price:
            return True
        else:
            return False


def rightInput(money):
    try:
        float(money)
        return True
    except ValueError:
        return False





if __name__ == '__main__':
    main()