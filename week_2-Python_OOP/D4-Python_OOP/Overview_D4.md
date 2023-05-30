## ２０２３年０５月２９日（月）

## Week 2

### Recap

## Topics to Cover
There is a much concise method to making objects. Instead of writing the same, redundant pieces of information:
```py
# Using a dictionary to save user to DB
user_one = {
    'first_name' : 'Jane',
    'last_name' : 'Doe',
    'id' : 1,
    'DOB' : 19990428,
}
```

We can use Python OOP to make DRY code and resuse the layout of our data using classes.
```py
# Using class containing a constructor and its attributes
class User:
    id = 1
    def __init__ (self, first_name, last_name, DOB):
        self.first_name = first_name
        self.last_name = last_name
        self.DOB = DOB
        self.id = User.id

jane_doe = User('Jane', 'Doe', 19990428)
```