class Bank(object):
    cash = 1000

    @classmethod
    def avail_cash(cls):
        print(cls.cash)


class BobBank(Bank):
    pass


class StateBank(Bank):
    cash = 20000

    @classmethod
    def avail_cash(cls):
        print(cls.cash + Bank.cash)


b = BobBank()

b.avail_cash()


s = StateBank()

s.avail_cash()
