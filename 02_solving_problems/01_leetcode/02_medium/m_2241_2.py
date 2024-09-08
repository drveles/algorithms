class ATM:

    def __init__(self):
        self.__banknotes = [0] * 5
        self.denominations = [20, 50, 100, 200, 500]

    def deposit(self, banknotesCount: List[int]) -> None:
        for banknote_id in range(5):
            self.__banknotes[banknote_id] += banknotesCount[banknote_id]

    def withdraw(self, amount: int) -> List[int]:
        if amount % 10:
            return [-1]

        banknote_id = 4
        withdraw_banknotes = [0] * 5

        while banknote_id >= 0 and amount:
            if self.__banknotes[banknote_id] and self.denominations[banknote_id] <= amount:
                min_ctr_banknotes = min(amount // self.denominations[banknote_id], self.__banknotes[banknote_id])
                self.__banknotes[banknote_id] -= min_ctr_banknotes
                withdraw_banknotes[banknote_id] = min_ctr_banknotes
                amount -= self.denominations[banknote_id] * min_ctr_banknotes
            banknote_id -= 1

        if amount:
            self.deposit(withdraw_banknotes)
            return [-1]
        else:
            return withdraw_banknotes
