from webapp import create_app
import sys

app = create_app()
app.app_context().push()

from webapp import db

print('Dropping Database...', file=sys.stderr)
db.drop_all()
print('Database dropped!', file=sys.stderr)

print('Reinitializing Database..', file=sys.stderr)
db.create_all()
print('Database reinitialized!', file=sys.stderr)

from webapp.models import Keyword

toAdd_keyword = Keyword( keyword = 'Testi')
db.session.add(toAdd_keyword)
db.session.commit() 
print('KEywords in the Database:', file=sys.stderr)
print(Keyword.query.all() , file=sys.stderr)

 



