from os import getenv

DB_USER=getenv('DB_USER', 'root')
DB_PASS=getenv('DB_PASS', 'tdc')
DB_HOST=getenv('DB_HOST', 'db.tdc')
DB_NAME=getenv('DB_NAME', 'tdc')
PREFIX=getenv('PREFIX', 'Bearer ')
SECRET=getenv('SECRET', 'tdc')
DECODE_OPTIONS = {
    'verify_signature': True,
    'verify_exp': False,
    'verify_nbf': False,
    'verify_iat': False,
    'verify_aud': False,
    'require_exp': True,
    'require_iat': False,
    'require_nbf': False
}
