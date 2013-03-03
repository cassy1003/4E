
'''
Database:
  4e_attendance_master
Has the following Collections.
  users :
  atime :
  qtime :
  badge :
'''

from pymongo import Connection
from datetime import datetime
import time

con = Connection("localhost")

#db = con['4e_attendance_master']
db = con['test']

def _find(colName, key=None):
  col = db[colName]
  try:
    if key:
      data = col.find(key)
    else:
      data = col.find()
    return data
  except:
    return False

def _findOne(colName, key=None):
  col = db[colName]
  try:
    if key:
      data = col.find_one(key)
    else:
      data = col.find_one()
    return data
  except:
    return False

def _insert(colName, key):
  col = db[colName]
  try:
    col.insert(key)
    return True
  except:
    return False

def checkUserExist(name):
  if _findOne('user', {'name': name}):
    return True
  else:
    return False

def insertAtime(name, str_date):
  int_date = getUnixTime(str_date)
  if checkUserExist(name):
    key = {'name': name , 'datetime': int_date}
    return _insert('atime', key)
  else:
    return 'Not exist'

def insertQtime(name, str_date=None):
  int_date = getUnixTime(str_date)
  if checkUserExist(name):
    key = {'name': name , 'datetime': int_date}
    return _insert('qtime', key)
  else:
    return 'Not exist'

def createUser(name, skypeId):
  if checkUserExist(name):
    return 'Already exist'
  else:
    key = {'name': name, 'skypeId': skypeId, 'image': '', 'password': '', 'ctime': getUnixTime()}
    return _insert('user', key)

def getUnixTime(str_date=None):
  if str_date:
    try:
      date = datetime.strptime(str_date, "%Y-%m-%d %H:%M")
    except:
      date = datetime.strptime(str_date, "%Y-%m-%d %H:%M:%S.%f")
  else:
    date = datetime.now()
  return int(time.mktime(date.timetuple()))
