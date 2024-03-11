# Создайте базовый класс "Транспортное средство" с методами для вычисления максимальной скорости и вместимости. Затем создайте производные классы, представляющие разные виды транспорта (например, "Автомобиль" и "Самолет"), и реализуйте соответствующие методы для каждого виде транспорта.

class Transport:
    def __init__(self, max_speed, capacity):
        self.max_speed = max_speed
        self.capacity = capacity

    def get_max_speed(self):
        return self.max_speed

    def get_capacity(self):
        return self.capacity


class Electro(Transport):
    def __init__(self, max_speed, capacity, battery_life):
        super().__init__(max_speed, capacity)
        self.battery_life = battery_life

    def get_battery_life(self):
        return self.battery_life


class Classic(Transport):
    def __init__(self, max_speed, capacity, fuel_type):
        super().__init__(max_speed, capacity)
        self.fuel_type = fuel_type

    def get_fuel_type(self):
        return self.fuel_type


class Customer:
    def __init__(self, id, name):
        self.id = id
        self.name = name


class CustomerTransport:
    def __init__(self, customer_id, transport_id):
        self.customer_id = customer_id
        self.transport_id = transport_id


def main():
    transports = []

    electro_car = Electro(120, 4, "электричество")
    classic_car = Classic(180, 5, "бензин")

    transports.append(electro_car)
    transports.append(classic_car)

    for transport in transports:
        if isinstance(transport, Electro):
            print("Максимальная скорость электрокара:", transport.get_max_speed())
            print("Вместимость электрокара:", transport.get_capacity())
            print("Время работы от батареи:", transport.get_battery_life())
            print()
        elif isinstance(transport, Classic):
            print("Максимальная скорость классического автомобиля:", transport.get_max_speed())
            print("Вместимость классического автомобиля:", transport.get_capacity())
            print("Тип топлива:", transport.get_fuel_type())
            print()

    customers = []

    customer1 = Customer(1, "Иванов")
    customer2 = Customer(2, "Петров")

    customers.append(customer1)
    customers.append(customer2)

    customer_transports = []

    customer_transport1 = CustomerTransport(1, 1)
    customer_transport2 = CustomerTransport(2, 2)

    customer_transports.append(customer_transport1)
    customer_transports.append(customer_transport2)

    for customer_transport in customer_transports:
        customer_id = customer_transport.customer_id
        transport_id = customer_transport.transport_id

        for customer in customers:
            if customer.id == customer_id:
                print("Покупатель:", customer.name)

        for transport in transports:
            if isinstance(transport, Electro) and transport_id == 1:
                print("Транспортное средство: электрокар")
            elif isinstance(transport, Classic) and transport_id == 2:
                print("Транспортное средство: классический автомобиль")

        print()

if __name__ == "__main__":
    main()
