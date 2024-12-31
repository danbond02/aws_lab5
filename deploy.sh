#!/bin/bash -ex

# Установка необхідних залежностей
sudo apt-get install -y python3-pip python3-venv

# Перехід у папку з файлами
cd /home/ubuntu/branch-files

# Копіювання service-файла в систему
sudo cp ./lab2-app.service /etc/systemd/system/lab2-app.service

source venv/bin/activate

# Встановлення Python-залежностей
pip install -r requirements.txt

# Перезавантаження конфігурації systemd
sudo systemctl daemon-reload

# Додавання сервісу до автозавантаження
sudo systemctl enable lab2-app.service

# Запуск сервісу
sudo systemctl start lab2-app.service