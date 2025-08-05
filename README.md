**Анализатор сетевого трафика**

Проект на Python для перехвата и анализа сетевых пакетов. Визуализирует топ-10 IP-адресов по количеству перехваченных пакетов.

Пример вывода:

<img width="454" height="268" alt="image" src="https://github.com/user-attachments/assets/38def04c-8e12-418c-8272-02e9eba92420" />

Требования:

- Python 3.10+
- Библиотеки:
  ```bash
  scapy pandas matplotlib

  Установка:
  
  1. Клонируйте репозиторий
  git clone https://github.com/maxarasomaxa/traffic_analyzer.git
  2. Установите зависимости
  pip install -r requirements.txt

  Запуск:
  
  sudo python3 main.py

  Структура проекта:

main.py             Основной скрипт
utils.py            Визуализация данных
requirements.txt    Зависимости
traffic_stats.png   Пример графика


