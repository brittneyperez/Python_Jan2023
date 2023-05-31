## **Week 2 - D4** | ２０２３年０１月１７日（火）

### Overview
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

We can use Python OOP to make DRY code and reuse the layout of our data using classes.

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

## Topics to Cover
- Intro to Python OOP
    - DRY
    - Classes vs Instance
        - Class Student vs (actual) Instance of student
        - **`self`** : similar to `this` in JavaScript
    - **Classes**
        - Naming conventions, upercase singular
        - Defining a Class
    - **Instances**
        - Create an **Instance** of a Class
    - **Attributes** : similar to variables/keys
        - Class attributes
        - Instance attributes
    - **Methods**
        - Class
        - Instance
        - Static
    - Chaining Methods
        - return `self`
            - _But why?_
    - Class constructor with data dictionary
