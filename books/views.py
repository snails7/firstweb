from audioop import reverse

from django.shortcuts import render, redirect, reverse
from django.db  import connection


# Create your views here.
from matplotlib.artist import get


def index(request):
#    db = pymysql.connect(
#        host='127.0.0.1',
#        user='root',
#        password='wb851205',
#        db='books',
#        charset='utf8',
#        cursorclass=pymysql.cursors.DictCursor
#    )
    cursor = connection.cursor()
    cursor.execute("select id, name, people from list")
    rows = cursor.fetchall()

    context = {
        'books':rows
    }

    return render(request, 'index.html' , context=context)


def get_corsor():
    return connection.cursor()


def book_add(request):
    if request.method == 'GET':
        return render(request, 'book_add.html')
    else:
        name = request.POST.get("name")
        author = request.POST.get("author")
        cursor = get_corsor()
        cursor.execute("insert into list(id, name, people) values(null, '%s', '%s')" % (name, author))
        return redirect(reverse('index'))



def book_detail(request, book_id):
    cursor = get_corsor()
    cursor.execute("select id, name, people from list where id=%s" % book_id)
    book = cursor.fetchone()
    return render(request, 'book_detail.html', context = {"book": book})

def delete_book(request):
    if request.method == 'POST':
        book_id = request.POST.get('book_id')
        cursor = get_corsor()
        cursor.execute("delete from list where id=%s" % book_id)
        return redirect(reverse('index'))
    else:
        raise RuntimeError("Error deleting")


