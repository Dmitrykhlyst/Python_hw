from address import Address
from mailing import Mailing

to_address = Address
from_address = Address
to_address = Address(391500, "г. Рязань", "ул. Ленина", 30, 16)
from_address = Address(236404, "г. Москва", "ул. Горького", 171, 342)

sending = Mailing
to_address = Address(391500, "г. Рязань", "ул. Ленина", 30, 16)
from_address = Address(236404, "г. Москва", "ул. Горького", 171, 342)
sending = Mailing(to_address, from_address, 1500, "1234567890")

print(
    "Отправление",
    sending.track,
    "из",
    sending.from_address.index,
    sending.from_address.city,
    sending.from_address.street,
    sending.from_address.home_number,
    sending.from_address.apart_number,
    "в",
    sending.to_address.index,
    sending.to_address.city,
    sending.to_address.street,
    sending.to_address.home_number,
    sending.to_address.apart_number,
    ". Стоимость",
    sending.cost,
    "рублей.",
)
