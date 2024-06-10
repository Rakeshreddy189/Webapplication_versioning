from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

def init_db():
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    c.execute('CREATE TABLE IF NOT EXISTS data (value1 TEXT, value2 TEXT)')
    conn.commit()
    conn.close()

@app.route('/api/submit', methods=['POST'])
def submit():
    data = request.get_json()
    value1 = data.get('value1')
    value2 = data.get('value2')

    if not value1 or not value2:
        return jsonify({'error': 'Invalid input'}), 400

    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    c.execute('INSERT INTO data (value1, value2) VALUES (?, ?)', (value1, value2))
    conn.commit()
    conn.close()

    return jsonify({'message': 'Data submitted successfully!'}), 200

if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0', port=5000)
