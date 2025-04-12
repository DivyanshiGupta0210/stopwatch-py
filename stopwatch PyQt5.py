import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QPushButton
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QTimer, QTime, Qt

class stopwatch(QWidget):
    def __init__(self):
        super().__init__()
        self.time = QTime(0,0,0,0) #hours min sec millisec
        self.time_label = QLabel("00:00:00.00", self)
        self.start_button = QPushButton("START", self)
        self.stop_button = QPushButton("STOP", self)
        self.reset_button = QPushButton("RESET", self)
        self.timer = QTimer(self)
        self.initUI() 

    def initUI(self):
        self.setWindowTitle("Stopwatch")
        # self.setWindowIcon(QIcon(" ")) #lrelative path location of the icon
        self.setGeometry(370,150,600,200)  

        vbox = QVBoxLayout()
        vbox.addWidget(self.time_label)
        vbox.addWidget(self.start_button)
        vbox.addWidget(self.stop_button)
        vbox.addWidget(self.reset_button)
        self.start_button.setGeometry(450,450,150,100)
        self.setLayout(vbox)
        self.time_label.setAlignment(Qt.AlignCenter)

        hbox = QHBoxLayout()
        # hbox.addWidget(self.start_button)
        # hbox.addWidget(self.stop_button)
        # hbox.addWidget(self.reset_button)
        # self.setLayout(hbox)
        vbox.addLayout(hbox)

        self.setStyleSheet("""
            QPushButton, QLabel{
                padding:20px;
                           font-weight: bold}
            QPushButton{
                font-size: 46px;}    
            QLabel{
                font-size: 100px;
                background-color: #808080;
                           border-radius: 20px}               
        """)

        self.start_button.clicked.connect(self.start)
        self.stop_button.clicked.connect(self.stop)
        self.reset_button.clicked.connect(self.reset)
        self.timer.timeout.connect(self.update_display)

    def start(self):
        self.timer.start(10)

    def stop(self):
        self.timer.stop()

    def reset(self):
        self.timer.stop()
        self.time = QTime(0,0,0,0)
        self.time_label.setText(self.format_time(self.time))

    def format_time(self, time):
        hours = time.hour()
        minutes = time.minute()
        seconds = time.second()
        milliseconds = time.msec() // 10 #to get upto 2 digits

        return f"{hours:02}:{minutes:02}:{seconds:02}.{milliseconds:02}"

    def update_display(self):
        self.time = self.time = self.time.addMSecs(10) 
        self.time_label.setText(self.format_time(self.time))        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    stopwatch = stopwatch() 
    stopwatch.show() 
    sys.exit(app.exec_())

