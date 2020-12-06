from nebulaApi.connect import runGql

def getAllGraph():
    query_resp = runGql('SHOW SPACES')
    return query_resp

def createGraph(dbName):
    query_resp = runGql(f'CREATE SPACE {dbName}')
    return query_resp

def deletGraph(dbName):
    query_resp = runGql(f'DROP  SPACE {dbName}')
    return query_resp
