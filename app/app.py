from flask import Flask, request, jsonify, render_template
import mysql.connector
import os

app = Flask(__name__)

# Подключение к базе данных MySQL
def get_db_connection():
    try:
        conn = mysql.connector.connect(
            host=os.environ.get("MYSQL_HOST"),
            user=os.environ.get("MYSQL_USER"),
            password=os.environ.get("MYSQL_PASSWORD"),
            database=os.environ.get("MYSQL_DATABASE")
        )
        return conn
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None

# Главная страница с веб-интерфейсом чата
@app.route('/')
def index():
    return render_template('index.html')

# Отправка сообщения
@app.route('/send', methods=['POST'])
def send_message():
    content = request.json
    message = content.get('message')  # Проверяем наличие сообщения в запросе
    if not message:
        return jsonify({"status": "Message is required"}), 400

    conn = get_db_connection()
    if conn is None:
        return jsonify({"status": "Database connection failed"}), 500

    try:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO messages (content) VALUES (%s)", (message,))
        conn.commit()
        cursor.close()
    except mysql.connector.Error as err:
        print(f"Error inserting message: {err}")
        return jsonify({"status": "Error inserting message"}), 500
    finally:
        conn.close()

    return jsonify({"status": "Message sent"}), 200

# Получение списка сообщений
@app.route('/messages', methods=['GET'])
def get_messages():
    connection = mysql.connector.connect(
        host=os.getenv('MYSQL_HOST'),
        database=os.getenv('MYSQL_DATABASE'),
        user=os.getenv('MYSQL_USER'),
        password=os.getenv('MYSQL_PASSWORD')
    )

    if connection is None:
        return jsonify({"status": "Database connection failed"}), 500

    try:
        cursor = connection.cursor()
        cursor.execute("SELECT content FROM messages")
        messages = cursor.fetchall()
        cursor.close()
    except mysql.connector.Error as err:
        print(f"Error fetching messages: {err}")
        return jsonify({"status": "Error fetching messages"}), 500
    finally:
        connection.close()

    return jsonify([message[0] for message in messages]), 200

# Запуск приложения
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
