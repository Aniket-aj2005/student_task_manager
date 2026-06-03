import mysql.connector

def get_database_connection():
    connection = mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        password = 'aniket#$123',
        database = 'student_tasks_manager',
        port = 4000
    )
    
    return connection





# def get_database_connection():
#     connection = mysql.connector.connect(
#         host = 'localhost',
#         user = 'root',
#         password = 'aniket#$123',
#         database = 'student_tasks_manager'
#         )
    
#     return connection
