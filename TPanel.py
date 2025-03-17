from PyQt5.QtWidgets import QMainWindow, QWidget, QFileDialog, QPushButton, QTableWidget, QTableWidgetItem, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox, QAction
import re
from TControl import TControl
from TAbout import TAbout

class TPanel(QMainWindow):
    def __init__(self):
        super().__init__()
        self.control = TControl()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Телефонная книга")
        self.setGeometry(100, 100, 500, 400) 

        # Основной виджет
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)
        
        self.table_widget = QTableWidget()  # Используем QTableWidget вместо QListWidget
        self.table_widget.setColumnCount(2)
        self.table_widget.setHorizontalHeaderLabels(["Имя", "Номер"])
        self.load_contacts()
        
        # Устанавливаем ширину колонок
        self.table_widget.setColumnWidth(0, 185)  # Ширина колонки для имени (можно настроить по желанию)
        self.table_widget.setColumnWidth(1, 199)  # Ширина колонки для номера, чтобы номер был виден полностью

        # Устанавливаем размер самой таблицы
        self.table_widget.setFixedSize(400, 300)  # Задаем фиксированные размеры для таблицы (ширина и высота)

        self.name_input = QLineEdit()
        self.number_input = QLineEdit()

        # Регулярный выражение для валидации ввода номера
        self.number_input.setMaxLength(18)  # Максимальная длина номера с форматированием
        self.number_input.textChanged.connect(self.format_phone_input)

        self.add_button = QPushButton("Добавить")
        self.add_button.setFixedSize(100, 30)
        self.add_button.setToolTip("Добавить новый контакт")
        self.add_button.clicked.connect(self.add_contact)
        
        self.remove_button = QPushButton("Удалить")
        self.remove_button.setFixedSize(100, 30)
        self.remove_button.setToolTip("Удалить выбранный контакт")
        self.remove_button.clicked.connect(self.remove_contact)
        
        self.clear_button = QPushButton("Очистить")
        self.clear_button.setFixedSize(100, 30)
        self.clear_button.setToolTip("Очистить всю книгу контактов")
        self.clear_button.clicked.connect(self.clear_contacts)
        
        self.save_button = QPushButton("Сохранить")
        self.save_button.setFixedSize(100, 30)
        self.save_button.setToolTip("Сохранить контакты в файл")
        self.save_button.clicked.connect(self.save_contacts)
        
        self.load_button = QPushButton("Загрузить")
        self.load_button.setFixedSize(100, 30)
        self.load_button.setToolTip("Загрузить контакты из файла")
        self.load_button.clicked.connect(self.load_contacts)
        
        self.edit_button = QPushButton("Изменить")
        self.edit_button.setFixedSize(100, 30)
        self.edit_button.setToolTip("Изменить выбранный контакт")
        self.edit_button.clicked.connect(self.edit_contact)
        
        self.find_button = QPushButton("Найти")
        self.find_button.setFixedSize(100, 30)
        self.find_button.setToolTip("Поиск контакта по имени и номеру")
        self.find_button.clicked.connect(self.find_contact)
        
        form_layout = QHBoxLayout()
        form_layout.addWidget(QLabel("ФИО"))
        form_layout.addWidget(self.name_input)
        form_layout.addWidget(QLabel("Номер"))
        form_layout.addWidget(self.number_input)
        form_layout.addWidget(self.add_button)
        
        button_layout = QVBoxLayout()
        button_layout.addWidget(self.remove_button)
        button_layout.addWidget(self.clear_button)
        button_layout.addWidget(self.save_button)
        button_layout.addWidget(self.load_button)
        button_layout.addWidget(self.edit_button)
        button_layout.addWidget(self.find_button)

        # Основной layout
        main_layout = QHBoxLayout()  # Используем QHBoxLayout, чтобы располагать элементы горизонтально
        main_layout.addWidget(self.table_widget)  # Таблица слева
        main_layout.addStretch(1)  # Добавляем растяжку, чтобы кнопки были справа
        main_layout.addLayout(button_layout)  # Кнопки справа от таблицы
        
        # И добавляем форму с полями для ввода внизу
        form_layout_bottom = QVBoxLayout()
        form_layout_bottom.addLayout(form_layout)
        
        # Основной вертикальный layout
        final_layout = QVBoxLayout()
        final_layout.addLayout(main_layout)  # Добавляем горизонтальный layout с таблицей и кнопками
        final_layout.addLayout(form_layout_bottom)  # Форма для ввода будет под таблицей
        
        central_widget.setLayout(final_layout)

        # Создание меню
        self.create_menu()

    def create_menu(self):
        """Метод для создания меню"""
        menubar = self.menuBar()
        help_menu = menubar.addMenu("Справка")

        about_action = QAction("О программе", self)
        about_action.triggered.connect(self.show_about)
        help_menu.addAction(about_action)

    def show_about(self):
        """Метод для отображения окна справки"""
        about_window = TAbout()  # Создаем экземпляр окна справки
        about_window.exec_()  # Открываем окно в модальном режиме
    
    def format_phone_input(self):
        """Автоматически форматирует номер телефона"""
        phone = self.number_input.text()
        
        # Убираем все символы, кроме цифр
        phone = re.sub(r'[^0-9]', '', phone)
        
        # Ограничиваем номер 11 цифрами
        if len(phone) > 11:
            phone = phone[:11]
        
        # Форматируем номер в +7 (XXX) XXX-XX-XX
        formatted_phone = "+7 "
        if len(phone) > 1:
            formatted_phone += f"({phone[1:4]}) "
        if len(phone) > 4:
            formatted_phone += f"{phone[4:7]}-"
        if len(phone) > 7:
            formatted_phone += f"{phone[7:9]}-"
        if len(phone) > 9:
            formatted_phone += phone[9:11]
        
        self.number_input.setText(formatted_phone)
        # Теперь не устанавливаем курсор в конец, чтобы пользователь мог редактировать

    
    def add_contact(self):
        name = self.name_input.text()
        number = self.number_input.text()

        # Проверяем, что имя и номер не пустые
        if name and number:
            # Форматируем номер перед сохранением
            self.control.add_contact(name, number)
            self.update_table()
            self.name_input.clear()
            self.number_input.clear()
        else:
            QMessageBox.warning(self, "Ошибка", "Пожалуйста, заполните все поля!")
    
    def remove_contact(self):
        selected = self.table_widget.currentRow()
        if selected >= 0:
            self.control.remove_contact(selected)
            self.update_table()
    
    def clear_contacts(self):
        self.control.clear_contacts()
        self.update_table()
    
    def save_contacts(self):
        options = QFileDialog.Options()
        filename, _ = QFileDialog.getSaveFileName(self, "Сохранить контакты", "", "JSON Files (*.json);;All Files (*)", options=options)
        if filename:
            self.control.save_contacts(filename)
            QMessageBox.information(self, "Сохранение", "Контакты сохранены!")
    
    def load_contacts(self):
        options = QFileDialog.Options()
        filename, _ = QFileDialog.getOpenFileName(self, "Загрузить контакты", "", "JSON Files (*.json);;All Files (*)", options=options)
        if filename:
            self.control.load_contacts(filename)
            self.update_table()
    
    def update_table(self):
        self.table_widget.setRowCount(len(self.control.abonent_list.contacts))  # Обновляем количество строк
        for row, abonent in enumerate(self.control.abonent_list.contacts):
            self.table_widget.setItem(row, 0, QTableWidgetItem(abonent.name))
            self.table_widget.setItem(row, 1, QTableWidgetItem(abonent.number))
    
    def edit_contact(self):
        selected = self.table_widget.currentRow()
        if selected >= 0:
            name = self.name_input.text()
            number = self.number_input.text()

            if name and number:
                # Форматируем номер перед сохранением
                abonent = self.control.abonent_list.contacts[selected]
                abonent.name = name
                abonent.number = number  # Сохраняем номер в нужном формате
                self.update_table()  # Обновляем таблицу
                self.name_input.clear()
                self.number_input.clear()
    
    def find_contact(self):
        name = self.name_input.text()
        number = self.number_input.text()
        index = self.control.find_contact(name, number)
        if index >= 0:
            QMessageBox.information(self, "Найдено", f"Контакт найден: {self.control.abonent_list.contacts[index].name}, {self.control.abonent_list.contacts[index].number}")
        else:
            QMessageBox.warning(self, "Не найдено", "Контакт не найден!")