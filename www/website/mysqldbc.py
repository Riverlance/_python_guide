'''
Readmore: https://dev.mysql.com/doc/connector-python/en/
'''

import mysql.connector as mysqlc
import mysql.connector.errorcode as db_error # Database error code

from . import website_lib as lib



@lib.singleton
class MySQLdbConnection():
  '''
  Usage:
  ```
  import mysqldbc
  with mysqldbc.MySQLdbConnection() as db:
    print(db.is_connected())
  ```
  '''

  def __enter__(self):
    try:
      self.__db = mysqlc.connect(host = '127.0.0.1', user = 'root', password = '', database = 'python_db')
    except mysqlc.Error as err:
      if err.errno == db_error.ER_DBACCESS_DENIED_ERROR:
        print('Access denied.')
      elif err.errno == db_error.ER_ACCESS_DENIED_ERROR:
        print('Something is wrong with your user name or password.')
      elif err.errno == db_error.ER_BAD_DB_ERROR:
        print('Database does not exist.')
      else:
        print(err)
    else:
      return self.__db

  def __exit__(self, __exc_type, __exc_val, __exc_tb):
    if self.__db and self.__db.is_connected():
      self.__db.close()
