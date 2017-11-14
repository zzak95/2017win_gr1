#Banking simulator. Write a code in python that simulates the banking system.
#The program should:
# - be able to create new banks
# - store client information in banks
# - allow for cash input and withdrawal
# - allow for money transfer from client to client
#If you can thing of any other features, you can add them.
#This code shoud be runnable with 'python kol1.py'.
#You don't need to use user input, just show me in the script that the structure of your code works.
#If you have spare time you can implement: Command Line Interface, some kind of data storage, or even multiprocessing.
#Do your best, show off with good, clean, well structured code - this is more important than number of features.
#After you finish, be sure to UPLOAD this (add, commit, push) to the remote repository.
#Good Luck


import sys


class Client:
    def __init__(self, name, surname, cash):
        self.name=name
        self.surname=surname
        self.cash=cash

    def print_client(self):
        print(self.name," ",self.surname," ",self.cash," ")


class Bank:
    def __init__ (self):
        self.data=[]

    def add_client(self, client):
               self.data.append(client)

    def input(self, client, cash_plus):
        index=self.data.index(client)
        self.data[index].cash+=cash_plus

    def withdrawal(self, client, cash_minus):
        index = self.data.index(client)
        self.data[index].cash-=cash_minus

    def transfer(self, client1, client2, cash_amount):
        self.withdrawal(client1, cash_amount)
        self.input(client2, cash_amount)

    def write_bank_data(self, filename):
        f=open(filename,'w')
        for cl in (self.data):
            f.write("{} {} {}\n".format(cl.name, cl.surname,cl.cash))
        f.close()


class Transaction:
    def __init__(self):
        self.banks=[]

    def add_bank(self, bank):
        self.banks.append(bank)

    def transfer(self, bank1, bank2, client1, client2, cash_amount):
        id1=self.banks.index(bank1)
        self.banks[id1].withdrawal(client1, cash_amount)
        id2 = self.banks.index(bank2)
        self.banks[id2].input(client2, cash_amount)




if __name__=="__main__":

    b1=Bank()
    b2=Bank()
    c = []
    i=0
    stop='y'
    stop1='y'
    stop2='y'
    while stop=='y':
            print("do you want to add a client? (y/n)\n")
            answ=input()
            if answ=="n":
                stop=answ
                break
            print("type in client's name\n")
            name=sys.stdin.readline()
            print("type in client's surname\n")
            surname=sys.stdin.readline()
            print("type in amount of cash\n")
            cash = sys.stdin.readline()
            c.append(Client(name,surname,int(cash)))
            i +=1

    while stop1=='y':
        print("which client do you want to add to the 1st bank? if you don't want more clients here press n \n")
        answ=input()
        if answ=='n':
            stop=answ
            break
        else:
            b1.add_client(c[int(answ)])

    while  stop2 == 'y':
            print("which client do you want to add to the 2nd bank? if you don't want more clients here press n \n")
            answ = input()
            if answ == 'n':
                stop = answ
                break
            else:
                b2.add_client(c[int(answ)])

    for cl in c:
        cl.print_client()

    b1.input(c[0],100)
    b1.withdrawal(c[1],200)

    print("after first operations: \n")

    for cl in b1.data:
        cl.print_client()

    b1.transfer(c[0],c[1],500)

    print("after transfer: \n")

    for cl in b1.data:
        cl.print_client()

    b1.write_bank_data("b1_data.txt")
    b2.write_bank_data("b2_data.txt")

    t=Transaction()
    t.add_bank(b1)
    t.add_bank(b2)
    t.transfer(b1,b2,c[0],c[2],500)

    print("after second transfer: \n")

    for cl in b1.data:
        cl.print_client()
    b2.data[0].print_client()







