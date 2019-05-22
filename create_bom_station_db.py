import sqlite3
import config

def setup():
    conn = sqlite3.connect(config.station_db_file)
    c = conn.cursor()
    c.execute('''  CREATE TABLE IF NOT EXISTS bomStation (
        stationID TEXT PRIMARY KEY,
        stationName TEXT NOT NULL,
        latitude TEXT NOT NULL,
        longitude TEXT NOT NULL,
        height TEXT NOT NULL
    ); ''')
    conn.commit()
    conn.close()


setup()
