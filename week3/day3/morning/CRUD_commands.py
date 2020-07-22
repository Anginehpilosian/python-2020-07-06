from books_app.models import Author, Book, Review

# from books_app.models import *

# create a book
Book.objects.create(
    title="The Great Gatsby",
    description="Something great"
)
# create an author
Author.objects.create(
    first_name="Clint",  # request.POST['first_name']
    last_name="Eastwood"
)

book_to_add_author_to = Book.objects.get(title="The Great Gatsby")

author_of_book_to_add = Author.objects.get(first_name="Clint")
book_to_add_author_to.authors.all()
# create many to many relationship between book and author
book_to_add_author_to.authors.add(author_of_book_to_add)
book_to_add_author_to.authors.all()


book_to_add_review = Book.objects.get(id=1)
# create a review
Review.objects.create(
    reviewer="Anonymous user2",
    book=book_to_add_review,
    text="it was awesome"
)

# read a book
book_to_add_author_to.title
# read an author
author_of_book_to_add.first_name
# read a review
review_to_check_out = Review.objects.get(id=2)

# update a book
# update an author
# update a review
review_to_update = Review.objects.get(id=1)
review_to_update.text
review_to_update.text = 'I only watched the movie'
review_to_update.save()
review_to_update.text

# delete a book
# delete an author
# delete a review

review_to_delete_because_they_didnt_read_the_book = Review.objects.get(id=1)
review_to_delete_because_they_didnt_read_the_book.delete()
review_to_delete_because_they_didnt_read_the_book.text
Review.objects.get(id=1)
