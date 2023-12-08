'''
> Required:
  # Cryptography
  pip3 install cryptography

  # Flask webserver
  pip3 install flask

  # Original lib from MySQL
  pip3 install mysql-connector-python
  # pip install mysql-connector-python --upgrade

> Ignored:
  # flask-mysqldb
  https://hevodata.com/learn/flask-mysql/
  # flask-mysqldb is too old and never updated
  # ERROR: Failed building wheel for mysqlclient
  # ERROR: Could not build wheels for mysqlclient, which is required to install pyproject.toml-based projects
  #pip3 install flask flask-mysqldb
'''

import website

app = website.create_app()
if __name__ == '__main__':
  app.run(port = 3000, debug = True)
