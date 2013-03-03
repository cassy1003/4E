
import database

fileName = 'test%g.test.hoge%1.dat'
item = fileName.split('%')
print item
name = item[0]
skypeId = item[1]

if database.createUser(name, skypeId):
  print 'success create user'
else:
  print 'error create user'

for line in open(fileName, 'r'):
  database.insertQtime(name, line[:-1])
