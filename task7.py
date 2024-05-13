# ; İlk classımızda bizim hesab nömrəsi (int) və balans argumentlərimiz olacaq.
# ; Metod olaraq 3 fərqli metoddan istifadə edəcəyik Balansı artırmaq,  Pul çıxarmaq  və balansı göstərmək 
# ; üçün metodlar.
# ; İkinci classımız isə kreditlə bağlıdır. İlk classımızı bu classa inheritance eliyəcəyik və  super initdən  
# ; istifadə edəcəyik.   Bu classda bizim 2 metodumuz olacaq. Kredit vermək və kredit ödənişi. 
# ; Bu səbəbdən classımızın əlavə kimi 1 argumenti olacaq.                                                        
# ; Kredit götürüləcək məbləğ. Kredit sadəcə 1 il müddəti üçündür və faiz yoxdur (kreditinməbləği / 12=aylıq ödəniş).

class Account:
    def __init__(self, acc_id: int, balance: int):
        self.acc_id = acc_id
        self.balance = balance

    def increase(self, inc_amount: int):
        self.balance += inc_amount
        return f"Balansınız artırıldı. Balans: {self.balance}"

    def expense(self, exp_amount: int):
        if exp_amount > self.balance:
            return "Hesabınızda kifayət qədər vəsait yoxdur."
        else:
            self.balance -= exp_amount
            return f"Balansdan məxaric. Balans: {self.balance}"

class Credit(Account):
    def __init__(self, acc_id: int, balance: int, credit_amount: int):
        super().__init__(acc_id, balance)
        self.credit_amount = credit_amount

    def take_credit(self, take_credit: int):
        self.credit_amount += take_credit
        return f"{take_credit} azn kredit hesabınıza yükləndi. Kredit borcu: {self.credit_amount}. Şəxsi vəsaitiniz:{self.balance} azn. Aylıq ödəniş: {self.credit_amount // 12} azn"

    def pay(self, pay_credit: int):
        self.credit_amount -= pay_credit
        return f"{pay_credit} azn borc ödəildi. Qalan borc: {self.credit_amount}"


account = Credit(1001, 1000, 0) 
print(account.increase(300))  
print(account.take_credit(1200))
print(account.pay(200))



    
    