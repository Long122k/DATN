# import sys
# sys.path.append('data_access')
# from city_dao import fetch_city_info

# class CityLogic:
#     def __init__(self, city_dao):
#         self.city_dao = city_dao

#     def get_city_info(self, city_name):
#         city_data = self.city_dao.fetch_city_info(city_name)

#         # Perform any additional business logic or data manipulation here
#         # For example, you can format the activity list as a comma-separated string
#         city_data['activity'] = ', '.join(city_data['activity'])

#         return city_data

# CityLogic.get_city_info(CityLogic, 'Ha Tinh')