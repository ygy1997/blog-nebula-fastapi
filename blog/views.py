from pydantic import BaseModel
from nebulaApi.connect import runGql
from utils.utils import delLastChar
Typedict={}

# 声明参数模型
class BlogNode(BaseModel):
    nodeType: str
    nodeIdByHash: str=None
    description: str = None
    properties: dict = None


#查询属性类型
def DESCRIBENODE(nodeType):
    nGQL=f"""
    USE blog;
    DESCRIBE tag {nodeType};
    """
    query_resp = runGql(nGQL)
    print(query_resp)
    for attr in query_resp['data'].rows:
        attrNames = bytes.decode(attr.values[0].get_sVal())
        attrType = bytes.decode(attr.values[1].get_sVal())
        Typedict[attrNames]=attrType
    return query_resp

def DESCRIBEEDGE(edgeName):
    nGQL="""
    USE blog;
    DESCRIBE tag MainCategory;
    """
    query_resp = runGql(nGQL)
    return query_resp
###########点类型 增删改查
def createNode(node):
    propertiesString=""
    for attr,attrType in node.properties.items():
        propertiesString+=f"{attr} {attrType},"
    nGQL=f"""
     USE blog;
     CREATE TAG {node.nodeType}({propertiesString});
    """
    query_resp = runGql(nGQL)
    return query_resp

def getNode(node):
    nGQL=f"""
    USE blog;
    DESCRIBE tag {node.nodeType};
    """
    query_resp = runGql(nGQL)
    return query_resp

def dropNode(node):
    nGQL=f"""
     USE blog;
     DROP  TAG {node.nodeType};
    """
    query_resp = runGql(nGQL)
    return query_resp

def alertNodeAddAttr(node):
    propertiesString=""
    for attr,attrType in node.properties.items():
        propertiesString+=f"{attr} {attrType},"
    propertiesString=delLastChar(propertiesString)
    nGQL=f"""
     USE blog;
     ALTER TAG {node.nodeType} ADD ({propertiesString});
    """
    query_resp = runGql(nGQL)
    return query_resp

def alertNodeDropAttr(node):
    propertiesString=""
    for attr,attrType in node.properties.items():
        propertiesString+=f"{attr},"
    propertiesString=delLastChar(propertiesString)

    nGQL=f"""
     USE blog;
     ALTER TAG {node.nodeType} DROP ({propertiesString});
    """
    query_resp = runGql(nGQL)
    return query_resp

#增删改查某个点
def insertNodeByName(node):
    attrString=""
    attrValuesString=""
    for attr,attrValues in node.properties.items():
        attrString+=f"{attr},"
        try:
            attrType=Typedict[attr]
        except:
            DESCRIBENODE(node.nodeType)
            attrType=Typedict[attr]
        if attrType=="string":
            attrValuesString+=f'"{attrValues}",'
        else:
            attrValuesString+=f'{attrValues},'

    attrString,attrValuesString=map(delLastChar,[attrString,attrValuesString])

    nGQL=f"""
     USE blog;
     INSERT VERTEX {node.nodeType}({attrString}) VALUES "{node.nodeIdByHash}":({attrValuesString});
    """
    query_resp = runGql(nGQL)
    return query_resp

def dropNodeByName(node):
    nGQL=f"""
     USE blog;
     DELETE VERTEX "{node.nodeIdByHash}";
    """
    query_resp = runGql(nGQL)
    return query_resp

def fetchNodeByName(node):
    nGQL=f"""
     USE blog;
     FETCH PROP ON MainCategory "{node.nodeIdByHash}";
    """
    query_resp= runGql(nGQL)
    return query_resp
