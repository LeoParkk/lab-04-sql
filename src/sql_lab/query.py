import logging
import os

import mysql.connector

logging.basicConfig(level=logging.INFO)

#this reads the database credentials given from the env variables
DBHOST = os.environ.get("DBHOST")
DBUSER = os.environ.get("DBUSER")
DBPASS = os.environ.get("DBPASS")
DBNAME = os.environ.get("DBNAME")

db = mysql.connector.connect(host=DBHOST, user=DBUSER, password=DBPASS, database=DBNAME)
cur = db.cursor()


def get_data_by_group(value):
    """this function shows all rows where group column equals the given value"""
    query = "SELECT * FROM mock WHERE `group` = %s;"
    try:
        cur.execute(query, (value,))
        results = cur.fetchall()
        logging.info(f"{len(results)} rows found where group is {value}")
        return results
    except mysql.connector.Error as e:
        logging.error(f"MySQL Error: {e}")
        return None


def plot_counts(groupby):
    """this function counts the num of rows that have values given by groupby input"""
    query = f"SELECT `{groupby}`, COUNT(*) FROM mock GROUP BY `{groupby}`;"
    try:
        cur.execute(query)
        results = cur.fetchall()
        logging.info(f"counted rows by {groupby}")
        return results
    except mysql.connector.Error as e:
        logging.error(f"MySQL Error: {e}")
        return None


def main():
    """this function runs query, and closes once done"""
    print(get_data_by_group("UVA"))
    print(plot_counts("group"))

    cur.close()
    db.close()

#this helps make sure file is run correctly before running main(), which allows query to function
if __name__ == "__main__":
    main()
