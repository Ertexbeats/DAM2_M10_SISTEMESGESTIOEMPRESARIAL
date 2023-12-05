class Bill:
    def __init__(self, dni, name, surname, phone, totalPrice):
        self.dni = dni
        self.name = name
        self.surname = surname
        self.phone = phone
        self.totalPrice = totalPrice

    def __str__(self):
        return (
            f"------- Bill -------\n"
            f"\tDNI: {self.dni}\n"
            f"\tName: {self.name}\n"
            f"\tSurname: {self.surname}\n"
            f"\tPhone: {self.phone}\n"
            f"\tTotalPrice: {self.totalPrice}€"
        )
