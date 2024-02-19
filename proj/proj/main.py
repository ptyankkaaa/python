import sys
import random
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout, QWidget, QLineEdit
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PIL import Image

class RandomImageApp(QMainWindow):
    def __init__(self):
        super(RandomImageApp, self).__init__()

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Random Image App')
        self.setGeometry(100, 100, 400, 300)

    
        
        self.result_label = QLabel('Введите число чтоб играть: ', self)
        self.new_roll_label = QLabel('', self)
        self.new_roll_label.setAlignment(Qt.AlignCenter)
        
        self.input_number = QLineEdit(self)
        
    
        # Создаем виджет и размещаем его на главном окне
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        # Создаем макет вертикального расположения для виджета
        layout = QVBoxLayout(central_widget)

        # Создаем метку для отображения изображения
        self.image_label = QLabel(self)
        self.image_label.setAlignment(Qt.AlignHCenter)

        # Создаем 4 кнопки для отображения текущего режима игры
        self.button1 = QPushButton('4 грани', self)
        self.button2 = QPushButton('6 граней', self)
        self.button3 = QPushButton('10 граней', self)
        self.button4 = QPushButton('20 граней', self)

        # Подключение слотов к кнопкам
        self.button1.clicked.connect(lambda: self.set_game_mode(4))
        self.button2.clicked.connect(lambda: self.set_game_mode(6))
        self.button3.clicked.connect(lambda: self.set_game_mode(10))
        self.button4.clicked.connect(lambda: self.set_game_mode(20))

        # Добавление кнопок на форму
        layout.addWidget(self.button1)
        layout.addWidget(self.button2)
        layout.addWidget(self.button3)
        layout.addWidget(self.button4)
        
        # Изначально устанавливаем режим игры 
        self.current_game_mode = 6
        self.text_game_mode = QLabel('Выбран режим где 6 гранный кубик.', self)
        self.text_game_mode.setAlignment(Qt.AlignHCenter)
        layout.addWidget(self.text_game_mode)


        layout.addWidget(self.image_label)

        # Создаем кнопку для загрузки рандомного изображения
        
        layout.addWidget(self.result_label)
        layout.addWidget(self.input_number)
        layout.addWidget(self.new_roll_label)
        

        load_button = QPushButton('Бросить кости', self)
        load_button.clicked.connect(self.load_random_image)
        layout.addWidget(load_button)

    def load_random_image(self):
        # Загружаем рандомное изображение
        random_image_path = self.get_random_image_path()
        pixmap = QPixmap(random_image_path)
        self.check_guess(random_image_path)
        self.image_label.setPixmap(pixmap)

    def get_random_image_path(self):
        # Замените путь к вашей папке с изображениями
        image_folder_path = 'images'
        random_int = random.randint(1, self.current_game_mode)
        
        image_folder_path = 'images_' +  str(self.current_game_mode) + '/' + str(random_int) + '.jpg'
        
        # Получаем список файлов в папке
        # image_files = ['images/1.png', 'images/2.png', 'images/3.png', 'images/4.png', 'images/5.png', 'images/6.png']

        # # Выбираем рандомное изображение
        # random_image_filename = random.choice(image_files)
        # print(random_image_filename.split('/')[1].split('.')[0])
        return image_folder_path

    def check_guess(self, random_image_filename):
        try:
            user_guess = int(self.input_number.text())
            if 1 <= user_guess <= self.current_game_mode:
                generated_result = int(random_image_filename.split('/')[1].split('.')[0])
                if user_guess == generated_result:
                    self.new_roll_label.setText('Поздравляю! Вы угадали!')
                else:
                    self.new_roll_label.setText('Попробуйте еще раз. Не угадали.')
            else:
                self.new_roll_label.setText(f'Введите число от 1 до {self.current_game_mode}')
        except ValueError:
            self.new_roll_label.setText('Введите целое число.')


    
    def set_game_mode(self, mode):
        # Устанавливаем текущий режим игры
        self.current_game_mode = mode
        if mode == 4:
            self.text_game_mode.setText('Выбран режим где 4 гранный кубик.')
        elif mode == 6:
            self.text_game_mode.setText('Выбран режим где 6 гранный кубик.')
        elif mode == 10:
            self.text_game_mode.setText('Выбран режим где 10 гранный кубик.')
        elif mode == 20:
            self.text_game_mode.setText('Выбран режим где 20 гранный кубик.')
        print(f"Current Game Mode: {mode}")



if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_app = RandomImageApp()
    main_app.show()
    sys.exit(app.exec_())
