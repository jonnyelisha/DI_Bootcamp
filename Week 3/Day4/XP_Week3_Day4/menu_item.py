#In the file menu_item.py, create a new class called MenuItem, the attributes should be the name and price of each item.
#Create several methods (save, delete, update) these methods will allow a user to save, delete and update items from the Menu_Items table.
#The update method can update the name as well as the price of an item.

import psycopg2

# IF ALL LETTERS ARE UPPERCASE - THEN ITS A CONSTANT (not meant to change)
DBNAME = "Restaurant_Menu_Manager"
USER = "postgres"  # postgres
PASSWORD = "password"  # <YOUR POSTGRES PASSWORD>
HOST = "localhost"
PORT = "5432"

connection = psycopg2.connect(
    dbname=database, user=postgres, password=password, host=postgres, port=5423
)

# 2. Create a cursor (tool to run queries)
cursor = connection.cursor()


class MenuItem:
    def __init__(self, name_item, price_item=None) -> None:
        self.name_item = name_item
        self.price_item = price_item
        self.item_id = None

    # def save(self):
    #     query = f"insert into Menu_Items(item_name, item_price) values('{self.name_item}', {self.price_item});"
    #     cursor.execute(query)
    #     connection.commit()

    # more secure way
    def save(self):
        query = f"insert into Menu_Items(item_name, item_price) values(%s, %s);"
        cursor.execute(query, (self.name_item, self.price_item))
        connection.commit()  # apply all changes from cursor through the connection

    def delete(self):
        query = f"delete from Menu_Items where item_name = %s;"
        cursor.execute(query, (self.name_item,))  # comma for price_item value
        connection.commit()

    def update(self, new_name=None, new_price=None):
        if self.item_id is None:  # Check if item_id is not set
            query = "SELECT item_id FROM Menu_Items WHERE item_name = %s;"
            cursor.execute(query, (self.name_item,))
            result = cursor.fetchone()
            if result:
                self.item_id = result[0]
            else:
                print("Item not found in the database.")
                return

        if new_name:
            self.name_item = new_name
        if new_price:
            self.price_item = new_price
        query = "UPDATE Menu_Items SET item_name = %s, item_price = %s WHERE item_id = %s"
        cursor.execute(query, (self.name_item, self.price_item, self.item_id))
        connection.commit()


def main():
    item = MenuItem('Chips', 10)
    item.update('Veggie Burger', 37)

    # Run SELECT queries
    def select_all(table: str) -> list[tuple]:
        query = f"select * from {table};"
        cursor.execute(query)
        rows = (
            cursor.fetchall()
        )  # if the query returns something (like select) - fetch all of the rows returned
        return rows

    rows_movies = select_all("Menu_Items")

    for row in rows_movies:
        print(row)


if __name__ == "__main__":
    main()