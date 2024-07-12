# Flask Mail Sender

Проект Flask для отправки писем с возможностью прикрепления файлов. Этот проект использует Flask, Flask-Mail и TailwindCSS для создания простого веб-интерфейса для отправки писем.

## Требования

- Python 3.6+
- Flask
- Flask-Mail
- python-dotenv
- werkzeug

## Установка

1. Клонируйте репозиторий:

    ```bash
    git clone https://github.com/yourusername/flask-mail-sender.git
    cd flask-mail-sender
    ```

2. Создайте виртуальное окружение и активируйте его:

    ```bash
    python -m venv venv
    source venv/bin/activate  # для Windows используйте venv\Scripts\activate
    ```

3. Установите зависимости:

    ```bash
    pip install -r requirements.txt
    ```

4. Создайте файл `.env` в корневой папке проекта и добавьте в него следующие строки:

    ```dotenv
    MAIL_SERVER=smtp.gmail.com
    MAIL_PORT=587
    MAIL_USE_TLS=True
    MAIL_USERNAME=your-email@gmail.com
    MAIL_PASSWORD=your-app-specific-password
    MAIL_DEFAULT_SENDER=your-email@gmail.com
    UPLOAD_FOLDER=uploads/
    ```

5. Создайте папку для загрузки файлов, если она еще не существует:

    ```bash
    mkdir uploads
    ```

## Запуск

1. Активируйте виртуальное окружение, если оно еще не активировано:

    ```bash
    source venv/bin/activate  # для Windows используйте venv\Scripts\activate
    ```

2. Запустите Flask сервер:

    ```bash
    python app.py
    ```

3. Перейдите в браузер и откройте [http://localhost:5000](http://localhost:5000).

## Использование

1. Заполните форму, указав получателя, тему и сообщение.
2. При необходимости прикрепите файлы, нажав на кнопку "Выбрать файлы".
3. Нажмите кнопку "Отправить".
4. При успешной отправке письма появится модальное окно с уведомлением об успешной отправке.

## Структура проекта

```plaintext
flask-mail-sender/
│
├── .env               # Файл конфигурации с переменными окружения
├── app.py             # Основной файл приложения Flask
├── templates/
│   └── index.html     # HTML-шаблон для формы отправки письма
├── uploads/           # Папка для хранения загруженных файлов
├── requirements.txt   # Файл с зависимостями проекта
└── README.md          # Документация проекта
