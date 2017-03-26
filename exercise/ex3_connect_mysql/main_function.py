import sys
import _mysql
import _mysql_exceptions

"""
pip install mysqlclient
export DYLD_LIBRARY_PATH=/usr/local/mysql/lib/
"""

try:
    config = {
        'user': 'root',
        'passwd': 'root',
        'host': 'localhost',
        'db': 'slimfw-demo',
    }
    conn = _mysql.connect(**config)
except _mysql_exceptions.MySQLError as err:
    errCode, errMsg = err.args
    print(errMsg)
except:
    print("Unexpected error:", sys.exc_info()[0])
else:
    conn.close()
