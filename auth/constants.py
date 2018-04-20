from os import getenv

DB_USER=getenv('DB_USER', 'root')
DB_PASS=getenv('DB_PASS', 'tdc')
DB_HOST=getenv('DB_HOST', 'db.tdc')
DB_NAME=getenv('DB_NAME', 'tdc')
PREFIX=getenv('PREFIX', 'Bearer ')
SECRET=getenv('SECRET', 'tdc')
