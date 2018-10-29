class Atm:
    def __init__(self ,balance ,bank_name):
        self.balance = balance
        self.bank_name = bank_name
        self.withdrawals_list = []

    def withdraw(self,request):
        print("Current balance =  ",self.balance)
        print("=" * 30)

        if request > self.balance:
            print("You don't have that much !!")

        elif request < 0:
            print("Error , Wrong request !!!!!")

        else:
            self.withdrawals_list.append(request)
            self.balance -= request

            notes = [100, 50, 10, 5]
            for note in notes:
                while request >= note:
                    request -= note
                    print("give ", str(note))

            while request < 5 and request > 0:
                print("give " + str(request))
                request -= request
                break

        print("=" * 30)

        return self.balance

    def show_withdrawals(self):
        for withdrawal in self.withdrawals_list:
            print("Withdrawal No. %d = %d" % ((self.withdrawals_list.index(withdrawal)+1),withdrawal))

        print("Total withdrawal = ",sum(self.withdrawals_list))
        print("Your balance now = ",self.balance)
        print("=" * 30)

balance1 = 500
balance2 = 1000

atm1 = Atm(balance1 , "Smart Bank")
atm2 = Atm(balance2 , "Baraka Bank")


atm1.withdraw(277)
atm1.withdraw(217)
atm1.show_withdrawals()

atm2.withdraw(100)
atm2.withdraw(2000)
atm2.show_withdrawals()
