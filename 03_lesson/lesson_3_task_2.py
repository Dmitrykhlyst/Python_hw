from smartphone import Smartphone

phone1 = Smartphone("POCO", "X6 Pro 5G", "+79512356984")
phone2 = Smartphone("Huawei", "nova13", "+79990062212")
phone3 = Smartphone("Honor", "400", "+79050062212")
phone4 = Smartphone("Samsung", "A10", "+79502365849")
phone5 = Smartphone("Samsung", "Galaxy A56", "+79620555552")

catalog = [phone1, phone2, phone3, phone4, phone5]

for phones in catalog:
    print(f"{phone5.brand} - {phone5.model}. {phone5.number}")
