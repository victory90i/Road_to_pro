"""
Python Object-Oriented Programming Exercises
------------------------------------------
Instructions for SEED <WOC> Participants
Each exercise focuses on key OOP concepts with real-world applications.
Complete each exercise and test your implementation.

Exercise 1: Library Management System (Encapsulation)
--------------------------------------------------
Create a Book class that demonstrates proper encapsulation:
- Private attributes should include: __title, __author, __isbn, __is_available, add your own properties that are not private
- Public methods should include: checkout(), return_book(), get_book_info()
- Use proper getters and setters
- Validate ISBN (must be 13 digits)
- Track if book is available for checkout

Example usage:
    book = Book("Python Programming", "John Smith", "9780123456789")
    book.checkout()  # Should mark book as unavailable
    book.get_book_info()  # Should return formatted book information
"""

"""
Exercise 2: Pet Shop Management (Inheritance)
------------------------------------------
Create a hierarchy of pet classes to manage a pet shop:
1. Create a base class Pet with common attributes:
   - name, age, price, species
   - methods: make_sound(), get_info()

2. Create derived classes:
   - Dog (with specific attributes like breed, is_trained)
   - Cat (with specific attributes like fur_color, is_indoor)
   - Bird (with specific attributes like can_fly, wing_span)

Each derived class should override make_sound() appropriately.

Example usage:
    dog = Dog("Max", 2, 500, "Golden Retriever")
    dog.make_sound()  # Should return "Woof!"
    cat = Cat("Whiskers", 3, 300, "Persian")
    cat.make_sound()  # Should return "Meow!"
"""

"""
Exercise 3: Smart Home Devices (Polymorphism)
-------------------------------------------
Create a smart home system with different types of devices:
1. Create a base class SmartDevice:
   - methods: turn_on(), turn_off(), get_status()

2. Create specific device classes:
   - SmartLight (with brightness level)
   - SmartThermostat (with temperature setting)
   - SmartTV (with current channel)

3. Create a SmartHome class that can control multiple devices:
   - Should be able to add devices
   - Turn all devices on/off
   - Get status of all devices

Example usage:
    home = SmartHome()
    home.add_device(SmartLight("Living Room"))
    home.add_device(SmartThermostat("Bedroom"))
    home.turn_all_on()
    home.get_all_status()
"""

"""
Exercise 4: Banking System (Abstraction & Encapsulation)
-----------------------------------------------------
Create an abstract banking system:
1. Create an abstract class Account:
   - Abstract methods: deposit(), withdraw(), get_balance()
   - Protected attributes: _balance, _account_number

2. Create concrete classes:
   - SavingsAccount (with interest rate)
   - CheckingAccount (with overdraft limit)
   - FixedDeposit (with lock-in period)

3. Implement proper validation:
   - No negative deposits
   - Sufficient balance for withdrawals
   - Respect overdraft limits

Example usage:
    savings = SavingsAccount("SA001", 1000, 0.025)  # 2.5% interest
    savings.deposit(500)
    savings.withdraw(200)
    savings.calculate_interest()
"""

"""
Exercise 5: University Course Management (Multiple Inheritance)
-----------------------------------------------------------
Create a course management system using multiple inheritance:
1. Create base classes:
   - OnlineCourse (with zoom_link, platform)
   - InPersonCourse (with room_number, building)
   - Course (with name, code, instructor)

2. Create derived classes:
   - HybridCourse (inherits from both Online and InPerson)
   - Create appropriate methods for:
     - Scheduling classes
     - Managing attendance
     - Submitting assignments

Example usage:
    hybrid = HybridCourse("Python Programming", "CS101", "Dr. Smith")
    hybrid.schedule_online_session("Monday 10:00")
    hybrid.schedule_inperson_session("Wednesday 14:00")
"""

"""
Exercise 6: E-Commerce Shopping Cart (Composition)
-----------------------------------------------
Create a shopping cart system using composition:
1. Create classes:
   - Product (name, price, category, stock)
   - CartItem (product, quantity)
   - ShoppingCart (collection of CartItems)
   - User (with shopping cart)

2. Implement methods:
   - Add/remove items from cart
   - Calculate total
   - Apply discounts
   - Check stock availability

Example usage:
    user = User("John Doe")
    product = Product("Laptop", 999.99, "Electronics", 5)
    user.cart.add_item(product, 1)
    total = user.cart.calculate_total()
"""