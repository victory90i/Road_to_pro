
# Exercise 1: Library Management System (Encapsulation)
# --------------------------------------------------
# Create a Book class that demonstrates proper encapsulation:

    
# - Private attributes should include: __title, __author, __isbn, __is_available,
#  add your own properties that are not private
class book():
  def __init__(self,title,author,isbn,year_published,pages):
    self.__title=title
    self.__author=author
    self.__isbn=isbn
    self.__is_available=True or False
    self.year=year_published
    self.pages=pages

# - Public methods should include: checkout(), return_book(), get_book_info()
def checkout(self):
  if self.__is_available:
    self.__is_available=False
    print(f"{self.__title} is unavailable for the moment")
  else:
    self.__is_avaliable=True
    print(f"{self.__title} is still available")
def return_book(self):
  if not self.__is_available:
    self.__is_available=True
    print(f"{self.__title} has been returned")
  else:
    self.__is_available=False
    print(f"{self.__title} has not been return ")
def get_book_info(self):
  print(f"title:{self.__title} ,author:{self.__author},isbn:{self.__isbn}\n")
  print(f"year published:{self.year},pages:{self.pages}")

def _validate_isbn(self):
  return self.__isbn.isdigit() and len(self.__isbn)==13
# use proper getter and setters
@property
def title(self):
  return self.__title
@title.setter
def title(self, new_title):
  if isinstance(new_title,str) and new_title.strip():
    self._title=new_title
  else:
    raise ValueError("title must be a non empty string")
@property
def author(self):
  return self._author
@author.setter
def author(self,new_author):
  if isinstance(new_author,str) and new_author.strip():
    self._author=new_author
  else:
    raise ValueError("author mst be a non empty string")
@property
def isbn(self):
  return self.__isbn
@isbn.setter
def isbn(self,new_isbn):
  if new_isbn.isdigit() and len(new_isbn)==13:
    self.__isbn=new_isbn
  else:
    raise ValueError("isbn must be exactly 13 digits no more no less")
@property
def is_available(self):

  return self._is_available
Book=book("loving God with all your mind","elisabeth george","9321345678456",2007,78)
book.checkout()
book.get
print("title:", book._title)
print("author:",book.__author)
print("ISBN:",book.__isbn)
print("available",book._is_available)

  


# - Validate ISBN (must be 13 digits) 
# - Track if book is available for checkout

# Example usage:
#     book = Book("Python Programming", "John Smith", "9780123456789")
#     book.checkout()  # Should mark book as unavailable
#     book.get_book_info()  # Should return formatted book information
# """
