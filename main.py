# Import the required packages.
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, \
    QVBoxLayout, QHBoxLayout, QPushButton, QLabel
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtCore import QEvent, QSize, QObject, Qt
from PyQt5 import QtCore
import sys


class MainWindow(QMainWindow):

    push_button_size = QSize(450, 35)

    push_button_sunken_style = "color: rgb(255, 255, 255);" \
                               "font: 75 10pt FreeSans;" \
                               "background-color: rgba(6, 104, 249, 200);" \
                               "border-top-color: rgba(4, 57, 135, 200);" \
                               "border-left-color: rgba(4, 57, 135, 200);" \
                               "border-right-color: rgba(151, 222, 247, 200);" \
                               "border-bottom-color: rgba(151, 222, 247, 200);" \
                               "border-style: solid;" \
                               "border-top-width: 3px;" \
                               "border-left-width: 3px;" \
                               "border-right-width: 2px;" \
                               "border-bottom-width: 2px;" \
                               "border-radius: 5px;"

    push_button_risen_style = "color: rgb(255, 255, 255);" \
                              "font: 75 10pt FreeSans;" \
                              "background-color: rgba(6, 104, 249, 200);" \
                              "border-top-color: rgba(151, 222, 247, 200);" \
                              "border-left-color: rgba(151, 222, 247, 200);" \
                              "border-right-color: rgba(4, 57, 135, 200);" \
                              "border-bottom-color: rgba(4, 57, 135, 200);" \
                              "border-style: solid;" \
                              "border-top-width: 2px;" \
                              "border-left-width: 2px;" \
                              "border-right-width: 3px;" \
                              "border-bottom-width: 3px;" \
                              "border-radius: 5px;"

    push_button_enter_style = "color: rgb(255, 255, 255);" \
                              "font: 75 12pt FreeSans;" \
                              "background-color: rgba(6, 104, 249, 200);" \
                              "border-top-color: rgba(151, 222, 247, 200);" \
                              "border-left-color: rgba(151, 222, 247, 200);" \
                              "border-right-color: rgba(4, 57, 135, 200);" \
                              "border-bottom-color: rgba(4, 57, 135, 200);" \
                              "border-style: solid;" \
                              "border-top-width: 2px;" \
                              "border-left-width: 2px;" \
                              "border-right-width: 3px;" \
                              "border-bottom-width: 3px;" \
                              "border-radius: 6px;"

    push_button_leave_style = "color: rgb(255, 255, 255);" \
                              "font: 75 10pt FreeSans;" \
                              "background-color: rgba(6, 104, 249, 200);" \
                              "border-top-color: rgba(151, 222, 247, 200);" \
                              "border-left-color: rgba(151, 222, 247, 200);" \
                              "border-right-color: rgba(4, 57, 135, 200);" \
                              "border-bottom-color: rgba(4, 57, 135, 200);" \
                              "border-style: solid;" \
                              "border-top-width: 2px;" \
                              "border-left-width:2px;" \
                              "border-right-width: 3px;" \
                              "border-bottom-width: 3px;" \
                              "border-radius: 5px;"

    push_button_enter_style_2 = "color: rgb(255, 255, 255);" \
                                "font: 75 12pt FreeSans;" \
                                "background-color: rgba(6, 104, 249, 200);" \
                                "border-top-color: rgba(151, 222, 247, 200);" \
                                "border-left-color: rgba(151, 222, 247, 200);" \
                                "border-right-color: rgba(4, 57, 135, 200);" \
                                "border-bottom-color: rgba(4, 57, 135, 200);" \
                                "border-style: solid;" \
                                "border-top-width: 2px;" \
                                "border-left-width: 2px;" \
                                "border-right-width: 3px;" \
                                "border-bottom-width: 3px;" \
                                "border-radius: 6px;"

    def __init__(self) -> None:
        super(MainWindow, self).__init__()

        # Create an instance of a QLabel class.
        label_1 = QLabel("The style of this button is changed by: \nmouse press and mouse release events")
        # Create an instance of a QPushButton class.
        self.button_1 = QPushButton()
        self.button_1.setText("Button 1")
        self.button_1.setObjectName("Button 1")
        self.button_1.setFixedSize(self.push_button_size)
        self.button_1.setStyleSheet(self.push_button_risen_style)
        self.button_1.installEventFilter(self)
        # Create an instance of a QHBoxLayout class.
        button_vertical_layout_1 = QVBoxLayout()
        button_vertical_layout_1.setContentsMargins(0, 10, 0, 0)
        button_vertical_layout_1.addWidget(label_1, alignment=Qt.AlignCenter)
        button_vertical_layout_1.addWidget(self.button_1, alignment=Qt.AlignCenter)
        button_vertical_layout_1.addStretch(1)

        # Create an instance of a QLabel class.
        label_2 = QLabel("The style of this button is changed by: \nmouse hover enter and mouse hover leave events")
        # Create an instance of a QPushButton class.
        self.button_2 = QPushButton()
        self.button_2.setText("Button 2")
        self.button_2.setObjectName("Button 2")
        self.button_2.setFixedSize(self.push_button_size)
        self.button_2.setStyleSheet(self.push_button_risen_style)
        self.button_2.installEventFilter(self)
        # Create an instance of a QHBoxLayout class.
        button_vertical_layout_2 = QVBoxLayout()
        button_vertical_layout_2.setContentsMargins(0, 10, 0, 0)
        button_vertical_layout_2.addWidget(label_2, alignment=Qt.AlignCenter)
        button_vertical_layout_2.addWidget(self.button_2, alignment=Qt.AlignCenter)
        button_vertical_layout_2.addStretch(1)

        # Create an instance of a QLabel class.
        label_3 = QLabel("The style of this button is changed by: "
                         "\nmouse pressed, released, hover enter, and hover leave events")
        # Create an instance of a QPushButton class.
        self.button_3 = QPushButton()
        self.button_3.setText("Button 3")
        self.button_3.setObjectName("Button 3")
        self.button_3.setFixedSize(self.push_button_size)
        self.button_3.setStyleSheet(self.push_button_risen_style)
        self.button_3.installEventFilter(self)
        # Create an instance of a QHBoxLayout class.
        button_vertical_layout_3 = QVBoxLayout()
        button_vertical_layout_3.setContentsMargins(0, 10, 0, 0)
        button_vertical_layout_3.addWidget(label_3, alignment=Qt.AlignCenter)
        button_vertical_layout_3.addWidget(self.button_3, alignment=Qt.AlignCenter)
        button_vertical_layout_3.addStretch(1)

        # Create an instance of a QVBoxLayout class.
        horizontal_layout = QVBoxLayout()
        horizontal_layout.setContentsMargins(0, 0, 0, 0)
        horizontal_layout.addLayout(button_vertical_layout_1)
        horizontal_layout.addLayout(button_vertical_layout_2)
        horizontal_layout.addLayout(button_vertical_layout_3)

        # Create an instance of a QWidget class.
        self.widget = QWidget(self)
        self.widget.setLayout(horizontal_layout)
        self.setCentralWidget(self.widget)
        self.setFixedSize(620, 300)
        # self.setStyleSheet("QLabel {font: 75 11pt FreeSans;}")
        self.setStyleSheet("font: 75 11pt FreeSans;")
        self.setWindowIcon(QIcon(QPixmap("python-logo.png")))
        self.setWindowTitle("Change the style of a widget (PushButton) reimplementing the eventFilter method")
        self.statusBar().showMessage("")

    # Override method for class MainWindow.
    def eventFilter(self, source: QObject, event: QEvent) -> bool:
        # If a mouse press event has occurred.
        if event.type() == QtCore.QEvent.MouseButtonPress:
            # If the originator of the event is a QPushButton.
            if isinstance(source, QPushButton) and (source.objectName() == "Button 1" or
                                                    source.objectName() == "Button 3"):
                source.setStyleSheet(self.push_button_sunken_style)
                source.setText("Mouse pressed event")
                return True
        # If a mouse release event has occurred.
        elif event.type() == QtCore.QEvent.MouseButtonRelease:
            # If the originator of the event is a QPushButton.
            if isinstance(source, QPushButton) and (source.objectName() == "Button 1" or
                                                    source.objectName() == "Button 3"):
                source.setStyleSheet(self.push_button_risen_style)
                source.setText("Mouse released event")
                return True
        #
        elif event.type() == QtCore.QEvent.Enter:
            # If the originator of the event is a QPushButton.
            if isinstance(source, QPushButton) and (source.objectName() == "Button 2" or
                                                    source.objectName() == "Button 3"):
                source.setStyleSheet(self.push_button_enter_style)
                source.setText("Mouse enter event")
                return True
        #
        elif event.type() == QtCore.QEvent.Leave:
            # If the originator of the event is a QPushButton.
            if isinstance(source, QPushButton) and (source.objectName() == "Button 2" or
                                                    source.objectName() == "Button 3"):
                source.setStyleSheet(self.push_button_leave_style)
                source.setText("Mouse leave event")
                return True
        else:
            return False
        return False


def main() -> None:
    # Create a QApplication object. It manages the GUI application's control flow and main settings.
    # It handles widget specific initialization, finalization.
    # For any GUI application using Qt, there is precisely one QApplication object
    app = QApplication(sys.argv)
    # Create an instance of the class MainWindow.
    window = MainWindow()
    # Show the window.
    window.show()
    # Start Qt event loop.
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()

