# Watcher of Friends Online

The script for working with the site vk.com
The program displays the names and surnames of the user friends who are online at the moment.
For the program to work, the user needs to enter his / her login and password VK.

# How to Install

Python 3 should be already installed. Then use pip (or pip3 if there is a conflict with old Python 2 setup) to install dependencies:

```bash
pip install -r requirements.txt # alternatively try pip3
```

Remember, it is recommended to use [virtualenv/venv](https://devman.org/encyclopedia/pip/pip_virtualenv/) for better isolation.

To get app_id, you need to register your application at https://vk.com/dev

# Quickstart

Example of script launch on Linux, Python 3.5

```bash
python3 vk_friends_online.py
VK Login: oeananas@mail.ru
VK Password: 
Your VK friends online:
Никита Лис
Асанi Гилязов
Иван Старцев
Денис Перевозчиков
Аким Седельников
Людмила Окулова
Олеся Клементьева
Антоша Нас
Дмитрий Якимов
Макс Байметов
Kseniya Demonova
Павел Аверин
Алена Колобова

```

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
