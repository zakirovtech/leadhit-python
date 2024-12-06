import re
import typing


def validate_form(context: typing.Dict, form: typing.Dict) -> typing.Dict | str:
    """
    Вызывается только когда форма была найдена по запрашиваемым полям. 
    Валидирует типы каждого поля в форме от юзера и в форме в базе
    """
    form_types = do_typing(form)
    request_types = do_typing(context)

    common_keys = form_types.keys() & request_types.keys() # Нужны только общие, тк есть поле name и юзер может запросить несуществующие
    
    for key in common_keys:
        if not form_types[key] == request_types[key]: # Если хотя бы 1 значение не совпадает типами возвращаем типы полей запроса
            return request_types

    return form.get("name") # В ответ нужно вернуть имя шаблона формы, если она была найдена.


def do_typing(form: typing.Dict) -> typing.Dict:
    phone_pattern = r'^\+7\d{10}$'
    email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    date_pattern = r'^(?:\d{2}\.\d{2}\.\d{4}|\d{4}-\d{2}-\d{2})$'

    form_types = {key: None for key in form.keys()}

    for k, v in form.items():
        if re.match(date_pattern, v):
            form_types[k] = "date"
        elif re.match(phone_pattern, v):
            form_types[k] = "phone"
        elif re.match(email_pattern, v):
            form_types[k] = "email"
        else:
            form_types[k] = "text"
    
    return form_types
