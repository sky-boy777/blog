from django.test import TestCase

# # 电影循环插入数据库，movie_view
# import json
# from datetime import datetime
#
# with open('movie.json', 'r', encoding='utf8') as f:
#     for i in f:
#         i = json.loads(i)
#         i['time'] = datetime.strptime(i['time'], '%Y-%m-%d')
#         try:
#             movie = MovieModel(**i)
#             movie.save()
#         except Exception as e:
#             print(e)
#             continue

