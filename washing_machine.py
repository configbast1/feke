from dataclasses import dataclass


@dataclass
class WashingMachine:
    brand: str
    socks: int
    lost_socks: int
    is_noisy: bool

    def eat_sock(self):
        self.socks -= 1
        self.lost_socks += 1
        print(f"{self.brand}: Ням! Я з'їла шкарпетку. Всього зникло: {self.lost_socks}")

    def spin(self):
        print(f"{self.brand}: Віджим! Їду на кухню, шкарпеток усередині: {self.socks}")

    def beep(self):
        if self.is_noisy:
            print(f"{self.brand}: Третя ночі, прання завершено!")
        else:
            print(f"{self.brand}: Тихенько завершила прання.")

    def deny(self):
        print(f"{self.brand}: Шкарпеток зникло: {self.lost_socks}? Це не я, це кіт.")


def main():
    bosch = WashingMachine("Bosch", 6, 0, True)
    indesit = WashingMachine("Indesit", 3, 42, False)
    samsung = WashingMachine("Samsung", 10, 5, True)

    for machine in [bosch, indesit, samsung]:
        machine.eat_sock()
        machine.spin()
        machine.beep()
        machine.deny()
        print()


if __name__ == "__main__":
    main()
