# Python A118 - Daily Python Learning Journey 📚

An ongoing Python fundamentals learning repository where I practice and master Python concepts day by day. This course follows a structured progression from basic printing and keywords to advanced operators and control flow statements.

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


