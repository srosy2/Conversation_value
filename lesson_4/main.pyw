import sys
from PyQt5.QtWidgets import QApplication

# from Model.Model import Money
from Model.under_model import Rubles, Dollars
from Controller.Controller import Controller


def main():
    app = QApplication(sys.argv)

    # создаём модель
    model1 = Rubles(1500, 50)
    model2 = Dollars(150, 20)

    # создаём контроллер и передаём ему ссылку на модель
    Controller(model1, model2)

    app.exec()


if __name__ == '__main__':
    sys.exit(main())
