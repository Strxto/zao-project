from aiogram import F, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery, InputMediaPhoto
from aiogram import types
import app.keyboards as kb
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.storage.memory import MemoryStorage
from app.database import ExcelManager

from datetime import datetime
import random
excel_manager = ExcelManager()

router = Router()

@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer_photo(photo='AgACAgIAAxkBAAMWaCB1-ChpQb5wsMca0PpYIwoPC5AAAvfzMRsl7whJJaRiHrKeNg4BAAMCAAN5AAM2BA',
                               caption='Добро пожаловать в ЗАО "БЕЩЕКИ" Delivery. \n '
                                       ' * Это бот, в котором вы сможете заказать любую вещь с китайского Poizon по цене, от которой китайцы плачут в подушку! \n '
                                       ' * Наша комиссия за перевозку ниже, чем самооценка Зеленского после проебанного Харькова, ведь мы доставляем ваши вещи на ишаках через Гималаи, используя при этом труд Непальских детей практически за бесплатно! \n '
                                       ' * Наша поддержка ответит быстрее, чем вы успеете перенаправить свои сбережения на деп в казике т.к. один из основателей нашей компании долбоеб студент, вылетевший из вуза по неуспеваемости и ему больше нехуй делать. \n '
                                       ' * Наш слоган: Заказываешь в "БЕЩЕКИ" - получаешь радость за обе щеки (и пару проблем с Китайским законодательством ... )',
                               reply_markup=kb.start_menu_button)

@router.message(Command('help'))
async def get_help(message: Message):
    await message.answer('Это команда /help')

@router.message(Command('get_id'))
async def get_id(message: Message):
    await message.answer(f'Твой ID: {message.from_user.id}')

@router.callback_query(F.data == 'Menu')
async def menu(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.answer_photo(photo='AgACAgIAAxkBAANIaCCIauR7fklK5xfTx7YSIcSukCsAAlv0MRsl7whJRtAlhvdFQRYBAAMCAAN5AAM2BA',
                                        reply_markup=kb.main_menu)

@router.callback_query(F.data == 'comments')
async def comments(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer_photo(
        photo='AgACAgIAAxkBAANxaCHQ56orzwABpQTjEUkRbtEUx9oHAAKL7zEbJe8QSdNejgPMOcdlAQADAgADeAADNgQ',
        reply_markup=kb.comments_menu
    )

@router.callback_query(F.data == 'back')
async def get_back(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer_photo(
        photo='AgACAgIAAxkBAANIaCCIauR7fklK5xfTx7YSIcSukCsAAlv0MRsl7whJRtAlhvdFQRYBAAMCAAN5AAM2BA',
        reply_markup=kb.main_menu)

@router.callback_query(F.data == 'Guide')
async def get_guide(callback:CallbackQuery):
    await callback.message.delete()
    await callback.message.answer_photo(
        photo='AgACAgIAAxkBAAO7aCcZ2Y5dXmcTVwVOcmgfpv5FtvEAAt3xMRtkKDlJrGj0AeJF2UwBAAMCAAN5AAM2BA',
        reply_markup=kb.guide_menu
    )

@router.callback_query(F.data == 'how_to_reg')
async def get_reg(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer_photo(
        photo='AgACAgIAAxkBAAPNaCcgxQnM4GAj9CYeS4edS0-zAhMAAijyMRtkKDlJXX8uQOD2zIgBAAMCAAN4AAM2BA',
        caption='',
        reply_markup=kb.how_to_reg_menu
    )

@router.callback_query(F.data == 'back_to_guide_menu')
async def back_to_guide_menu(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer_photo(photo='AgACAgIAAxkBAAO7aCcZ2Y5dXmcTVwVOcmgfpv5FtvEAAt3xMRtkKDlJrGj0AeJF2UwBAAMCAAN5AAM2BA',
        reply_markup=kb.guide_menu)

@router.callback_query(F.data == 'how_to_install')
async def how_to_install(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer_photo(photo='AgACAgIAAxkBAAPjaCcnT23izpj_Hp2JWz1pDKfk4kEAAk7yMRtkKDlJ1HqgjlaahPcBAAMCAAN4AAM2BA',
                                        caption='Шаг 1: Скачиваем приложение\n'
                                                'В случае, если у вас iphone: \n'
                                                'заходим в App Store и вводим в строку поиска "Dewu", скачиваем приложение с китайскими иероглифами\n'
                                                'В случае, если у вас android: \n'
                                                '1.Переходите по ссылке https://www.dewu.com Вы попали на страницу скачивания китайского аналога Play Market. На странице есть QR код, его нужно отсканировать. Можно сделать скриншот страницы и открыть его через приложение для распознавания QR кодов\n'
                                                '2.Система предлагает перейти на промежуточный сайт с ссылкой на нужное нам приложение. Жмем на верхнюю активную синюю кнопку. Далее появляется подтверждение установки. После нажатия кнопки “установить”, приложение автоматически начнет загружаться на ваш телефон\n',
                                        reply_markup=kb.how_to_back_to_install_and_reg_menu
                                        )

@router.callback_query(F.data == 'how_to_reg_in_app')
async def how_to_reg_in_app(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer_photo(photo='AgACAgIAAxkBAAIBBmgnKnq8xofxX7y7ahRZhGa7P7JMAAJ08jEbZCg5SU6DqKThQ4VtAQADAgADeAADNgQ',
                                        caption='Шаг 2: Регистрация в приложении\n'
                                                'При первом открытии приложения автоматически появляется окно для регистрации пользователя\n'
                                                'Если окно не появилось или вы его закрыли, открываем страницу с регистрацией самостоятельно\n'
                                                '1.Заходим в любую карточку товара\n'
                                                '2.Нажимаем на ценник внизу карточки\n'
                                                '3.В новом окне справа вверху кнопка. Жмём на нее\n'
                                                '4.В следующем окне появляются две строки для ввода данных. Пока ничего не вводим. Жмём на кнопку, которая ниже двух строк справа\n'
                                                '5.Третье окно предлагают ввести номер телефона\n'
                                                '6.Начинаем с выбора кода страны. Жмём на цифру, в выпадающем списке выбираем код +7. Поднимаемся и жмём на кнопку слева вверху\n'
                                                '7.Теперь вводим номер телефона\n'
                                                '8.Подтверждаем нажатием на бирюзовую кнопку под номером телефона. Сайт обрабатывает данные, это занимает немного времени\n'
                                                '9.На ваш номер отправляется четырехзначный код. Иногда на телефон поступает звонок, нужно ввести последние 4 цифры номера\n'
                                                '10.После успешного подтверждения, приложение готово к работе',
                                        reply_markup=kb.how_to_back_to_install_and_reg_menu)

@router.callback_query(F.data == 'back_to_how_to_install')
async def back_to_how_to_install(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer_photo(photo='AgACAgIAAxkBAAPNaCcgxQnM4GAj9CYeS4edS0-zAhMAAijyMRtkKDlJXX8uQOD2zIgBAAMCAAN4AAM2BA',
                                        reply_markup=kb.how_to_reg_menu)

@router.callback_query(F.data == 'how_to_find_size_shoes')
async def how_to_find_size_shoes(callback: CallbackQuery):
    await callback.message.delete()
    media = [InputMediaPhoto(media='AgACAgIAAxkBAAIBXmgu1pkrFqBNT3inRJOpX-MKerZIAAKG8zEbaqZ4SabJbiqRIBy1AQADAgADeQADNgQ', caption='1 фото', reply_markup=kb.back_to_guide_menu),
             InputMediaPhoto(media='AgACAgIAAxkBAAIBYGgu1qKnAnQhHNxk1qXugDecm0MBAAKH8zEbaqZ4SampLt9IikTIAQADAgADeQADNgQ'),
             InputMediaPhoto(media='AgACAgIAAxkBAAIBYmgu1qUBYx-VpDeZI2m0KZE25KAuAAKI8zEbaqZ4SaBy78CmLfRaAQADAgADeQADNgQ'),
             InputMediaPhoto(media='AgACAgIAAxkBAAIBZGgu1qn8zlXa4SwGkpJ8aeZ6rQxyAALI7zEbSk55SdMyt6JUZI5xAQADAgADeQADNgQ')]
    await callback.message.answer_media_group(media=media)
    await callback.message.answer(reply_markup=kb.back_to_guide_menu)

# Состояния бота
class OrderStates(StatesGroup):
    waiting_for_order_number = State()
    waiting_for_name = State()
    waiting_for_address = State()
    waiting_for_size = State()
    waiting_for_photo = State()
    waiting_for_price = State()
    waiting_for_tglink = State()


@router.callback_query(F.data == 'make an order')
async def make_an_order(callback: types.CallbackQuery, state: FSMContext):
    # Отвечаем на callback, чтобы убрать "часики" у кнопки
    await callback.answer()

    # Отправляем сообщение через callback.message.answer()
    await callback.message.answer(text="Введите ваше ФИО:")
    await state.set_state(OrderStates.waiting_for_name)


@router.message(OrderStates.waiting_for_name)
async def process_name(message: types.Message, state: FSMContext):
    await state.update_data(name=message.text)
    await message.answer(text="🏠 Введите адрес доставки:")
    await state.set_state(OrderStates.waiting_for_address)

@router.message(OrderStates.waiting_for_address)
async def process_address(message: types.Message, state: FSMContext):
    await state.update_data(address=message.text)
    await message.answer(text="Введите ваш размер:")
    await state.set_state(OrderStates.waiting_for_size)

@router.message(OrderStates.waiting_for_size)
async def process_size(message: types.Message, state: FSMContext):
    await state.update_data(size=message.text)
    await message.answer(text='Отправьте фото со стоимостью товара вашего размера: ')
    await state.set_state(OrderStates.waiting_for_photo)

@router.message(OrderStates.waiting_for_photo)
async def process_price(message: types.Message, state: FSMContext):
    await state.update_data(photo=message.photo[-1])
    await message.answer(text='Введите стоимость товара вашего размера: ')
    await state.set_state(OrderStates.waiting_for_price)

@router.message(OrderStates.waiting_for_price)
async def process_price(message: types.Message, state: FSMContext):
    await state.update_data(price=message.text)
    await message.answer(text='Отправьте ссылку на ваш телеграм аккаунт (для связи с вами): ')
    await state.set_state(OrderStates.waiting_for_tglink)




@router.message(OrderStates.waiting_for_tglink)
async def get_data_from_messages(message: types.Message, state: FSMContext):
    await state.update_data(tglink=message.text)
    try:
        order_number = f"ORDER_{datetime.now().strftime('%Y%m%d_%H%M%S')}_{random.randint(1000, 9999)}"

        data = await state.get_data()

        order_data = {
            'Номер заказа': order_number,
            'ФИО': data['name'],
            'Адрес': data['address'],
            'Размер': data['size'],
            'Фото': data['photo'],
            'Стоимость заказа': data['price'],
            'Ссылка на тг аккаунт': data['tglink'],
            'Оплата': 'Не оплачено',
            'Статус заказа': 'Ждет оплаты'
        }

        # ✅ ВЫЗЫВАЕМ ФУНКЦИЮ ИЗ DATABASE ДЛЯ ЗАПИСИ
        if excel_manager.add_order(order_data):
            await message.answer(
                f"✅ Заказ успешно добавлен!\n\n"
                f"📦 Номер: {order_number}\n"
                f"👤 ФИО: {data['name']}\n"
                f"🏠 Адрес: {data['address']}\n"
                f"💰 Стоимость: {data['price']} руб."
            )
        else:
            await message.answer("❌ Ошибка при сохранении заказа")

    except ValueError:
        await message.answer("❌ Пожалуйста, введите корректную сумму:")
        return

    # Очищаем состояние
    await state.clear()
