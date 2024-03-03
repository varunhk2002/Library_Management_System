from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Books, Member, Transaction
from django.urls import reverse
import requests
from django.contrib import messages
from django.db.models import F

# Create your views here.

def index(request):
    if request.method == 'GET':
        return render(request, 'lib_manage/index.html')

def booksview(request):
    if request.method == 'GET':
        books_data = list(Books.objects.all())
        return render(request, 'lib_manage/books.html', {'books_data':books_data})

def search(request):
    if request.method == 'POST':
        author = request.POST['author']
        title = request.POST['title']

        search_result1 = []
        search_result2 = []
        if author != '':
            search_result1 = list(Books.objects.filter(author__contains=author))
        
        if title != '':
            search_result2 = list(Books.objects.filter(title__contains=title))
        search_result = search_result1 + search_result2
        
        return render(request, 'lib_manage/search_result.html', {'books_data': search_result})
    
def membersview(request):
    if request.method == 'GET':
        member_data = list(Member.objects.all())
        return render(request, 'lib_manage/members.html', {'member_data':member_data})

def addMember(request):
    if request.method == 'GET':
        return render(request, 'lib_manage/add_member.html')
    elif request.method == 'POST':
        name = request.POST['name']
        number = request.POST['number']

        add_query = Member.objects.create(name=name, number=number)
        add_query.save()

        return HttpResponseRedirect(reverse("lib_manage:membersview"))

def newBook(request):
    if request.method == 'GET':
        return render(request, 'lib_manage/new_book.html')
    elif request.method == 'POST':
        title = request.POST['title']
        isbn = request.POST['isbn']
        num = request.POST['quantity']

        response = requests.get(f'https://frappe.io/api/method/frappe-library?title={title}&isbn={isbn}').json()

        if len(response['message']) == 0:
            messages.error(request, 'Book not Found')
            return HttpResponseRedirect(reverse('lib_manage:newBook'))

        if num == '':
            num = 1
        else:
            num = int(num)
    
        i = 0
        while i<num:
            import_book = Books.objects.create(title=response['message'][0]['title'], author=response['message'][0]['authors'], isbn=response['message'][0]['isbn'], publisher=response['message'][0]['publisher'])
            import_book.save()
            i+=1

        return HttpResponseRedirect(reverse('lib_manage:booksview'))


def issue(request, id):
    if request.method == 'GET':
        #print(id)
        available_books = list(Books.objects.filter(status=True))
        return render(request, 'lib_manage/issue.html', {'available_books':available_books, 'member_id':id})
    
    elif request.method == 'POST':
        book_id = request.POST['book_id']
        
        member_obj = Member.objects.get(id=id)
        book_obj = Books.objects.get(id=book_id)
        transaction_obj = Transaction.objects.create(member=member_obj, book=book_obj, type='issue')
        transaction_obj.save()

        update_member = Member.objects.filter(id=id).update(holding=book_obj)
        update_book = Books.objects.filter(id=book_id).update(holder=id, status=False)

        return HttpResponseRedirect(reverse('lib_manage:membersview'))


def return_book(request, id):
    if request.method == 'GET':
        member_obj = Member.objects.get(id=id)
        book_info = Books.objects.get(holder=id)
        # print(member_obj)
        
        transaction_obj = Transaction.objects.create(member=member_obj, book=book_info, type='return')

        update_book = Books.objects.filter(holder=id).update(status=True, holder=None)
        update_member = Member.objects.filter(id=id).update(holding=None, fees=F('fees')+100)

        return HttpResponseRedirect(reverse('lib_manage:membersview'))

def collect_fee(request):
    if request.method == 'POST':
        member_id = request.POST['member_id']
        update_member = Member.objects.filter(id=member_id).update(fees=0)
        return HttpResponseRedirect(reverse('lib_manage:membersview'))

def transacView(request):
    if request.method == 'GET':

        transaction_list = list(Transaction.objects.all())

        return render(request, 'lib_manage/transactions.html', {'transaction_list':transaction_list})