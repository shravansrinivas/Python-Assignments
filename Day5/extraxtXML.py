import pymysql

db = pymysql.connect("localhost", "root", "", "test")
cursor = db.cursor(pymysql.cursors.DictCursor)


# data=cursor.execute("CREATE TABLE User(FNAME CHAR(20) NOT NULL, LNAME CHAR(20))")

from xml.dom import minidom

doc = minidom.parse("users1.xml")

# doc.getElementsByTagName returns NodeList
name = doc.getElementsByTagName("fname")[0]
print(name.firstChild.data)

def getNodeText(node):

    nodelist = node.childNodes
    result = []
    for node in nodelist:
        if node.nodeType == node.TEXT_NODE:
            result.append(node.data)
    return ''.join(result)

names = doc.getElementsByTagName("user")
for name in names:
        fname = name.getElementsByTagName("fname")[0]
        lname = name.getElementsByTagName("lname")[0]
        #salary = staff.getElementsByTagName("salary")[0]
        print((getNodeText(fname), getNodeText(lname)))
        value=(fname.childNodes[0].data,lname.childNodes[0].data)
        sql = """INSERT INTO User(FNAME,LNAME)
        VALUES(%s,%s)
        """
        query = cursor.execute(sql, value);
        db.commit()


data = cursor.execute('SELECT * FROM User')
resp = cursor.fetchall()
for row in cursor:
           print(row)
db.close()
