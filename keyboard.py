from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def get_function_keyboard() -> ReplyKeyboardMarkup:
    buttons = [
        [KeyboardButton(text="Сложение➕"), KeyboardButton(text="Вычитание➖")],
        [KeyboardButton(text="Умножение✖️")], [KeyboardButton(text="Деление➗")]
    ]
    return ReplyKeyboardMarkup(keyboard=buttons, resize_keyboard=True)


def get_answer_after_primer() -> ReplyKeyboardMarkup:
    buttons = [
        [KeyboardButton(text="Да✔"), KeyboardButton(text="Нет❌")]
    ]
    return ReplyKeyboardMarkup(keyboard=buttons, resize_keyboard=True)
