# MedinaBook

![pipeline status](https://github.com/TekatoKiary/MedinaBook/actions/workflows/python-package.yml/badge.svg)

---
### Команды терминала по работе с проектом:

- Клонирование репозитория: 
```bash
git clone https://github.com/TekatoKiary/MedinaBook
```
- Установка виртуальной среды (venv): 
```bash 
python -m venv venv
```
- Активация виртуальной среды (venv activation): 
```bash 
source venv/bin/activate
``` 
или
```bash 
source venv/Scripts/activate
``` 
- Установка продовых зависимостей для проекта (installation of requirements for prod): 
```bash 
pip install -r requirements/prod.txt
```
- Запуск сервера (run command): 
```bash 
python server.py
```

---
### Работа с файлом .env
В корневой папке должен быть файл .env, который содержит такие параметры, как 'SECRET_KEY'. 
Примером такого файла служит .env.template.