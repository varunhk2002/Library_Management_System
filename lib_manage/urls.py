from django.urls import path
from . import views

app_name = 'lib_manage'

urlpatterns = [
    path("", views.index, name="index"),
    path("books/", views.booksview, name='booksview'),
    path("members/", views.membersview, name='membersview'),
    path("add_members/", views.addMember, name='addMember'),
    path("new_book/", views.newBook, name="newBook"),
    path("issue/<int:id>/", views.issue, name="issue"),
    path("return/<int:id>/", views.return_book, name='return_book'),
    path("transactions/", views.transacView, name='transacView'),
    path("collect_fee/", views.collect_fee, name='collect_fee'),
    path("search/", views.search, name='search')
]