from flask import Flask, render_template, request, jsonify
from mysql.connector import connect, Error

app = Flask(__name__)

# Database connection function
def get_db_connection():
    try:
        conn = connect(
            host='localhost',
            database='test',
            user='root',
            password='password'  # Replace with your actual password
        )
        return conn
    except Error as e:
        print(e)

# Route to display data from 'golcha' table
@app.route('/')
def index():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM golcha")
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('indexx.html', data=rows)

# API route to insert data into 'golcha' table
@app.route('/insert', methods=['POST'])
def about():
    data = request.get_json()
    id = data.get('id')
    st_name = data.get('st_name')
    email = data.get('email')

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO golcha (id, st_name, email) VALUES (%s, %s, %s)", (id, st_name, email))
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({'message': 'Data inserted'}), 201

# Route to serve the insertion form
@app.route('/form')
def form():
    return render_template('insert.html')

# Start the Flask app
if __name__ == '__main__':
    app.run(debug=True)
