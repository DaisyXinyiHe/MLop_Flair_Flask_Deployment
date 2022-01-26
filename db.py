import os
import pymysql
from flask import jsonify

db_user = os.environ.get('CLOUD_SQL_USERNAME')
db_password = os.environ.get('CLOUD_SQL_PASSWORD')
db_name = os.environ.get('CLOUD_SQL_DATABASE_NAME')
db_connection_name = os.environ.get('CLOUD_SQL_CONNECTION_NAME')


def open_connection():
    unix_socket = '/cloudsql/{}'.format(db_connection_name)
    try:
        if os.environ.get('GAE_ENV') == 'standard':            conn = pymysql.connect(user=db_user, password=db_password,
                                unix_socket=unix_socket, db=db_name,                                cursorclass=pymysql.cursors.DictCursor
                                )
    except pymysql.MySQLError as e:
        print(e)

    return conn


def get_sentences():
    conn = open_connection()
    with conn.cursor() as cursor:
        result = cursor.execute('SELECT * FROM all_sent;’)
        songs = cursor.fetchall()
        if result > 0:
            all_sentences = jsonify(all_sent)
        else:
            all_sentences = 'No entry in DB'
    conn.close()
    return all_sentences

def add_sentences(sentence, sentiment):
    conn = open_connection()
    with conn.cursor() as cursor:
        cursor.execute('INSERT INTO all_sent (sentence, sentiment) VALUES(%s, %s)', (all_sent[“sentence”], all_sent[“sentiment”]))
    conn.commit()
    conn.close()
