from urllib.parse import parse_qs

from fastapi import FastAPI, Request, HTTPException

from services import search_form
from models.validators import validate_form

app = FastAPI()


@app.post("/get_form/")
async def search_forms(request: Request):
    body = await request.body()
    parsed_data = parse_qs(body.decode("utf-8"))

    data = {key: value[0] for key, value in parsed_data.items()}
    form = search_form(data) # Если все поля формы из базы есть в запросе от юзера возвращает эту форму
    
    if form is not None:
        response = validate_form(context=data, form=form)
        return response
    
    raise HTTPException(status_code=404, detail="Failed find the form by the provided fields")
