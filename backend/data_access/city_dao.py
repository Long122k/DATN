import sys
sys.path.append('database')
from cassandra_connector import create_cassandra_session

def fetch_city_info(city_name):
    session = create_cassandra_session()

    query = f"SELECT activity, city_image, city_name, country_name, intro, title FROM city_intro WHERE city_name = '{city_name}' ALLOW FILTERING;"
    result = session.execute(query)

    city_info = {}
    for row in result:
        city_info['activity'] = row['activity']
        city_info['city_image'] = row['city_image']
        city_info['city_name'] = row['city_name']
        city_info['country_name'] = row['country_name']
        city_info['intro'] = row['intro']
        city_info['title'] = row['title']

    session.shutdown()

    return city_info

# print(fetch_city_info("Ha Tinh"))
