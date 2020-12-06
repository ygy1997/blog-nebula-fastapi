from nebula2.gclient.net import ConnectionPool
from nebula2.Config import Config
# define a config
config = Config()
config.max_connection_pool_size = 10
# init connection pool
connection_pool = ConnectionPool()
# if the given servers are ok, return true, else return false
ok = connection_pool.init([('127.0.0.1', 3699)], config)
def runGql(nGQL):
    print(nGQL)
    # get session from the pool
    session = connection_pool.get_session('root', 'nebula')
    # show hosts
    result = session.execute(nGQL)
    # release session
    session.release()
    res = result._resp.__dict__
    return res
