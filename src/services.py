import typing

from models.database import db

def search_form(context: typing.Dict) -> typing.Dict | None:
    """Возвращает форму, если совпали все поля из запроса пользователя"""
    forms = db.all()
    request_fields = set(context.keys())  # Поля формы от юзера
    
    for form in forms:
        form_fields = set(list(form.keys())[1:]) # Поля шаблона в базе
        if not form_fields.difference(request_fields): # ТЗ: Самое главное, чтобы все поля шаблона присутствовали в форме (от юзера).
            return form
 