from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider
from cassandra.query import dict_factory

CASSANDRA_HOSTS = ['localhost']
CASSANDRA_PORT = 9042
KEY_SPACE = 'datn'

def create_cassandra_session():
    auth_provider = PlainTextAuthProvider(username='cassandra', password='cassandra')
    cluster = Cluster(CASSANDRA_HOSTS, port=CASSANDRA_PORT, auth_provider=auth_provider)
    session = cluster.connect()
    session.set_keyspace(KEY_SPACE)  
    session.row_factory = dict_factory
    return session

