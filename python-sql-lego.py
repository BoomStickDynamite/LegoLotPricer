# Grant Zukowski
# SQL queries from Python

# this script will serve as the base for queries to the lego set database
# I will be creating in lieu of getting the bricklinks API database calls
# not to work.  My thought is it will be faster to have a local database query
# then to query an external database.  Also, it will give me practice
# creating my own database, then hopefully converting that to a Flask database
# at a later time


# import SQL module connector
import mysql.connector
# import SQL module error checker - super helpful, will always use this from
# now on, helps tremendously in debugging
from mysql.connector import errorcode

# start try statement
try:
  # create a cnx object that uses connect() and feeds in values, must
  # put this information in separate .py module for later use so
  # pw is not public
  cnx = mysql.connector.connect(user='test_user', password='Thisisatest!1',
                              host='127.0.0.1',
                              database='lg')
  # create a cursor object using the cnx connection
  cursor = cnx.cursor()

  # set the specifics of the query, doesn't work correctly but at least
  # gives data back
  query = ("SELECT LOWER(customer_last_name) AS 'First name' FROM customers \
    WHERE customer_first_name > 's'")

  # use the cursor to execuse the query 
  cursor.execute(query)

  # go through each customer name returned and print it out
  for (customer_last_name) in cursor:
      print("{} has a last name that is after s, sort of.".format(customer_last_name))

  # close the cursor
  cursor.close()
  # close the connection
  cnx.close()

# start exception handling
except mysql.connector.Error as err:
  if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
    print("Something is wrong with your user name or password")
  elif err.errno == errorcode.ER_BAD_DB_ERROR:
    print("Database does not exist")
  else:
    print(err)
else:
  # close the connection if nothing works
  cnx.close()
