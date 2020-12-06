from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from nebulaApi.connect import runGql
from views import getAllGraph,createGraph,deletGraph,runGql
from blog import views as blog
app = FastAPI()


####nebula 数据库操作
@app.get("/runGql/{nGql}")
async def runNgql(nGql):
    result=runGql(nGql)
    return result
#显示所有数据库
@app.get("/getDb")
async def getDb():
    result=getAllGraph()
    return jsonable_encoder(result)
#建立新数据库
@app.get("/creatDb/{dbName}")
async def createDb(dbName:str):
    result=createGraph(dbName)
    return jsonable_encoder(result)
#删除某个数据库
@app.get("/delDb/{dbName}")
async def delDb(dbName:str):
    result=deletGraph(dbName)
    return jsonable_encoder(result)


#### blog操作
#创建点类型
@app.post("/blog/createNodeType/")
async def blogCreateNode(node:blog.BlogNode):
    createResult=blog.createNode(node)
    return jsonable_encoder(createResult)
#查询点类型
@app.post("/blog/getNodeType/")
async def blogGetNode(node:blog.BlogNode):
    createResult=blog.getNode(node)
    return jsonable_encoder(createResult)
#删除点类型
@app.post("/blog/dropNodeType/")
async def blogCreateNode(node:blog.BlogNode):
    dropResult=blog.dropNode(node)
    return jsonable_encoder(dropResult)
#追加点类型属性
@app.post("/blog/addNodeTypeAttr/")
async def addNodeAttr(node:blog.BlogNode):
    addAttrResult=blog.alertNodeAddAttr(node)
    return jsonable_encoder(addAttrResult)
#删除点类型属性
@app.post("/blog/dropNodeTypeAttr/")
async def dropNodeAttr(node:blog.BlogNode):
    dropAttrResult=blog.alertNodeDropAttr(node)
    return jsonable_encoder(dropAttrResult)


#给某个点类型增加点
@app.post("/blog/insertNode/")
async def insertNode(node:blog.BlogNode):
    insertResult=blog.insertNodeByName(node)
    return jsonable_encoder(insertResult)
@app.post("/blog/dropNode/")
async def insertNode(node:blog.BlogNode):
    dropResult=blog.dropNodeByName(node)
    return jsonable_encoder(dropResult)
@app.post("/blog/fetchNode/")
async def fetchNode(node:blog.BlogNode):
    fetchResult=blog.fetchNodeByName(node)
    return jsonable_encoder(fetchResult)


if __name__ == '__main__':
    import os
    os.system('uvicorn main:app --reload')
