from nebula.graph import ttypes
from nebula.ConnectionPool import ConnectionPool
from nebula.Client import GraphClient


connection_pool = ConnectionPool('127.0.0.1', 3699)
client = GraphClient(connection_pool)
auth_resp = client.authenticate('user', 'password')

def getDb():
    query_resp = client.execute_query('SHOW SPACES')
    return query_resp
