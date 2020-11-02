import kivy
import psycopg2

from kivy.app import App

from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty

con = psycopg2.connect(
	        host = "aceappdb.c96npodftr7k.us-east-2.rds.amazonaws.com",
            database="postgres",
	        user = "postgres",
	        password = "Aceboom!")


cursor = con.cursor()




class MyGrid(Widget):
    firstname = ObjectProperty(None)
    lastname = ObjectProperty(None)
    email = ObjectProperty(None)

    def btn(self):
        print("First Name:", self.firstname.text, "Last Name: ", self.lastname.text, "Email: ", self.email.text)
        insert_query = """INSERT INTO CUSTOMER (FNAME, LNAME, EMAIL) VALUES (%s, %s, %s)"""
        record_to_insert = (self.firstname.text, self.lastname.text, self.email.text)
        cursor.execute(insert_query, record_to_insert)

        con.commit()
        count = cursor.rowcount
        print(count, "Record inserted successfully into customer table")





class DemoApp(App):
    def build(self):
        return MyGrid()

if __name__ == "__main__":
    DemoApp().run()


