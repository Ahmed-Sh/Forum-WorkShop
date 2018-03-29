class Atm():
    def __init__(self ,balance ,bank_name):
        self.balance = balance
        self.bank_name = bank_name
        
    def withdraw(self,request):
        print "Welcome to {0} ".format(self.bank_name)
        print "Current balance = {0} ".format(self.balance)
        print "=================================="

        if request > self.balance:
            print "You don't have that much !!"

        elif request < 0:
            print "Error , Wrong request !!!!!"

        else:
            self.balance -= request

            while request >= 100:
                print "give 100"
                request -= 100

            while request >= 50:
                print "give 50"
                request -= 50

            while request >= 10:
                print "give 10"
                request -= 10

            while request >= 5:
                print "give 5"
                request -= 5

            while request < 5 and request > 0:
                print "give " + str(request)
                request -= request
                break

        print "=================================="

        return self.balance

balance1 = 500
balance2 = 1000

atm1 = Atm(balance1 , "Smart Bank")
atm2 = Atm(balance2 , "Baraka Bank")


atm1.withdraw(277)
atm1.withdraw(800)

atm2.withdraw(100)
atm2.withdraw(2000)
