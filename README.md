# Python A118 - Complete Python Fundamentals Course 🐍

A comprehensive, day-by-day Python learning journey covering fundamental concepts through object-oriented programming. This structured curriculum progresses from basic printing and keywords to advanced OOP concepts, file handling, and exception handling.

## 📋 Course Overview

This repository contains complete course materials for the Python A118 program, with 40+ days of structured learning:
- **Fundamentals**: Print statements, variables, data types, operators
- **Control Flow**: Conditional statements, loops, jumping statements  
- **Functions**: Built-in methods, user-defined functions
- **Advanced Concepts**: File handling, CSV/Binary files, exception handling
- **OOP**: Classes, objects, constructors, OOPS variables

---

## 📚 Complete Learning Curriculum

### **Day 1: Print Statements & Keywords**
Master the fundamentals of Python output and language reserved words:

**Topics Covered:**
- **Print Function**: Output text and values using the `print()` function
  - Simple text printing: `print('Hello Python')`
  - Printing mathematical expressions: `print('sum:', 98+45)`
  - Printing with multiple arguments and automatic spacing
  
- **Keywords in Python**: Reserved words that have special meaning
  - Importing the `keyword` module to access Python's keyword list
  - `keyword.kwlist` - displays all Python keywords
  - `keyword.iskeyword()` - checks if a word is a keyword
  - Understanding keyword sensitivity (e.g., `if` is a keyword, but `IF` is not)
  - Total of 35+ Python keywords that cannot be used as variable names

---

### **Day 2: Creating Identifiers, Variables & String Formatting**
Learn variable naming conventions and multiple ways to format and display strings:

**Topics Covered:**
- **Identifiers (Variable Names)**: Rules for naming variables
  - Must start with a letter or underscore (_)
  - Can contain letters, digits, and underscores
  - Case-sensitive (e.g., `Ename` and `ename` are different)
  - Examples: `a`, `Ename`, `pna_me`, `_student_name`, `sname123`
  
- **Variables**: Storing and retrieving data
  - Creating single variables: `a = 98`
  - Multiple variable assignment: `a, b, c = 10, 20, 30`
  - Using `id()` function to get memory address of variables
  
- **String Formatting Techniques**:
  - Basic concatenation: `'my name is ' + name`
  - **F-strings (Modern approach)**: `f'my name is:{name}'` - cleanest and most readable
  - Combining multiple values: `f'employee name:{ename} and salary is:{salary}'`
  
- **Comments**: Documenting code
  - Single-line comments using `#`
  - Multi-line comments using `''' '''` or `""" """`
  
- **Escape Sequences**: Special characters in strings
  - `\n` - newline (move to next line)
  - Printing multiple lines: `'python\njava\nsql\nwebtech'`

---

### **Day 3: Data Types Overview**
Explore Python's fundamental data types and their characteristics:

**Topics Covered:**
- **Integer (int)**: Whole numbers without decimal points
  - `a = 98` creates an integer
  - Default value: `0`
  - `type()` function returns `<class 'int'>`
  - Works with arithmetic operations
  
- **Float (float)**: Numbers with decimal points
  - `b = 98.48` creates a float
  - Default value: `0.0`
  - `type()` function returns `<class 'float'>`
  
- **Complex Numbers (complex)**: Combination of real and imaginary parts
  - Format: `10+5j` (real part + imaginary part)
  - `a = 10+5j` creates a complex number
  - Can perform arithmetic on complex numbers: `(10+6j) + (20+3j) = (30+9j)`
  - Imaginary unit represented by `j` (not `i`)
  
- **Boolean (bool)**: Logical values for conditional logic
  - Two values: `True` (equivalent to 1) and `False` (equivalent to 0)
  - Can be used in arithmetic: `True + 98 = 99`, `False * 95 = 0`
  - Default value of `bool()`: `False`
  
- **String (str)**: Text data
  - Single quotes: `'python'`
  - Double quotes: `"HEllo python"`
  - Triple quotes for multi-line strings
  - `type()` returns `<class 'str'>`

---

### **Day 4: String Data Type - Indexing & Slicing**
Master accessing and extracting parts of strings:

**Topics Covered:**
- **Indexing Strings**: Accessing individual characters
  - **Positive Indexing**: `msg[0]` gets first character, `msg[5]` gets sixth character
  - **Negative Indexing**: `msg[-1]` gets last character, `msg[-3]` gets third-to-last
  - Error handling: Out of range indices raise `IndexError`
  
- **String Length**: Using `len()` function
  - `len('python')` returns `6`
  
- **Slicing Strings**: Extracting substrings
  - **Syntax**: `string[start:end:step]`
  - Start index is **included**, end index is **excluded**
  - `msg[2:13:1]` - slice from index 2 to 12, step by 1
  - `msg[4:15:2]` - every 2nd character from index 4 to 14
  - `msg[-16:-3:1]` - negative slicing using negative indices
  
- **Step Parameter**: Controlling character progression
  - Default step is 1 (every character)
  - Even indices: `string[0::2]` gets characters at positions 0, 2, 4, 6...
  - Odd indices: `string[1::2]` gets characters at positions 1, 3, 5, 7...
  
- **Reverse Slicing**: 
  - `string[::-1]` reverses entire string
  - `string[-2::-2]` reverse with step 2
  - Negative step reverses direction

---

### **Day 5: List Data Type - Indexing & Slicing**
Work with ordered, mutable collections of elements:

**Topics Covered:**
- **List Basics**: Creating and understanding lists
  - **Homogeneous**: `list1 = [10, 20, 30, 40, 98]` - same data type
  - **Heterogeneous**: `list2 = [98, 'smith', True, 100, 98]` - mixed data types
  - `type()` returns `<class 'list'>`
  
- **Indexing Lists**: Similar to strings
  - Positive indexing: `list[0]` first element, `list[3]` fourth element
  - Negative indexing: `list[-1]` last element, `list[-3]` third-to-last
  - Out of range raises `IndexError`
  
- **Nested Lists**: Lists containing other lists
  - `nested = [10, 20, [100, 200, 300], 'analyst']`
  - Accessing nested elements: `nested[4][1]` - second element of nested list
  - Slicing nested lists: `nested[4][1:-1:1]` - slice within nested list
  
- **Slicing Lists**: Extracting portions of lists
  - Forward slicing: `list[0:3:1]` gets first 3 elements
  - With step: `list[0:7:2]` gets every 2nd element
  - Negative slicing: `list[-7:-4:1]` uses negative indices
  - Reverse slicing: `list[6:0:-1]` reverses portion of list

---

### **Day 6: Tuple Data Type - Indexing & Slicing**
Master immutable, ordered sequences of elements:

**Topics Covered:**
- **Tuple Basics**: Creating tuples (immutable sequences)
  - Single element: `t2 = (10,)` - note the comma to distinguish from parentheses
  - Without comma: `t1 = (10)` is just a number, not a tuple
  - **Homogeneous**: `t3 = (10, 20, 30, 98)` - same data types
  - **Heterogeneous**: `t4 = (10, 'smith', 98.45, True, (1,2,3), [98,100])` - mixed types
  - `type()` returns `<class 'tuple'>`
  
- **Immutability**: Tuples cannot be modified after creation
  - Cannot add, remove, or change elements
  - More memory efficient than lists for fixed data
  
- **Indexing Tuples**: Accessing individual elements
  - Same as strings and lists
  - Positive: `tuple[0]`, `tuple[3]`
  - Negative: `tuple[-1]`, `tuple[-3]`
  
- **Slicing Tuples**: 
  - **Positive slicing**: `t1[0:5:1]` - first 5 elements
  - **Negative slicing**: `t1[-9:-1:1]` - from 9th-last to 1st-last
  - **Reverse slicing**: `t1[8:2:-2]` - backward with step 2
  - With step parameter for custom progression

---

### **Day 7: Set & Dictionary Data Types - Range**
Explore unique collections, key-value mappings, and number ranges:

**Topics Covered:**
- **Sets**: Unordered collections of unique elements
  - `s1 = {10, 20, 30, 20, 20, 40, 98}` - duplicates automatically removed
  - Duplicate elements are ignored: `{10, 20, 30, 20}` becomes `{10, 20, 30}`
  - `type()` returns `<class 'set'>`
  - Useful for membership testing and removing duplicates
  - **Note**: Direct indexing on sets is not supported; convert to list first
  
- **Dictionaries**: Key-value pair collections
  - Format: `data = {'ename': 'smith', 'sal': 98000, 'job': 'analyst'}`
  - Accessing values: `data['ename']` returns `'smith'`
  - **Nested Dictionaries**: Multiple records
    ```python
    employee = {
        'emp1': {'ename': 'smith', 'sal': 900},
        'emp2': {'ename': 'king', 'sal': 2000},
        'emp3': {'ename': 'allen', 'sal': 1250}
    }
    ```
  - Accessing nested values: `employee['emp3']['ename']` returns `'allen'`
  
- **Range (range)**: Generate sequences of numbers efficiently
  - `range(6)` - 0 to 5: `[0, 1, 2, 3, 4, 5]`
  - `range(10, 16)` - 10 to 15: `[10, 11, 12, 13, 14, 15]`
  - `range(1, 11, 2)` - start, stop, step: `[1, 3, 5, 7, 9]`
  - `range(10, 5, -1)` - descending: `[10, 9, 8, 7, 6]`
  - Convert to list: `list(range(6))` for viewing as list
  - Indexing on range: `nums = range(100, 501, 100); nums[0]` returns `100`

---

### **Day 8: Type Casting - Implicit & Explicit Type Conversion**
Convert between different data types automatically and manually:

**Topics Covered:**
- **Implicit Type Casting**: Python automatically converts types when needed
  - When adding int and float: `98 + 35.67 = 133.67` (result is float)
  - Result type is `<class 'float'>`
  - Automatic promotion to more general type
  
- **Explicit Type Casting**: Manual conversion between types
  
  **Integer Conversions**:
  - `float(57)` → `57.0`
  - `complex(57)` → `57+0j`
  - `bool(57)` → `True` (any non-zero is True)
  - `str(57)` → `'57'`
  - `list()`, `tuple()`, `set()`, `dict()` raise `TypeError`
  
  **Float Conversions**:
  - `int(89.56)` → `89` (truncates decimal)
  - `complex(89.56)` → `(89.56+0j)`
  - `bool(89.56)` → `True`
  - `str(89.56)` → `'89.56'`
  
  **Complex Conversions**:
  - `bool(10+0j)` → `True`
  - `str(10+0j)` → `'(10+0j)'`
  - `int()` and `float()` on complex raise `TypeError`
  
  **Boolean Conversions**:
  - `int(True)` → `1`, `int(False)` → `0`
  - `float(True)` → `1.0`
  - `complex(True)` → `(1+0j)`
  - `str(True)` → `'True'`
  
  **String Conversions**:
  - `int('python')` → `ValueError` (not numeric)
  - `list('python')` → `['p', 'y', 't', 'h', 'o', 'n']` (splits into characters)
  - `tuple('python')` → `('p', 'y', 't', 'h', 'o', 'n')`
  - `set('python')` → `{'p', 'y', 't', 'h', 'o', 'n'}` (unique characters)
  - `bool('python')` → `True` (non-empty string)
  
  **Collection Conversions**:
  - `list([10, 20, 30])` creates list copy
  - `tuple()` converts collections to tuples
  - `set()` converts to set, removing duplicates
  - `str()` converts collections to string representation

---

### **Day 9: Input & eval() Statements**
Learn to interact with users and evaluate dynamic expressions:

**Topics Covered:**
- **Input Function**: Reading user input
  - `number = input('enter the value:')` - takes user input as string
  - Input is always returned as string type: `type(number)` returns `<class 'str'>`
  - `num = int(input('enter the value:'))` - convert to integer directly
  - Can be combined with type conversion on same line
  
- **eval() Function**: Evaluate string expressions
  - `n = eval(input('enter the decimal value:'))` - evaluates Python expression
  - `eval()` intelligently determines data type based on input
  - "10" becomes int, "10.5" becomes float
  - Returns `<class 'float'>` for decimal inputs

---

## 🔧 Operators - Foundation of Computation

### **Day 9: Arithmetic Operators** (Operators folder)
Perform mathematical calculations with different data types:

**Topics Covered:**
- **Addition (+)**:
  - Numbers: `98 + 76 = 174`
  - Strings: `'Smith is earning ' + str(9800)` = `'Smith is earning 9800'`
  - Lists: `[10, 20, 30] + [40, 50, 60]` = `[10, 20, 30, 40, 50, 60]` (concatenation)
  - Integers and floats: `67 + 56.89 = 123.89`
  - Complex numbers: `100 + (10+5j) = (110+5j)`
  - Tuples: `(1,2,3) + (10,20,30)` = `(1, 2, 3, 10, 20, 30)`
  
- **Subtraction (-)**: 
  - Only works with numbers: `98 - 67 = 31`
  
- **Multiplication (*)**: 
  - Numbers: `3 * 2 = 6`
  - String repetition: `4 * ' python'` = `' python python python python'`
  
- **True Division (/)**: 
  - Always returns float: `98 / 78 = 1.256...`
  - Even dividing integers: `10 / 2 = 5.0`
  
- **Floor Division (**)**: 
  - Integer result: `78 // 34 = 2` (quotient only)
  - Useful for removing last digits: `8734567 // 10 = 873456`
  - Remove last 2 digits: `8734567 // 100 = 87345`
  
- **Modulus (%)**:
  - Remainder after division: `11 % 2 = 1`
  - Extract last digit: `7689 % 10 = 9`
  - Extract last 3 digits: `7689 % 1000 = 689`
  - **ZeroDivisionError** if dividing by zero
  
- **Exponentiation (**)**: 
  - Power operation: `2 ** 3 = 8` (2×2×2)
  - Works with negative powers: `2 ** -1 = 0.5`

---

### **Day 10: Relational Operators** (Operators folder)
Compare values and make decisions based on comparisons:

**Topics Covered:**
- **Greater Than (>)**:
  - Numbers: `98 > 40` → `True`
  - Strings: `'microsoft' > 'apple'` → `True` (alphabetical comparison using ASCII)
  - `ord('m')` = 109, `ord('a')` = 97
  
- **Less Than (<)**:
  - `98 < 48` → `False`
  
- **Equal To (==)**:
  - Numbers: `98 == 98` → `True`
  - Strings (case-sensitive): `'jspiders' == 'Jspiders'` → `False`
  - Lists: `[10,20,30] == [10,20,30]` → `True` (content comparison)
  
- **Not Equal To (!=)**:
  - `list1 != list2` → `False` if contents are same
  
- **Greater Than or Equal To (>=)**: Returns True if left ≥ right
  
- **Less Than or Equal To (<=)**: Returns True if left ≤ right
  
- **String Comparison**: Uses ASCII/Unicode values for alphabetical ordering

---

### **Day 11: Assignment, Logical, Membership & Identity Operators** (Operators folder)
Assign values, combine conditions, test membership, and check object identity:

**Topics Covered:**
- **Swapping Variables**:
  - Without third variable: `a, b = b, a` (Python tuple unpacking)
  - With third variable: `temp = a; a = b; b = temp`
  
- **Compound Assignment Operators**:
  - `+=` : `a += 2` is equivalent to `a = a + 2`
  - `-=` : `a -= 2` is equivalent to `a = a - 2`
  - `*=` : `a *= 2` is equivalent to `a = a * 2`
  - `/=` : `a /= 3` is equivalent to `a = a / 3`
  - `//=`: `a //= 3` is equivalent to `a = a // 3`
  - `%=` : `a %= 3` is equivalent to `a = a % 3`
  - `**=`: `a **= 3` is equivalent to `a = a ** 3`
  
- **Logical Operators**:
  - **AND (`and`)**: Both conditions must be True
    - `a < b and b < c` → checks if both are true
    - `10 < 50 and 50 < 60` → `True`
    - `10 < 50 and 50 > 60` → `False`
  - **OR (`or`)**: At least one condition must be True
    - `a > b or b < c` → checks if either is true
    - `10 > 50 or 50 < 60` → `True`
  - **NOT (`not`)**: Reverses boolean value
    - `not (0)` → `True`
    - `not (1)` → `False`
    - `not (a > b or b < a)` → reverses entire expression
  - Chaining: `a < b and b < c and c < d and d > a` → `True`
  
- **Membership Operators**:
  - **in**: Checks if element exists in collection
    - `'p' in 'python'` → `True`
    - `'P' in 'python'` → `False` (case-sensitive)
    - `'th' in 'python'` → `True` (substring check)
  - **not in**: Checks if element does NOT exist
    - `'p' not in 'python'` → `False`
    - `'x' not in 'python'` → `True`
    
- **Identity Operators** (referenced but shown in conditional statements):
  - **is**: Checks if two variables refer to same object
  - **is not**: Checks if variables don't refer to same object

---

## 🔀 Control Flow & Functions

### **Day 12: Relational Operators** (Operators folder)
Compare values and make decisions based on comparisons (detailed in Day 10).

### **Day 13-16: Conditional Statements - if, elif, else** (Control statements folder)
Make decisions in code based on conditions:

**Topics Covered:**
- **if statement**: Execute code if condition is true
- **elif statement**: Multiple conditions check (else if)
- **else statement**: Execute if no previous condition is true
- **Nested if**: if statements inside if statements
- **Truth values**: 0 is False, any non-zero is True

### **Day 17-22: Looping Statements** (Looping statements folder)
Execute code repeatedly with while and for loops:

**Topics Covered:**
- **While Loop**: Repeat while condition is true
- **For Loop**: Iterate over sequences
- **Range Function**: Generate sequences for iteration
- **Loop Control**: Break, continue, pass statements

### **Day 23: Jumping Statements - break, continue, pass** (Jumping statements folder)
Control loop execution flow:

**Topics Covered:**
- **break**: Exit the loop immediately
- **continue**: Skip to next iteration
- **pass**: Placeholder, does nothing

### **Day 24-30: Functions** (Functions folder)
Create reusable code blocks:

**Topics Covered:**
- **Built-in String Methods**: upper(), lower(), strip(), split(), replace(), find(), startswith(), endswith(), format()
- **Built-in List Methods**: append(), extend(), insert(), remove(), pop(), clear(), index(), count(), sort(), reverse()
- **Built-in Tuple Methods**: count(), index()
- **Built-in Dictionary Methods**: keys(), values(), items(), get(), update(), pop(), clear()
- **Built-in Set Methods**: add(), remove(), discard(), union(), intersection(), difference()
- **Match-Case Statement**: Python 3.10+ pattern matching
- **User-Defined Functions**: Create custom functions with parameters and return values

---

## 📁 File Handling & Data Processing

### **Day 31: Variable Scope - Global, Local, Nested**
Understand variable accessibility in different scopes:

**Topics Covered:**
- **Global Variables**: Accessible throughout the entire program
  - Declared outside functions
  - Modified using `global` keyword inside functions
  - Accessed directly inside and outside functions
  
- **Local Variables**: Accessible only within the function
  - Declared inside functions
  - Cannot be accessed outside the function
  - Function parameters are local to that function
  
- **Nested Functions**: Functions defined inside other functions
  - Inner function can access outer function's variables
  - Using `nonlocal` keyword to modify outer function variables
  
- **Scope Resolution Order** (LEGB):
  - Local → Enclosing → Global → Built-in

---

### **Day 32: Text File Handling**
Read, write, and manipulate text files:

**Topics Covered:**
- **File Modes**:
  - `'w'` - Write: Create/overwrite file
  - `'r'` - Read: Open existing file for reading
  - `'a'` - Append: Add content to end of file
  - `'w+'` - Write and Read: Create file and read back
  - `'r+'` - Read and Write: Open file for both operations
  - `'a+'` - Append and Read: Add content and read
  - `'x'` - Create: Create new file only (error if exists)
  
- **File Operations**:
  - `file.read()` - Read entire file content
  - `file.write()` - Write content to file
  - `file.close()` - Close file (important for cleanup)
  - `file.seek()` - Move file pointer to position
  - Using `with` statement for automatic file closing
  
- **Best Practice**: Using `with` statement prevents file handle leaks

---

### **Day 33: CSV File Handling**
Work with Comma-Separated Values data files:

**Topics Covered:**
- **CSV Module**: Import `csv` module for CSV operations
- **csv.reader()**: Read CSV files row by row
- **csv.writer()**: Write data to CSV files
- **DictReader**: Read CSV as dictionaries with column names as keys
- **DictWriter**: Write dictionaries to CSV
- **Parsing CSV Data**: Convert rows to meaningful data structures
- **Employee Data Management**: Store and retrieve employee records

---

### **Day 34: Binary File Handling**
Work with binary data files using pickle module:

**Topics Covered:**
- **Binary Files**: Non-text data storage (images, compiled code, serialized objects)
- **Pickle Module**: Serialize and deserialize Python objects
  - `pickle.dump()` - Write Python object to binary file
  - `pickle.load()` - Read Python object from binary file
  
- **File Modes for Binary**:
  - `'wb'` - Write binary
  - `'rb'` - Read binary
  
- **Use Cases**: Store complex data structures (lists, dictionaries, objects) in files
- **Security Note**: Only unpickle data from trusted sources

---

## 🛡️ Error Handling & OOP

### **Day 35: Exception Handling - try, except, else, finally**
Handle errors gracefully and prevent program crashes:

**Topics Covered:**
- **Try-Except Block**: Basic exception handling
  - `try:` - Code that may raise exception
  - `except:` - Handle specific exceptions
  
- **Common Exceptions**:
  - `ZeroDivisionError` - Division by zero: `98/0`
  - `ValueError` - Invalid value: `int('abc')`
  - `TypeError` - Wrong type: `'string' + 5`
  - `IndexError` - Out of range: `list[999]`
  - `KeyError` - Missing dictionary key
  - `FileNotFoundError` - File doesn't exist
  
- **Multiple Except Blocks**: Handle different exceptions separately
  ```python
  try:
      num = int(input('Enter number:'))
  except ValueError:
      print('Invalid number')
  except TypeError:
      print('Wrong type')
  ```
  
- **Else Block**: Executes if no exception occurs
- **Finally Block**: Always executes (cleanup code)
  ```python
  try:
      file = open('data.txt', 'r')
  except FileNotFoundError:
      print('File not found')
  finally:
      file.close()  # Always runs
  ```

---

### **Day 36: Custom Exception Handling**
Create and raise custom exceptions:

**Topics Covered:**
- **Custom Exceptions**: Define your own exception classes
  - Inherit from `Exception` class
  - Raise with `raise` keyword
  - Useful for application-specific errors
  
- **User-Defined Exception Example**:
  ```python
  class InvalidAgeError(Exception):
      pass
  
  age = int(input('Enter age:'))
  if age < 0:
      raise InvalidAgeError('Age cannot be negative')
  ```

---

### **Day 37: Creating Classes and Objects**
Start object-oriented programming:

**Topics Covered:**
- **Class Definition**: Blueprint for objects
  ```python
  class Employee:
      company = 'Techcorp'  # Class variable
      
      def __init__(self, name, salary):
          self.name = name      # Instance variable
          self.salary = salary
  ```
  
- **Object Creation**: Instantiate class
  ```python
  emp1 = Employee('Smith', 98000)
  emp2 = Employee('John', 76000)
  ```
  
- **Class Variables**: Shared by all instances
  - Accessed via class name: `Employee.company`
  - Same value across all objects
  
- **Instance Variables**: Individual per object
  - Accessed via `self` keyword
  - Each object has its own copy
  - Different values per object
  
- **Accessing Variables**:
  - Instance: `emp1.name`, `emp1.salary`
  - Class: `Employee.company`

---

### **Day 38: Constructors - __init__() Method**
Initialize objects with default values:

**Topics Covered:**
- **Constructor Basics**: Special method called on object creation
  ```python
  def __init__(self, parameters):
      self.variable = parameter
  ```
  
- **Purpose**: Initialize instance variables automatically
- **self Parameter**: Refers to the object being created
- **Parameterized Constructor**: Pass values during object creation
  ```python
  emp = Employee('Smith', 98000)  # Values passed here
  ```

---

### **Day 39: Types of Constructors**
Different constructor patterns:

**Topics Covered:**
- **Default Constructor**: No parameters (except self)
  ```python
  def __init__(self):
      self.name = 'Default'
  ```
  
- **Parameterized Constructor**: Takes initialization parameters
  ```python
  def __init__(self, name, salary):
      self.name = name
      self.salary = salary
  ```
  
- **Constructor with Default Values**: Default parameter values
  ```python
  def __init__(self, name='Unknown', salary=0):
      self.name = name
      self.salary = salary
  ```

---

### **Day 40: Types of Variables in OOP**
Three categories of variables in object-oriented programming:

**Topics Covered:**
- **Instance Variables** (Object-level):
  - Declared in `__init__()` method using `self`
  - Unique to each object
  - Different value for each instance
  - Accessed via `object.variable`
  ```python
  self.name = name      # Instance variable
  self.salary = salary
  ```
  
- **Static Variables** (Class-level):
  - Declared inside class, outside methods
  - Shared by all instances
  - Same value across all objects
  - Accessed via `ClassName.variable`
  ```python
  company_name = 'Techcrop'  # Static variable
  Employee.company_name
  ```
  
- **Local Variables**:
  - Declared inside methods
  - Only accessible within that method
  - Scope limited to method execution
  ```python
  def calculate():
      temp = 100  # Local variable
  ```

---

## 📊 Repository Structure

**Days 1-9 Files (Fundamentals)**
- Day1(print,keyword).py - Print function and Python keywords
- Day2(creating-identifiers,variables,string formatting,commentline).py - Variables, identifiers, string formatting
- Day3(datatypes).py - Data types overview
- Day4(String datatype -indexing,slicing).py - String indexing and slicing
- Day5(List -indexing,slicing).py - List operations
- Day6(tuple-indexing,slicing).py - Tuple operations
- Day7(Set datatype,Dictionary datatype,Range).py - Sets, dictionaries, range
- Day8(Typecasting-implicit,explicit,datatypes).py - Type casting and conversions
- Day9(Input , eval Statements).py - Input and eval functions

**Days 31-40 Files (Advanced - Scoping, File Handling, OOP)**
- Day31(Scope_of_variables).py - Global, local, and nested variable scopes
- Day32(File handling).py - Text file operations
- Day33(CSV file handling).py - CSV file reading and writing
- Day34(Binary filehandling).py - Binary files and pickle module
- Day35(Exception handling).py - Try, except, else, finally blocks
- Day36(Custom exception handling).py - Creating custom exceptions
- Day37(Creating class and object).py - Classes and objects
- Day38(Constructor).py - Constructor methods
- Day39(Types of constuctor).py - Different constructor patterns
- Day40(types of oops variable).py - Instance, static, and local variables in OOP

**Folders**
- Operators/ - Day 10-12: Arithmetic, relational, and logical operators
- Control statements/ - Day 13-16: if, elif, else, and nested if statements
- Looping statements/ - Day 17-22: while and for loops
- Jumping statements/ - Day 23: break, continue, and pass statements
- Functions/ - Day 24-30: Built-in and user-defined functions
- Main/ - Main program files

**Data Files**
- emp1.csv - Employee data in CSV format
- emp2.csv - Employee data in CSV format
- main.csv - Main dataset in CSV format
- python.csv - Python course data in CSV format
- Students_data.csv - Student records in CSV format

**Text Files**
- python118.txt - Python course notes
- Pythonbatch.txt - Batch processing examples
- java.txt - Java reference
- students.txt - Student list

**Other Files**
- functions programming.ipynb - Jupyter notebook with interactive function examples
- data.bin - Binary file with pickled Python objects
- main.py - Main execution file
- README.md - This comprehensive guide

---

## 🚀 Getting Started

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd Python\ A118
   ```

2. **Run a Python file**:
   ```bash
   python Day1\(print,keyword\).py
   ```

3. **Run Jupyter notebook**:
   ```bash
   jupyter notebook functions\ programming.ipynb
   ```

---

## 💡 Key Learning Outcomes

By completing this course, you will understand:
- ✅ Python fundamentals (variables, data types, operators)
- ✅ Control flow (conditionals, loops, functions)
- ✅ File handling (text, CSV, binary files)
- ✅ Exception handling and error management
- ✅ Object-oriented programming basics (classes, objects, constructors)
- ✅ Variable scoping and memory management
- ✅ Python best practices and code organization

---

## 📝 Notes

- Each file contains practical examples and explanations
- Code is commented for easy understanding
- Start from Day 1 and progress sequentially for best learning
- Practice each concept before moving to the next
- Files in subfolders contain topic-specific implementations

---

## 👤 Author

Python A118 Learning Course - Structured Python Fundamentals

## 📄 License

Educational content for learning purposes.

---

**Last Updated**: May 2026
**Total Days Covered**: 40+ days
**Topics**: Fundamentals → OOP

---

## 🎯 Control Flow - Directing Program Execution

### **Day 12: Conditional Statements** (Control statements folder)
Make decisions in programs using if, elif, and else:

**Topics Covered:**
- **Simple if Statement**: Execute block only if condition is true
  - Format:
    ```python
    if condition:
        # code executes if condition is True
    ```
  - Example: Check if number is positive
    ```python
    num = 78
    if num > 0:
        print(f'{num} is a positive number')
    ```
  
- **Conditional Logic Examples**:
  - Find greatest of 2 numbers: `if a > b: print(f'{a} is greatest')`
  - Check if even: `if num % 2 == 0: print('even')`
  - Check if odd: `if num % 2 != 0: print('odd')`
  - Check divisibility: `if num % 3 == 0 and num % 5 == 0: print('divisible')`
  
- **String Checking**:
  - Check if starts with vowel: `if s1[0] in 'AEIOUaeiou': print('starts with vowel')`
  - Check if starts with consonant: `if s1[0] not in 'AEIOUaeiou': print('consonant')`
  - Check if starts with uppercase: `if 'A' <= s2[0] <= 'Z': print('uppercase')`
  
- **Data Type Checking**:
  - Single value types: `if type(data) in [int, float, complex, bool]: print('single value')`
  - Collection types: `if type(data) in [list, tuple, set, dict, str]: print('collection')`
  - String length: `if len(s1) > 5: print('>5 characters')`
  
- **Complex Conditional Operations**:
  - Convert to complex if divisible by 3 and 5: `if num % 3 == 0 and num % 5 == 0: print(complex(num))`
  - Store digits in list if even: `if num % 2 == 0: print(list(str(num)))`
  
- **Character Operations**:
  - Find next character: 
    ```python
    ch = 'A'
    if ch in 'AEIOUaeiou':
        next_ch = chr(ord(ch) + 1)
        print(next_ch)  # B
    ```
  - Find previous character:
    ```python
    ch = 'B'
    if ch not in 'AEIOUaeiou':
        prev_ch = chr(ord(ch) - 1)
        print(prev_ch)  # A
    ```

---

## 💡 Key Concepts Summary

✅ **Fundamentals** (Days 1-2): Print, keywords, identifiers, variables, string formatting  
✅ **Data Types** (Days 3-7): int, float, complex, bool, str, list, tuple, set, dict, range  
✅ **Type Conversion** (Day 8): Converting between different data types safely  
✅ **User Interaction** (Day 9): Taking input and evaluating expressions  
✅ **Operators** (Days 9-11): Arithmetic, relational, logical, membership, assignment  
✅ **Decision Making** (Day 12): Conditional statements with if  

---

## 🚀 Getting Started

```bash
# Navigate to the course directory
cd "Python A118"

# Run any day's lesson
python "Day1(print,keyword).py"
python "Day2(creating-identifiers,variables,string formatting,commentline).py"
# ... and so on
```


