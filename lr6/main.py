import MySQLdb as mdb


try:

    ssl = {'ca': 'crt/ca.pem', 'cert': 'crt/server-cert.pem', 'key': 'crt/server-key.pem'}
    con = mdb.connect(
        host="kritt66g.beget.tech",
        user="kritt66g_lab6",
        password="Laboratornaya6!",
        database="kritt66g_lab6",
        ssl=ssl
    )

    print("Connection Ok")
    con.close()
except Exception as ex:
    print("Connection No")
    print(ex)