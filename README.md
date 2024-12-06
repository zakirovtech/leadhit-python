# leadhit-python

Stack: Fastapi, tinydb, unittest

* **src**: основноя директория проекта
* **config**: пакет конфигурации
* **models**: работас базой и исходники в  **data**
* **tests**: тесты обработчика с разными входными данными

## Сборка
* ```git clone git@github.com:zakirovtech/leadhit-python.git```
* ```cd leadhit-python/src```
* ```docker compose build --no-cache```
* ```docker compose up```

### Запуск тестов
* ```docker exec -it web python -m unittest discover tests```

### Скрипт с запросами для проверки локально после запуска 
* ```./test.sh```

### Остановить и удалить контейнеры
* ```docker compose down```
