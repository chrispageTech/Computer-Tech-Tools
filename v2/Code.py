import sys
import shelve
import subprocess
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QImage, QPixmap, QFont
from PyQt5.QtWidgets import (QApplication, QGridLayout, QLabel, QMainWindow,
                             QPushButton, QVBoxLayout, QWidget, QLineEdit)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        font = QFont("Comic Sans MS", 16, QFont.Bold)
        fontBut = QFont("Comic Sans MS", 12, QFont.Bold)

        # Set the window properties
        self.setWindowTitle("Alpha Tech Tools")
        self.setGeometry(100, 100, 240, 400)

        # Create the label to hold the background image
        self.label = QLabel(self)
        self.label.setGeometry(0, 0, 400, 600)
        self.label.setAlignment(Qt.AlignLeft)

        # Set the background image
        image = QImage("background.jpg")
        self.label.setPixmap(QPixmap.fromImage(image))

        # Create the main widget and set the layout
        self.main_widget = QWidget(self)
        self.setCentralWidget(self.main_widget)
        self.layout = QVBoxLayout(self.main_widget)

        # Create the grid layout for the buttons
        self.button_grid = QGridLayout()
        self.layout.addLayout(self.button_grid)

        # Create the buttons
        self.button1 = QPushButton("Button 1", self.main_widget)
        self.button1.setMinimumSize(QSize(150, 80))
        self.button1.setMaximumSize(QSize(150, 80))
        self.button2 = QPushButton("Button 2", self.main_widget)
        self.button2.setMinimumSize(QSize(150, 80))
        self.button2.setMaximumSize(QSize(150, 80))
        self.button3 = QPushButton("Button 3", self.main_widget)
        self.button3.setMinimumSize(QSize(150, 80))
        self.button3.setMaximumSize(QSize(150, 80))
        self.button4 = QPushButton("Button 4", self.main_widget)
        self.button4.setMinimumSize(QSize(150, 80))
        self.button4.setMaximumSize(QSize(150, 80))
        self.button5 = QPushButton("Button 5", self.main_widget)
        self.button5.setMinimumSize(QSize(150, 80))
        self.button5.setMaximumSize(QSize(150, 80))
        self.button6 = QPushButton("Button 6", self.main_widget)
        self.button6.setMinimumSize(QSize(150, 80))
        self.button6.setMaximumSize(QSize(150, 80))
        self.button7 = QPushButton("Button 7", self.main_widget)
        self.button7.setMinimumSize(QSize(150, 80))
        self.button7.setMaximumSize(QSize(150, 80))
        self.button8 = QPushButton("Button 8", self.main_widget)
        self.button8.setMinimumSize(QSize(150, 80))
        self.button8.setMaximumSize(QSize(150, 80))
        self.buttonconfig = QPushButton("Configuration", self.main_widget)
        self.buttonconfig.setMinimumSize(QSize(150, 80))
        self.buttonreset = QPushButton("Reset", self.main_widget)
        self.buttonreset.setMinimumSize(QSize(150, 80))



        # Labels for each button
        self.label1 = QLabel("1", self.main_widget)
        self.label1.setFont(font)
        self.label2 = QLabel("2", self.main_widget)
        self.label2.setFont(font)
        self.label3 = QLabel("3", self.main_widget)
        self.label3.setFont(font)
        self.label4 = QLabel("4", self.main_widget)
        self.label4.setFont(font)
        self.label5 = QLabel("5", self.main_widget)
        self.label5.setFont(font)
        self.label6 = QLabel("6", self.main_widget)
        self.label6.setFont(font)
        self.label7 = QLabel("7", self.main_widget)
        self.label7.setFont(font)
        self.label8 = QLabel("8", self.main_widget)
        self.label8.setFont(font)

                # Create the shelve database for storing information
        self.db = shelve.open("Database")

         # Set the buttons' colors to green
        color1 = self.db["color1"]
        color2 = self.db["color2"]
        color3 = self.db["color3"]
        color4 = self.db["color4"]
        color5 = self.db["color5"]
        color6 = self.db["color6"]
        color7 = self.db["color7"]
        color8 = self.db["color8"]
        self.button1.setStyleSheet(color1)
        self.button1.setFont(fontBut)
        self.button2.setStyleSheet(color2)
        self.button2.setFont(fontBut)
        self.button3.setStyleSheet(color3)
        self.button3.setFont(fontBut)
        self.button4.setStyleSheet(color4)
        self.button4.setFont(fontBut)
        self.button5.setStyleSheet(color5)
        self.button5.setFont(fontBut)
        self.button6.setStyleSheet(color6)
        self.button6.setFont(fontBut)
        self.button7.setStyleSheet(color7)
        self.button7.setFont(fontBut)
        self.button8.setStyleSheet(color8)
        self.button8.setFont(fontBut)
        self.buttonconfig.setStyleSheet("background-color: blue")
        self.buttonconfig.setFont(fontBut)
        self.buttonreset.setStyleSheet("background-color: yellow")
        self.buttonreset.setFont(fontBut)

                # Add the buttons to the grid layout
        self.button_grid.addWidget(self.label1, 0, 0)
        self.button_grid.addWidget(self.label2, 0, 2)
        self.button_grid.addWidget(self.label3, 1, 0)
        self.button_grid.addWidget(self.label4, 1, 2)
        self.button_grid.addWidget(self.label5, 2, 0)
        self.button_grid.addWidget(self.label6, 2, 2)
        self.button_grid.addWidget(self.label7, 3, 0)
        self.button_grid.addWidget(self.label8, 3, 2)
        self.button_grid.addWidget(self.button1, 0, 1)
        self.button_grid.addWidget(self.button2, 0, 3)
        self.button_grid.addWidget(self.button3, 1, 1)
        self.button_grid.addWidget(self.button4, 1, 3)
        self.button_grid.addWidget(self.button5, 2, 1)
        self.button_grid.addWidget(self.button6, 2, 3)
        self.button_grid.addWidget(self.button7, 3, 1)
        self.button_grid.addWidget(self.button8, 3, 3)
        self.button_grid.addWidget(self.buttonconfig, 4, 1)
        self.button_grid.addWidget(self.buttonreset, 4, 3)

        # Connect the buttons to the appropriate functions
        self.button1.clicked.connect(self.open_program1)
        self.button2.clicked.connect(self.open_program2)
        self.button3.clicked.connect(self.open_program3)
        self.button4.clicked.connect(self.open_program4)
        self.button5.clicked.connect(self.open_program5)
        self.button6.clicked.connect(self.open_program6)
        self.button7.clicked.connect(self.open_program7)
        self.button8.clicked.connect(self.open_program8)
        self.buttonconfig.clicked.connect(self.open_config)
        self.buttonreset.clicked.connect(self.reset_clicked)

        # Load the button names and colors from the database, if they exist
        try:
            self.button1.setText(self.db["button1"])
            self.button2.setText(self.db["button2"])
            self.button3.setText(self.db["button3"])
            self.button4.setText(self.db["button4"])
            self.button5.setText(self.db["button5"])
            self.button6.setText(self.db["button6"])
            self.button7.setText(self.db["button7"])
            self.button8.setText(self.db["button8"])

        except KeyError:
            pass
    def reset_clicked(self):
        color = "background-color: green;"
        self.db["color1"] = color
        self.db["color2"] = color
        self.db["color3"] = color
        self.db["color4"] = color
        self.db["color5"] = color
        self.db["color6"] = color
        self.db["color7"] = color
        self.db["color8"] = color
        self.button1.setStyleSheet(color)
        self.button2.setStyleSheet(color)
        self.button3.setStyleSheet(color)
        self.button4.setStyleSheet(color)
        self.button5.setStyleSheet(color)
        self.button6.setStyleSheet(color)
        self.button7.setStyleSheet(color)
        self.button8.setStyleSheet(color)

    def open_program1(self):
        color1 = "background-color: red;"
        self.db["color1"] = color1
        self.button1.setStyleSheet(color1)
        program_name1 = self.db["program_name1"]
        subprocess.Popen([program_name1])

    def open_program2(self):
        color2 = "background-color: red;"
        self.db["color2"] = color2
        self.button1.setStyleSheet(color2)
        program_name2 = self.db["program_name2"]
        subprocess.Popen([program_name2])
        self.button2.setStyleSheet("background-color: red;")

    def open_program3(self):
        color3 = "background-color: red;"
        self.db["color3"] = color3
        self.button1.setStyleSheet(color3)
        program_name3 = self.db["program_name3"]
        subprocess.Popen([program_name3])
        self.button3.setStyleSheet("background-color: red;")

    def open_program4(self):
        color4 = "background-color: red;"
        self.db["color4"] = color4
        self.button1.setStyleSheet(color4)
        program_name4 = self.db["program_name4"]
        subprocess.Popen([program_name4])
        self.button4.setStyleSheet("background-color: red;")

    def open_program5(self):
        color5 = "background-color: red;"
        self.db["color5"] = color5
        self.button1.setStyleSheet(color5)
        program_name5 = self.db["program_name5"]
        subprocess.Popen([program_name5], shell=True)
        self.button5.setStyleSheet("background-color: red;")

    def open_program6(self):
        color6 = "background-color: red;"
        self.db["color6"] = color6
        self.button1.setStyleSheet(color6)
        program_name6 = self.db["program_name6"]
        subprocess.Popen([program_name6])
        self.button6.setStyleSheet("background-color: red;")

    def open_program7(self):
        color7 = "background-color: red;"
        self.db["color7"] = color7
        self.button1.setStyleSheet(color7)
        program_name7 = self.db["program_name7"]
        subprocess.Popen([program_name7])
        self.button7.setStyleSheet("background-color: red;")

    def open_program8(self):
        color8 = "background-color: red;"
        self.db["color8"] = color8
        self.button1.setStyleSheet(color8)
        self.button8.setStyleSheet("background-color: red;")
        program_name8 = self.db["program_name8"]
        subprocess.Popen([program_name8])
        
    def open_config(self):
        name_change_window.show()


class NameChangeWindow(QMainWindow):
    def __init__(self, main_window):
        super().__init__()

        # Store a reference to the main window
        self.main_window = main_window

        # Set the window properties
        self.setWindowTitle("Button Configuration")
        self.setGeometry(100, 100, 200, 200)

        # Create the main widget and set the layout
        self.main_widget = QWidget(self)
        self.setCentralWidget(self.main_widget)
        self.layout = QVBoxLayout(self.main_widget)

        # Create the change button name button
        self.change_button = QPushButton("Confirm", self.main_widget)
        self.change_button.clicked.connect(self.change_button_name)
        self.layout.addWidget(self.change_button)

        # Create the label inputs
        self.name_input = QLineEdit(self.main_widget)
        self.name_label = QLabel("Enter the new button name:", self.main_widget)
        self.number_input = QLineEdit(self.main_widget)
        self.number_label = QLabel("Enter the button number (1-8):", self.main_widget)
        self.program_input = QLineEdit(self.main_widget)
        self.program_label = QLabel("Enter the new program path", self.main_widget)

        # Add the label inputs to the layout
        self.layout.addWidget(self.name_label)
        self.layout.addWidget(self.name_input)
        self.layout.addWidget(self.number_label)
        self.layout.addWidget(self.number_input)
        self.layout.addWidget(self.program_label)
        self.layout.addWidget(self.program_input)

    def change_button_name(self):
        """Changes the name of a button in the main window."""
        # Get the new button name and button number
        button_name = self.name_input.text()
        button_number = int(self.number_input.text())
        program_name = self.program_input.text()

        # Change the name of the button
        if button_number == 1:
            self.main_window.button1.setText(button_name)
            self.main_window.db["button1"] = button_name
            self.main_window.db["program_name1"] = program_name
        elif button_number == 2:
            self.main_window.button2.setText(button_name)
            self.main_window.db["button2"] = button_name
            self.main_window.db["program_name2"] = program_name
        elif button_number == 3:
            self.main_window.button3.setText(button_name)
            self.main_window.db["button3"] = button_name
            self.main_window.db["program_name3"] = program_name
        elif button_number == 4:
            self.main_window.button4.setText(button_name)
            self.main_window.db["button4"] = button_name
            self.main_window.db["program_name4"] = program_name
        elif button_number == 5:
            self.main_window.button5.setText(button_name)
            self.main_window.db["button5"] = button_name
            self.main_window.db["program_name5"] = program_name
        elif button_number == 6:
            self.main_window.button6.setText(button_name)
            self.main_window.db["button6"] = button_name
            self.main_window.db["program_name6"] = program_name
        elif button_number == 7:
            self.main_window.button7.setText(button_name)
            self.main_window.db["button7"] = button_name
            self.main_window.db["program_name7"] = program_name
        elif button_number == 8:
            self.main_window.button8.setText(button_name)
            self.main_window.db["button8"] = button_name
            self.main_window.db["program_name8"] = program_name

            # Save the changes to the database
            self.main_window.db.sync()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    name_change_window = NameChangeWindow(main_window)
    sys.exit(app.exec_())