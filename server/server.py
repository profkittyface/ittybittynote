#!/usr/bin/env python
import psycopg2
from flask import Flask, jsonify, redirect, request, g
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/notes', methods=['GET', 'POST'])
def note_action():
    conn = get_db_conn()
    c = conn.cursor()
    if request.method == 'GET':
        c.execute('select id,title,content,created from notes')
        notes = c.fetchall()
        return jsonify(notes)
    if request.method == 'POST':
        title = request.form.get('title')
        content = request.form.get('content')
        c.execute('insert into notes (title,content) VALUES (%s,%s)', (title,content))
        conn.commit()
        return 'ok\n'


def get_db_conn():
    if not hasattr(g, 'pg_conn'):
        g.pg_conn = psycopg2.connect('dbname=ittynote')
    return g.pg_conn


if __name__ == '__main__':
    app.run(debug=True)



''' 
DROP DATABASE ittynote;
CREATE DATABASE ittynote;
\c ittynote;
CREATE TABLE notes (
    id serial NOT NULL, 
title text, 
content text, 
created timestamp DEFAULT now());
INSERT INTO notes (title, content) VALUES ('Hello!', 'Note content!');
INSERT INTO notes (title, content) VALUES ('Another note!', 'Some more note content!!');
'''