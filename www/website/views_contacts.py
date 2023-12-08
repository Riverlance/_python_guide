import flask
from . import mysqldbc

views = flask.Blueprint('views_contacts', __name__)



# Add contact
@views.route('/add_contact', methods=['POST'])
def add_contact():
  if flask.request.method == 'POST':
    with mysqldbc.MySQLdbConnection() as db:
      data = flask.request.form
      cursor = db.cursor()
      cursor.execute('INSERT INTO `contacts` (name, phone, email) VALUES (%s, %s, %s)', (data['name'], data['phone'], data['email']))
      db.commit()

    flask.flash('Contact created successfully.', category='success')

  return flask.redirect(flask.url_for('views_main.home'))

# Edit contact
@views.route('/edit_contact/<contact_id>')
def edit_contact(contact_id):

  with mysqldbc.MySQLdbConnection() as db:
    cursor = db.cursor()
    cursor.execute('SELECT * FROM `contacts` WHERE id = %s', (contact_id,))
    data = cursor.fetchone()

  return flask.render_template('edit_contact.html', contact = data)

# Edit contact - Confirm
@views.route('/edit_contact_confirm/<contact_id>', methods=['POST'])
def edit_contact_confirm(contact_id):

  if flask.request.method == 'POST':
    with mysqldbc.MySQLdbConnection() as db:
      cursor = db.cursor()
      cursor.execute('UPDATE `contacts` SET name = %s, phone = %s, email = %s WHERE id = %s', (flask.request.form['name'], flask.request.form['phone'], flask.request.form['email'], contact_id))
      db.commit()

    flask.flash('Contact edited successfully.', category='success')

  return flask.redirect(flask.url_for('views_main.home'))

# Delete contact
@views.route('/delete_contact/<string:contact_id>')
def delete_contact(contact_id):

  with mysqldbc.MySQLdbConnection() as db:
    cursor = db.cursor()
    cursor.execute('DELETE FROM `contacts` WHERE id = %s', (contact_id,))
    db.commit()

    flask.flash('Contact deleted successfully.', category='success')

  return flask.redirect(flask.url_for('views_main.home'))
