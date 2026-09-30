#!/usr/bin/env python3

import logging
import os

import mysql.connector
import pandas as pd

logging.basicConfig(level=logging.INFO)

DBHOST = os.environ.get("DBHOST")
DBUSER = os.environ.get("DBUSER")
DBPASS = os.environ.get("DBPASS")
DBNAME = os.environ.get("DBNAME")

#code below transforms pandas data types to sql data types
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
    columns = []
    for col, dtype in data.dtypes.items():
        columns.append(f"`{col}` {type_mapping[str(dtype)]}")
    create_query = f"CREATE TABLE IF NOT EXISTS `{table}` ({', '.join(columns)})"

    col_names = ", ".join(f"`{col}`" for col in data.columns)
    placeholders = ", ".join(["%s"] * len(data.columns))
    insert_query = f"INSERT INTO `{table}` ({col_names}) VALUES ({placeholders})"

    try:
        db = mysql.connector.connect(host=DBHOST, user=DBUSER, password=DBPASS, database=DBNAME)
        cursor = db.cursor()
        cursor.execute(create_query)

        # goes through each row one by one, with paramterized values
        for row in data.itertuples(index=False):
            cursor.execute(insert_query, row)

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


if __name__ == "__main__":
    main()
