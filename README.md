# TestovTask
API для учета финансовых операций
![GitHub top language](https://img.shields.io/github/languages/top/Mike0001-droid/TestovTask)

<!--Установка-->
## Установка 
У вас должны быть установлены [зависимости проекта](https://github.com/Mike0001-droid/TestovTask/requirements.txt)

1. Клонирование репозитория 

```git clone https://github.com/Mike0001-droid/TestovTask.git```

2. Переход в директорию Oxygen

```cd Fin_Operation```

3. Создание виртуального окружения

```python -m venv venv```

4. Активация виртуального окружения

```cd venv/scripts/activate```

5. Установка зависимостей

```pip install -r requirements.txt```

6. Запуск миграций

```python manage.py migrate```

7. Создание админа

```python manage.py createsuperuser```

7. Запуск сервера

```python manage.py runserver```