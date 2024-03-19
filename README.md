## Копируем репозиторий
```bash
git clone https://github.com/MikhalchenkoD/test-task-selenium.git
```
## Активация виртуального окружения (Для Windows)
```bash
python -m venv venv
.\venv\Scripts\activate
```
## Активация виртуального окружения (Для Linux)
```bash
python3 -m venv venv
source venv/bin/activate
```
## Установка зависимостей
```bash
cd test-task-selenium
pip install -r requirements.txt
```

## Запуск тестов
```bash
pytest
```
