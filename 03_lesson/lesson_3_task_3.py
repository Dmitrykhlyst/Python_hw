from address import Address
from mailing import Mailing

to_address = Address
from_address = Address
to_address = 391500, "г. Рязань", "ул. Ленина", 30, 16
from_address = 236404, "г. Москва", "ул. Горького", 171, 342

sending = Mailing
sending(to_address, from_address, 1500, 1234567890)

print(
    "Отправление",
    sending.track,
    "из",
    from_address,
    "в",
    to_address,
    ". Стоимость",
    sending.cost,
    "рублей.",
)