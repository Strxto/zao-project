import pandas as pd
import os
from datetime import datetime

class ExcelManager:
    def __init__(self, filename='orders.xlsx'):
        self.filename = filename
        self._initialize_file()

    def _initialize_file(self):
        """Создает файл Excel с нужными колонками если его нет"""
        if not os.path.exists(self.filename):
            df = pd.DataFrame(columns=[
                'Номер заказа',
                'ФИО',
                'Адрес',
                'Ссылка на ваш телеграм аккаунт (для связи)',
                'Ваш размер',
                'Стоимость товара',
                'Фото с размером и ценой',
                'Ссылка на товар с правильным размером',
                'Оплата',
                'Статус заказа',
                'Дата создания'
            ])
            df.to_excel(self.filename, index=False, engine='openpyxl')

    def add_order(self, order_data):
        """Добавляет новый заказ"""
        try:
            df = pd.read_excel(self.filename)

            # Добавляем дату создания
            order_data['Дата создания'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

            # Добавляем новую строку
            new_row = pd.DataFrame([order_data])
            df = pd.concat([df, new_row], ignore_index=True)

            # Сохраняем
            df.to_excel(self.filename, index=False, engine='openpyxl')
            return True
        except Exception as e:
            print(f"Ошибка при добавлении заказа: {e}")
            return False