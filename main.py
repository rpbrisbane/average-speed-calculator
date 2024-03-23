import sys
from datetime import datetime
from PyQt6.QtWidgets import QApplication, QLabel, QWidget, QGridLayout, \
    QLineEdit, QPushButton, QComboBox


class SpeedCalculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Average Speed Calculator")
        grid = QGridLayout()

        # Create Widgets
        distance_label = QLabel("Distance:")
        self.distance_line_edit = QLineEdit()

        time_label = QLabel("Time (hours)")
        self.time_line_edit = QLineEdit()

        self.metric_dropbox = QComboBox()
        self.metric_dropbox['value'] = ('Metric (km)', 'Imperial (miles)')

        calculate_button = QPushButton("Calculate Age")
        # calculate_button.clicked.connect(self.calculate_speed())
        self.output_label = QLabel("")

        # Add widgets to grid
        grid.addWidget(distance_label, 0, 0)
        grid.addWidget(self.distance_line_edit, 0, 1)
        grid.addWidget(metric_dropbox, 0, 2)
        grid.addWidget(time_label, 1, 0)
        grid.addWidget(self.time_line_edit, 1, 1)
        grid.addWidget(calculate_button, 2, 1)
        grid.addWidget(self.output_label, 3, 0)

        self.setLayout(grid)

    def calculate_speed(self):
        distance_edit_input = self.distance_line_edit
        time = self.time_line_edit


app = QApplication(sys.argv)
speed_calculator = SpeedCalculator()
speed_calculator.show()
sys.exit(app.exec())
