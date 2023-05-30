import sys


from PyQt5.QtWidgets import QApplication


from view.main import MainView


def main():
    app = QApplication([])
    MainView()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
