from django.shortcuts import render
from django.db import connection

def dictfetchall(cursor): 
    "Returns all rows from a cursor as a dict" 
    desc = cursor.description 
    return [
            dict(zip([col[0] for col in desc], row)) 
            for row in cursor.fetchall() 
    ]    

def index(request):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM students")
        result = dictfetchall(cursor)
    # for row in result:
    #     record = {'id':row[0],'fname':row[1],'lname':row[2]}
    #     values.append(record)
    #     print(record)
    print(result)
    return render(request,"index.html")