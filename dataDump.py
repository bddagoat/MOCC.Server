import sqlite3

conn = sqlite3.connect("MOCdb.db")
cursor = conn.cursor()
results = cursor.execute("SELECT * FROM business_info").fetchall()
sqlfile = open("sqlScripts\\buildBusinessInfo.sql", "w")

for row in results:
  sql = u"INSERT INTO business_info VALUES ("
  for data in row:
    sql += u"'" + str(data) + u"', " 
  sql = sql[:-2] + u");\n"
  sqlfile.write(sql.replace("None", ""))
conn.commit()
conn.close()
