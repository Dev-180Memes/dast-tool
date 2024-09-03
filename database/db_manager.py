# database/db_manager.py

import sqlite3

class DBManager:
    def __init__(self, db_path):
        self.conn = sqlite3.connect(db_path)
        self.create_table()

    def create_table(self):
        query = """
        CREATE TABLE IF NOT EXISTS scans (
            id INTEGER PRIMARY KEY,
            target TEXT,
            vulnerability TEXT,
            severity TEXT,
            recommendation TEXT
        )
        """
        self.conn.execute(query)
        self.conn.commit()

    def insert_scan_result(self, target, vulnerability, severity, recommendation):
        query = """
        INSERT INTO scans (target, vulnerability, severity, recommendation)
        VALUES (?, ?, ?, ?)
        """
        self.conn.execute(query, (target, vulnerability, severity, recommendation))
        self.conn.commit()

    def fetch_all_results(self):
        query = "SELECT * FROM scans"
        cursor = self.conn.execute(query)
        return cursor.fetchall()

    def close(self):
        self.conn.close()
