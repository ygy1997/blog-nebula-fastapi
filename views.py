from nebula.graph import ttypes
from nebula.ConnectionPool import ConnectionPool
from nebula.Client import GraphClient


connection_pool = ConnectionPool('127.0.0.1', 3699)
client = GraphClient(connection_pool)
auth_resp = client.authenticate('user', 'password')

def getDb():
    query_resp = client.execute_query('SHOW SPACES')
    return query_resp

def createDb(dbName):
    query_resp = client.execute_query(f'CREATE SPACE {dbName}')
    return query_resp

def deleDb(dbName):
    query_resp = client.execute_query(f'DROP  SPACE {dbName}')
    return query_resp

def creatDbNode(dbName,Node):
    pass

def creatDbEdge(dbName,Edge):
    pass
