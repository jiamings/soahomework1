
import sae, db
from soahomework1 import app

db.init(db_type = 'mysql', \
        db_schema = sae.const.MYSQL_DB, \
        db_host = sae.const.MYSQL_HOST, \
        db_port = int(sae.const.MYSQL_PORT), \
        db_user = sae.const.MYSQL_USER, \
        db_password = sae.const.MYSQL_PASS, \
        use_unicode = True, \
        charset = 'utf8')


application = sae.create_wsgi_app(app)
