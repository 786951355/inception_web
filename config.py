import os

# Flask settings
SECRET_KEY = os.getenv('SECRET_KEY', 'THIS IS AN INSECURE SECRET')
SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'mysql://inception_web:inception_web111@localhost:3306/inception_web?charset=utf8')
SQLALCHEMY_TRACK_MODIFICATIONS=False
CSRF_ENABLED = True

# Flask-Mail settings
# if send mail , set MAIL_ON_OFF is ON
MAIL_ON_OFF='OFF'
MAIL_SERVER='smtp.sina.com'
MAIL_PORT=587
MAIL_USE_TLS=True
MAIL_USE_SSL=False
MAIL_USERNAME='test@sina.cn'
MAIL_PASSWORD='test'
MAIL_DEFAULT_SENDER='"test@sina.cn"<test@sina.cn>'

#Inception settings

INCEPTION_HOST='192.168.152.128'
INCEPTION_PORT=6669

#Inception backup settings
INCEPTION_REMOTE_BACKUP_HOST='localhost'
INCEPTION_REMOTE_BACKUP_PORT=3306
INCEPTION_REMOTE_BACKUP_USER='test'
INCEPTION_REMOTE_BACKUP_PASSWORD='test'

#Other optins
CRITICAL_DDL_ON_OFF='OFF'
AUDIT_SROLE_ON_OFF='OFF'
