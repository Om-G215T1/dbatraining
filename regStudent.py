from pymongo import MongoClient

client = MongoClient('mongodb+srv://omg151315_db_user:frq1BclS1vqQhKPA@cluster0.dwztzj3.mongodb.net/?appName=Cluster0')
db = client['event_db']
collection = db['student_registration']
#  collection.insert_one({
#     'student_id': "12345",
#     'name': 'John Doe',
#     'registration_date': '2024-01-15',
#     'event_id': 'E1001'
# })
# to insert the multiple event using collection
collection.insert_many([
    {
        'student_id': "12346",
        'name': 'Jane Smith',
        'registration_date': '2024-01-16',
        'event_id': 'E1002'
    },
    {
        'student_id': "12347",
        'name': 'Alice Johnson',
        'registration_date': '2024-01-17',
        'event_id': 'E1003'
    },
    {
        'student_id': "12348",
        'name': 'Bob Brown',
        'registration_date': '2024-01-18',
        'event_id': 'E1004',
    },
    {
        'student_id': "12349",
        'name': 'Bob Brown',
        'registration_date': '2024-01-19',
        'event_id': 'E1005',
    }
])
# to delete a single event from database
# collection.delete_one({'student_id': '12345'})
# # to delete multiple events from database
# # collection.delete_many({'venue': 'Bareilly'})
# # to fetch the events from database
# for registration in collection.find():
#     print(registration)
# # to update a single event in database
# collection.update_one(
#     {'student_id': '12349'},
#     {'$set': {'name': 'Robert Brown'}}
# )