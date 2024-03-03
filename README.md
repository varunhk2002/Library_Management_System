# Library Management System

This is a web application that helps a librarian manage library books and members. The Librarian can import books from the API, and issue/return books from members of the library.
This web application is made with a Django backend, SQLite3 database and HTML, CSS frontend.

## Home Page

<img width="634" alt="image" src="https://github.com/varunhk2002/Library_Management_System/assets/63897501/d362f615-3c6f-46c5-b706-d3e6c3d3c8c2">

The Home page consists of three functions: Members, Books, Transactions

## Members Page

<img width="942" alt="image" src="https://github.com/varunhk2002/Library_Management_System/assets/63897501/9efcceec-e33f-4046-81ed-91ef3db5ed7d">

This page consists of a list of existing members, their details and their renting status with fees owed.

## Add New Member

<img width="948" alt="image" src="https://github.com/varunhk2002/Library_Management_System/assets/63897501/b1e1ef31-f2c1-4e05-9473-68272666b8a2">

The librarian can register a new member from this page


## Books Page
<img width="933" alt="image" src="https://github.com/varunhk2002/Library_Management_System/assets/63897501/43365268-af81-4226-af08-bb189bb7bc11">

<img width="928" alt="image" src="https://github.com/varunhk2002/Library_Management_System/assets/63897501/4643427e-7e7f-4653-b340-9a13732ac640">

This page consists of two things: a book searching tool based on title/author, as well as the list of all the books in the system and their status.


## Add New Book\

<img width="944" alt="image" src="https://github.com/varunhk2002/Library_Management_System/assets/63897501/7841a7b7-9bbf-458a-9c21-ac48991ab2cc">

The Librarian can add a new book from the Frappe API by searching with Title or ISBN and can state the number of books required.


## Transactions History
<img width="925" alt="image" src="https://github.com/varunhk2002/Library_Management_System/assets/63897501/4281d358-8935-4803-8cb7-372ac20baf63">

This page tracks the transaction (issues and returns) history of the library along with book, member details.


## Outstanding Debt

<img width="919" alt="image" src="https://github.com/varunhk2002/Library_Management_System/assets/63897501/c988cd20-2f71-431e-9b81-30c0fa662fb9">

Members with outstanding debt cannot issue a new book unless it has been repaid.


