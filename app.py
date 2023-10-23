from flask import Flask, render_template, request, redirect, url_for
import psycopg2
import os

app = Flask(__name__)
url = "postgres://raj:UPL64CjBLgQd4Sc5VlvRNcE4268zPjNg@dpg-ckrb2pg5vl2c73bqmhgg-a.oregon-postgres.render.com/raj"
# Configure your PostgreSQL connection parameters

url = os.environ.get('DATABASE_URL')
db_params = {
    url
    # 'database': 'raj',
    # 'user': 'raj',
    # 'password': 'UPL64CjBLgQd4Sc5VlvRNcE4268zPjNg',
    # 'host': 'dpg-ckrb2pg5vl2c73bqmhgg-a.oregon-postgres.render.com',
}


@app.route('/')
def list_users():
    conn = psycopg2.connect(url)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users;')
    users = cursor.fetchall()
    conn.close()
    return render_template('list_users.html', users=users)

@app.route('/add_user', methods=['POST'])
def add_user():
    username = request.form['username']
    conn = psycopg2.connect(url)
    cursor = conn.cursor()
    cursor.execute('INSERT INTO users (username) VALUES (%s);', (username,))
    conn.commit()
    conn.close()
    return redirect(url_for('list_users'))

@app.route('/update_user/<int:user_id>', methods=['POST'])
def update_user(user_id):
    new_username = request.form['new_username']
    conn = psycopg2.connect(url)
    cursor = conn.cursor()
    cursor.execute('UPDATE users SET username = %s WHERE id = %s;', (new_username, user_id))
    conn.commit()
    conn.close()
    return redirect(url_for('list_users'))

@app.route('/delete_user/<int:user_id>', methods=['POST'])
def delete_user(user_id):
    conn = psycopg2.connect(url)
    cursor = conn.cursor()
    cursor.execute('DELETE FROM users WHERE id = %s;', (user_id,))
    conn.commit()
    conn.close()
    return redirect(url_for('list_users'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
    app.run(debug=True)
    
