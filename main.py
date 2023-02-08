import pandas as pd
import sys

from PyQt6.QtWidgets import QApplication, QMainWindow, QComboBox, QWidget, QVBoxLayout, QLabel

pc_accessories = pd.ExcelFile('pc_accessories.xlsx')

hdds_df = pc_accessories.parse('Hdds')
hdds_name = hdds_df['name']
hdds_price = hdds_df['price']

ssds_df = pc_accessories.parse('Ssds')
ssds_name = ssds_df['name']
ssds_price = ssds_df['price']

power_units_df = pc_accessories.parse('PowerUnits')
power_units_name = power_units_df['name']
power_units_price = power_units_df['price']

videocards_df = pc_accessories.parse('Videocards')
videocards_name = videocards_df['name']
videocards_price = videocards_df['price']

soundcards_df = pc_accessories.parse('Soundcards')
soundcards_name = soundcards_df['name']
soundcards_price = soundcards_df['price']

cases_df = pc_accessories.parse('Cases')
cases_name = cases_df['name']
cases_price = cases_df['price']

coolers_df = pc_accessories.parse('Coolers')
coolers_name = coolers_df['name']
coolers_price = coolers_df['price']

motherboards_df = pc_accessories.parse('Motherboards')
motherboards_name = motherboards_df['name']
motherboards_price = motherboards_df['price']

rams_df = pc_accessories.parse('Rams')
rams_name = rams_df['name']
rams_price = rams_df['price']

cpus_df = pc_accessories.parse('Cpus')
cpus_name = cpus_df['name']
cpus_price = cpus_df['price']

hdds = [f'{name}; цена — {price}₽.' for name, price in zip(hdds_name, hdds_price)]
ssds = [f'{name}; цена — {price}₽.' for name, price in zip(ssds_name, ssds_price)]
power_units = [f'{name}; цена — {price}₽.' for name, price in zip(power_units_name, power_units_price)]
videocards = [f'{name}; цена — {price}₽.' for name, price in zip(videocards_name, videocards_price)]
soundcards = [f'{name}; цена — {price}₽.' for name, price in zip(soundcards_name, soundcards_price)]
cases = [f'{name}; цена — {price}₽.' for name, price in zip(cases_name, cases_price)]
coolers = [f'{name}; цена — {price}₽.' for name, price in zip(coolers_name, coolers_price)]
motherboards = [f'{name}; цена — {price}₽.' for name, price in zip(motherboards_name, motherboards_price)]
rams = [f'{name}; цена — {price}₽.' for name, price in zip(rams_name, rams_price)]
cpus = [f'{name}; цена — {price}₽.' for name, price in zip(cpus_name, cpus_price)]

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Pc_Configurator")

        self.hdds_label = QLabel('Жесткие диски.')
        self.hdds_combobox = QComboBox()
        self.hdds_combobox.addItems(hdds)
        self.hdds_combobox.activated.connect(self.count_price)

        self.ssds_label = QLabel('Твердотельные накопители.')
        self.ssds_combobox = QComboBox()
        self.ssds_combobox.addItems(ssds)
        self.ssds_combobox.activated.connect(self.count_price)

        self.power_units_label = QLabel('Блоки питания.')
        self.power_units_combobox = QComboBox()
        self.power_units_combobox.addItems(power_units)
        self.power_units_combobox.activated.connect(self.count_price)

        self.videocards_label = QLabel('Видеокарты.')
        self.videocards_combobox = QComboBox()
        self.videocards_combobox.addItems(videocards)
        self.videocards_combobox.activated.connect(self.count_price)

        self.soundcards_label = QLabel('Звуковые карты.')
        self.soundcards_combobox = QComboBox()
        self.soundcards_combobox.addItems(soundcards)
        self.soundcards_combobox.activated.connect(self.count_price)

        self.cases_label = QLabel('Корпуса.')
        self.cases_combobox = QComboBox()
        self.cases_combobox.addItems(cases)
        self.cases_combobox.activated.connect(self.count_price)

        self.motherboards_label = QLabel('Материнские платы.')
        self.motherboards_combobox = QComboBox()
        self.motherboards_combobox.addItems(motherboards)
        self.motherboards_combobox.activated.connect(self.count_price)

        self.rams_label = QLabel('Блоки оперативной памяти.')
        self.rams_combobox = QComboBox()
        self.rams_combobox.addItems(rams)
        self.rams_combobox.activated.connect(self.count_price)

        self.cpus_label = QLabel('Процессоры.')
        self.cpus_combobox = QComboBox()
        self.cpus_combobox.addItems(cpus)
        self.cpus_combobox.activated.connect(self.count_price)

        #self.price_button = QPushButton('Посчитать сумму')
        #self.price_button.clicked.connect(self.count_price)

        self.price_label = QLabel('Текущая сумма: 58336₽.')

        layout = QVBoxLayout()

        layout.addWidget(self.hdds_label)
        layout.addWidget(self.hdds_combobox)

        layout.addWidget(self.ssds_label)
        layout.addWidget(self.ssds_combobox)

        layout.addWidget(self.power_units_label)
        layout.addWidget(self.power_units_combobox)

        layout.addWidget(self.videocards_label)
        layout.addWidget(self.videocards_combobox)

        layout.addWidget(self.soundcards_label)
        layout.addWidget(self.soundcards_combobox)

        layout.addWidget(self.cases_label)
        layout.addWidget(self.cases_combobox)

        layout.addWidget(self.motherboards_label)
        layout.addWidget(self.motherboards_combobox)

        layout.addWidget(self.rams_label)
        layout.addWidget(self.rams_combobox)

        layout.addWidget(self.cpus_label)
        layout.addWidget(self.cpus_combobox)

        #layout.addWidget(self.price_button)
        layout.addWidget(self.price_label)

        container = QWidget()
        container.setLayout(layout)

        self.setCentralWidget(container)

    def count_price(self):
        hdds_combobox_index = self.hdds_combobox.currentIndex()
        ssds_combobox_index = self.ssds_combobox.currentIndex()
        power_units_combobox_index = self.power_units_combobox.currentIndex()
        videocards_combobox_index = self.videocards_combobox.currentIndex()
        soundcards_combobox_index = self.soundcards_combobox.currentIndex()
        cases_combobox_index = self.cases_combobox.currentIndex()
        motherboards_combobox_index = self.motherboards_combobox.currentIndex()
        rams_combobox_index = self.rams_combobox.currentIndex()
        cpus_combobox_index = self.cpus_combobox.currentIndex()
        
        full_price = (hdds_price[hdds_combobox_index]
        + ssds_price[ssds_combobox_index]
        + power_units_price[power_units_combobox_index]
        + videocards_price[videocards_combobox_index]
        + soundcards_price[soundcards_combobox_index]
        + cases_price[cases_combobox_index]
        + motherboards_price[motherboards_combobox_index]
        + rams_price[rams_combobox_index]
        + cpus_price[cpus_combobox_index])
        
        self.price_label.setText(f'Текущая сумма: {full_price}₽.')

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()