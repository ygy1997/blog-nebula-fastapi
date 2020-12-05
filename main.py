from fastapi import FastAPI
from views import getDb,createDb,deleDb
app = FastAPI()

#显示所有数据库
@app.get("/getDb")
async def getDb():
    dbList=getDb()
    return dbList

#建立新数据库
@app.get("/creatDb/{dbName}")
async def createDb(dbName:str):
    dbList=createDb(dbName)
    return dbList

#删除某个数据库
@app.get("/deleDb/{dbName}")
async def deleDb(dbName:str):
    dbList=deleDb(dbName)
    return dbList

#新建某个数据库的点模型
@app.get("/{dbName}/create/{node}")
async def deleDbNodebyDbase(dbName:str):
    dbList=deleDb(dbName)
    return dbList

#删除某个数据库的点模型
@app.get("/{dbName}/delete/{edge}")
async def deleDbDNodebyDbase(dbName:str):
    dbList=deleDb(dbName)
    return dbList

if __name__ == '__main__':
    import os
    os.system('uvicorn main:app --reload')
