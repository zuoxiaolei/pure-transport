import puretransport
from pyhive import hive

transport = puretransport.transport_factory(host='host',
                                            port=10000,
                                            username='username',
                                            password='secret',
                                            use_ssl=True)

hive_con = hive.connect(username='username', thrift_transport=transport,
                        database='default')
cursor = hive_con.cursor()

cursor.execute("select * from table limit 1")

cursor.fetchall()
