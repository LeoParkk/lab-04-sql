import logging
import os

import mysql.connector
import pandas as pd

logging.basicConfig(level=logging.INFO)

DBHOST = os.environ.get("DBHOST")
DBUSER = os.environ.get("DBUSER")
DBPASS = os.environ.get("DBPASS")
DBNAME = os.environ.get("DBNAME")

#step 3
type_mapping = {
    "int64": "BIGINT",
    "str": "VARCHAR(255)",
}

def read_data(filename):
    """this function loads a given csv file into a data frame"""
    data = pd.read_csv(filename)
    logging.info(f"Read {len(data)} rows from {filename}")
    return data


def clean_data(data):
    """this function cleans data by removes rows with missing values"""
    data = data.dropna()
    logging.info(f"{len(data)} rows left after cleaning")
    return data


def load_data(data, table):
    """this function creates a table, and inserts each row into it"""
    create_query = (
        f"CREATE TABLE IF NOT EXISTS `{table}` ("
        "id BIGINT, `group` VARCHAR(255), first_name VARCHAR(255), "
        "last_name VARCHAR(255), gender VARCHAR(255), email VARCHAR(255))"
    )
    
    insert_query = (
        f"INSERT INTO `{table}` "
        "(id, `group`, first_name, last_name, gender, email) "
        "VALUES (%s, %s, %s, %s, %s, %s)"
    )

    try:
        db = mysql.connector.connect(host=DBHOST, user=DBUSER, password=DBPASS, database=DBNAME)
        cursor = db.cursor()
        cursor.execute(create_query)

        #inserts rows one at a time, each row passed as a list
        rows = data.values.tolist()
        for record_data in rows:
            cursor.execute(insert_query, record_data)

        db.commit()
        cursor.close()
        db.close()
        logging.info(f"Inserted {len(data)} rows into {table}")
    except mysql.connector.Error as e:
        logging.error(f"Database error: {e}")


def main():
    """reads the data, cleans itm, then loads it"""
    data = read_data("MOCK_DATA.csv")
    data = clean_data(data)
    load_data(data, "mock")
    logging.info("pipeline finished!")

if __name__ == "__main__":
    main()
