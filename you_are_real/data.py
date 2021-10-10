from psycopg2 import connect

class Database:
    def __init__(self, conn_str):
        self.connection = connect(conn_str)
        self.connection.autocommit = True

    def add_answer(self, answer_text):
        with self.connection.cursor() as cursor:
            cursor.execute("INSERT INTO Answers (Answer) VALUES (%(answer)s)", {"answer": answer_text})

    def get_answers(self):
        with self.connection.cursor() as cursor:
            cursor.execute("SELECT Answer FROM Answers")
            return cursor.fetchall()
