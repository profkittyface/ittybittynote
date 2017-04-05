#!/usr/bin/env python
import psycopg2
from flask import Flask, jsonify, redirect, request, g
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/notes/', methods=['GET', 'POST'])
def get_notes():
    conn = get_db_conn()
    c = conn.cursor()
    if request.method == 'GET':
        c.execute('select id,title,content,created from notes')
        rs_notes = c.fetchall()
        notes = []
        for n in rs_notes:
            note = {}
            note['id'] = n[0]
            note['title'] = n[1]
            note['content'] = n[2]
            note['created'] = n[3]
            notes.append(note)
        return jsonify(notes)
    if request.method == 'POST':
        title = request.form.get('title')
        content = request.form.get('content')
        c.execute('insert into notes (title,content) VALUES (%s,%s) returning id', (title,content))
        note_id = c.fetchall()[0][0]
        conn.commit()
        return redirect('http://127.0.0.1:9000/notes/'+str(note_id))

@app.route('/notes/<int:note_id>', methods=['GET'])
def note_action(note_id=None):
    conn = get_db_conn()
    c = conn.cursor()
    if request.method == 'GET':
        if note_id == None:
            print note_id
            c.execute('select id,title,content,created from notes')
            note = {}
            notes = c.fetchall()
            return jsonify(notes)
        else:
            c.execute('select id,title,content,created from notes where id = %s', (note_id,))
            notes = c.fetchall()
            return jsonify(notes)


def get_db_conn():
    if not hasattr(g, 'pg_conn'):
        g.pg_conn = psycopg2.connect('dbname=ittybittynote')
    return g.pg_conn


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=9000, debug=True)


'''
DROP DATABASE ittybittynote;
CREATE DATABASE ittybittynote;
\c ittybittynote;
CREATE TABLE notes (
    id serial NOT NULL,
title text,
content text,
created timestamp DEFAULT now());
INSERT INTO notes (title, content) VALUES ('Hello!', 'Note content!');
INSERT INTO notes (title, content) VALUES ('Another note!', 'Some more note content!!');
'''
'''
curl -XPOST http://localhost:9000/notes/ -F 'title=thing1' -F 'content=thing2'
'''
