## TODO

### ACCOUNT CRUD

- [x] Creation
- [x] Read
- [x] Update
- [x] Deletion

### USER TYPES CRUD

- [ ] Prevent edit of admin
- [x] Creation
- [x] Read
- [x] Update
- [x] Deletion

### BOOKS CRUD

- [x] Creation
- [x] Read
- [x] update
  > select with check, then select them from id of selected then list them with ui
- [x] Deletion

### CATEGORY CRUD

- [x] Creation
- [x] Read
- [x] Update
- [x] Deletion

- [ ] display
  > display on last click

### TRANSACTION

- [x] QR Code

  > select which client to send request

- [x] Generate Qr on insert
- [x] Delete Qr on delete
- [x] add web sockets

### RECORD

- [x] Copies available
  > (Title, Author, available copies)
- [x] borrower records
  > (Book id, Title, borrower name, date, due date, status)
- [x] user records
  > (full name, role, email, borrowed books)
- [x] categories
  > (category, books available)

### CATEGORY

select books returns 2d array of book info
select cateogories returns 2d array of categories
select joint categories returns 2d arrays of category id and book using book id
now, i wanna have 2d array of boolean where all are false for every categories except the one from joint category result
