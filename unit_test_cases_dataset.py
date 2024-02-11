data = [

    {
        "topic":"Python Regular Expression",
        "summary": """
Python RegEx
A RegEx, or Regular Expression, is a sequence of characters that forms a search pattern.

RegEx can be used to check if a string contains the specified search pattern.

RegEx Module
Python has a built-in package called re, which can be used to work with Regular Expressions.

Import the re module:

import re
RegEx in Python
When you have imported the re module, you can start using regular expressions:

ExampleGet your own Python Server
Search the string to see if it starts with "The" and ends with "Spain":

import re

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)
RegEx Functions
The re module offers a set of functions that allows us to search a string for a match:

Function	Description
findall	Returns a list containing all matches
search	Returns a Match object if there is a match anywhere in the string
split	Returns a list where the string has been split at each match
sub	Replaces one or many matches with a string
Metacharacters
Metacharacters are characters with a special meaning:

Character	Description	Example	Try it
[]	A set of characters	"[a-m]"	
\	Signals a special sequence (can also be used to escape special characters)	"\d"	
.	Any character (except newline character)	"he..o"	
^	Starts with	"^hello"	
$	Ends with	"planet$"	
*	Zero or more occurrences	"he.*o"	
+	One or more occurrences	"he.+o"	
?	Zero or one occurrences	"he.?o"	
{}	Exactly the specified number of occurrences	"he.{2}o"	
|	Either or	"falls|stays"	
()	Capture and group	 	 
Special Sequences
A special sequence is a \ followed by one of the characters in the list below, and has a special meaning:

Character	Description	Example	Try it
\A	Returns a match if the specified characters are at the beginning of the string	"\AThe"	
\b	Returns a match where the specified characters are at the beginning or at the end of a word
(the "r" in the beginning is making sure that the string is being treated as a "raw string")	r"\bain"

r"ain\b"	

\B	Returns a match where the specified characters are present, but NOT at the beginning (or at the end) of a word
(the "r" in the beginning is making sure that the string is being treated as a "raw string")	r"\Bain"

r"ain\B"	

\d	Returns a match where the string contains digits (numbers from 0-9)	"\d"	
\D	Returns a match where the string DOES NOT contain digits	"\D"	
\s	Returns a match where the string contains a white space character	"\s"	
\S	Returns a match where the string DOES NOT contain a white space character	"\S"	
\w	Returns a match where the string contains any word characters (characters from a to Z, digits from 0-9, and the underscore _ character)	"\w"	
\W	Returns a match where the string DOES NOT contain any word characters	"\W"	
\Z	Returns a match if the specified characters are at the end of the string	"Spain\Z"	
Sets
A set is a set of characters inside a pair of square brackets [] with a special meaning:

Set	Description	Try it
[arn]	Returns a match where one of the specified characters (a, r, or n) is present	
[a-n]	Returns a match for any lower case character, alphabetically between a and n	
[^arn]	Returns a match for any character EXCEPT a, r, and n	
[0123]	Returns a match where any of the specified digits (0, 1, 2, or 3) are present	
[0-9]	Returns a match for any digit between 0 and 9	
[0-5][0-9]	Returns a match for any two-digit numbers from 00 and 59	
[a-zA-Z]	Returns a match for any character alphabetically between a and z, lower case OR upper case	
[+]	In sets, +, *, ., |, (), $,{} has no special meaning, so [+] means: return a match for any + character in the string	
 
The findall() Function
The findall() function returns a list containing all matches.

Example
Print a list of all matches:

import re

txt = "The rain in Spain"
x = re.findall("ai", txt)
print(x)
The list contains the matches in the order they are found.

If no matches are found, an empty list is returned:

Example
Return an empty list if no match was found:

import re

txt = "The rain in Spain"
x = re.findall("Portugal", txt)
print(x)
 
The search() Function
The search() function searches the string for a match, and returns a Match object if there is a match.

If there is more than one match, only the first occurrence of the match will be returned:

Example
Search for the first white-space character in the string:

import re

txt = "The rain in Spain"
x = re.search("\s", txt)

print("The first white-space character is located in position:", x.start())
If no matches are found, the value None is returned:

Example
Make a search that returns no match:

import re

txt = "The rain in Spain"
x = re.search("Portugal", txt)
print(x)
 
The split() Function
The split() function returns a list where the string has been split at each match:

Example
Split at each white-space character:

import re

txt = "The rain in Spain"
x = re.split("\s", txt)
print(x)
You can control the number of occurrences by specifying the maxsplit parameter:

Example
Split the string only at the first occurrence:

import re

txt = "The rain in Spain"
x = re.split("\s", txt, 1)
print(x)
 
The sub() Function
The sub() function replaces the matches with the text of your choice:

Example
Replace every white-space character with the number 9:

import re

txt = "The rain in Spain"
x = re.sub("\s", "9", txt)
print(x)
You can control the number of replacements by specifying the count parameter:

Example
Replace the first 2 occurrences:

import re

txt = "The rain in Spain"
x = re.sub("\s", "9", txt, 2)
print(x)
 
Match Object
A Match Object is an object containing information about the search and the result.

Note: If there is no match, the value None will be returned, instead of the Match Object.

Example
Do a search that will return a Match Object:

import re

txt = "The rain in Spain"
x = re.search("ai", txt)
print(x) #this will print an object
The Match object has properties and methods used to retrieve information about the search, and the result:

.span() returns a tuple containing the start-, and end positions of the match.
.string returns the string passed into the function
.group() returns the part of the string where there was a match
Example
Print the position (start- and end-position) of the first match occurrence.

The regular expression looks for any words that starts with an upper case "S":

import re

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.span())
Example
Print the string passed into the function:

import re

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.string)
Example
Print the part of the string where there was a match.

The regular expression looks for any words that starts with an upper case "S":

import re

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.group())"""
    },

    {
        "topic":"Python Classes and Objects",
        "summary": """
Python Classes and Objects
Python Classes/Objects
Python is an object oriented programming language.

Almost everything in Python is an object, with its properties and methods.

A Class is like an object constructor, or a "blueprint" for creating objects.

Create a Class
To create a class, use the keyword class:

ExampleGet your own Python Server
Create a class named MyClass, with a property named x:

class MyClass:
  x = 5
Create Object
Now we can use the class named MyClass to create objects:

Example
Create an object named p1, and print the value of x:

p1 = MyClass()
print(p1.x)
The __init__() Function
The examples above are classes and objects in their simplest form, and are not really useful in real life applications.

To understand the meaning of classes we have to understand the built-in __init__() function.

All classes have a function called __init__(), which is always executed when the class is being initiated.

Use the __init__() function to assign values to object properties, or other operations that are necessary to do when the object is being created:

Example
Create a class named Person, use the __init__() function to assign values for name and age:

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1.name)
print(p1.age)
Note: The __init__() function is called automatically every time the class is being used to create a new object.

The __str__() Function
The __str__() function controls what should be returned when the class object is represented as a string.

If the __str__() function is not set, the string representation of the object is returned:

Example
The string representation of an object WITHOUT the __str__() function:

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1)
Example
The string representation of an object WITH the __str__() function:

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def __str__(self):
    return f"{self.name}({self.age})"

p1 = Person("John", 36)

print(p1)
Object Methods
Objects can also contain methods. Methods in objects are functions that belong to the object.

Let us create a method in the Person class:

Example
Insert a function that prints a greeting, and execute it on the p1 object:

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)
p1.myfunc()
Note: The self parameter is a reference to the current instance of the class, and is used to access variables that belong to the class.

The self Parameter
The self parameter is a reference to the current instance of the class, and is used to access variables that belongs to the class.

It does not have to be named self , you can call it whatever you like, but it has to be the first parameter of any function in the class:

Example
Use the words mysillyobject and abc instead of self:

class Person:
  def __init__(mysillyobject, name, age):
    mysillyobject.name = name
    mysillyobject.age = age

  def myfunc(abc):
    print("Hello my name is " + abc.name)

p1 = Person("John", 36)
p1.myfunc()
Modify Object Properties
You can modify properties on objects like this:

Example
Set the age of p1 to 40:

p1.age = 40
Delete Object Properties
You can delete properties on objects by using the del keyword:

Example
Delete the age property from the p1 object:

del p1.age
Delete Objects
You can delete objects by using the del keyword:

Example
Delete the p1 object:

del p1
The pass Statement
class definitions cannot be empty, but if you for some reason have a class definition with no content, put in the pass statement to avoid getting an error.

Example
class Person:
  pass"""
    },

    {
        "topic":"Python JSON",
        "summary": """
Python JSON
JSON is a syntax for storing and exchanging data.

JSON is text, written with JavaScript object notation.

JSON in Python
Python has a built-in package called json, which can be used to work with JSON data.

ExampleGet your own Python Server
Import the json module:

import json
Parse JSON - Convert from JSON to Python
If you have a JSON string, you can parse it by using the json.loads() method.

The result will be a Python dictionary.

Example
Convert from JSON to Python:

import json

# some JSON:
x =  '{ "name":"John", "age":30, "city":"New York"}'

# parse x:
y = json.loads(x)

# the result is a Python dictionary:
print(y["age"])
Convert from Python to JSON
If you have a Python object, you can convert it into a JSON string by using the json.dumps() method.

Example
Convert from Python to JSON:

import json

# a Python object (dict):
x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

# convert into JSON:
y = json.dumps(x)

# the result is a JSON string:
print(y)
You can convert Python objects of the following types, into JSON strings:

dict
list
tuple
string
int
float
True
False
None
Example
Convert Python objects into JSON strings, and print the values:

import json

print(json.dumps({"name": "John", "age": 30}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))
When you convert from Python to JSON, Python objects are converted into the JSON (JavaScript) equivalent:

Python	JSON
dict	Object
list	Array
tuple	Array
str	String
int	Number
float	Number
True	true
False	false
None	null
Example
Convert a Python object containing all the legal data types:

import json

x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

print(json.dumps(x))
Format the Result
The example above prints a JSON string, but it is not very easy to read, with no indentations and line breaks.

The json.dumps() method has parameters to make it easier to read the result:

Example
Use the indent parameter to define the numbers of indents:

json.dumps(x, indent=4)
You can also define the separators, default value is (", ", ": "), which means using a comma and a space to separate each object, and a colon and a space to separate keys from values:

Example
Use the separators parameter to change the default separator:

json.dumps(x, indent=4, separators=(". ", " = "))
Order the Result
The json.dumps() method has parameters to order the keys in the result:

Example
Use the sort_keys parameter to specify if the result should be sorted or not:

json.dumps(x, indent=4, sort_keys=True)"""
    },

    {
        "topic":"JavaScript Regular Expressions",
        "summary": """
JavaScript Regular Expressions
A regular expression is a sequence of characters that forms a search pattern.

The search pattern can be used for text search and text replace operations.

What Is a Regular Expression?
A regular expression is a sequence of characters that forms a search pattern.

When you search for data in a text, you can use this search pattern to describe what you are searching for.

A regular expression can be a single character, or a more complicated pattern.

Regular expressions can be used to perform all types of text search and text replace operations.

Syntax
/pattern/modifiers;
Example
/w3schools/i;
Example explained:

/w3schools/i  is a regular expression.

w3schools  is a pattern (to be used in a search).

i  is a modifier (modifies the search to be case-insensitive).

Using String Methods
In JavaScript, regular expressions are often used with the two string methods: search() and replace().

The search() method uses an expression to search for a match, and returns the position of the match.

The replace() method returns a modified string where the pattern is replaced.

Using String search() With a String
The search() method searches a string for a specified value and returns the position of the match:

Example
Use a string to do a search for "W3schools" in a string:

let text = "Visit W3Schools!";
let n = text.search("W3Schools");
The result in n will be:

6

Using String search() With a Regular Expression
Example
Use a regular expression to do a case-insensitive search for "w3schools" in a string:

let text = "Visit W3Schools";
let n = text.search(/w3schools/i);
The result in n will be:

6

Using String replace() With a String
The replace() method replaces a specified value with another value in a string:

let text = "Visit Microsoft!";
let result = text.replace("Microsoft", "W3Schools");
Use String replace() With a Regular Expression
Example
Use a case insensitive regular expression to replace Microsoft with W3Schools in a string:

let text = "Visit Microsoft!";
let result = text.replace(/microsoft/i, "W3Schools");
The result in res will be:

Visit W3Schools!
Did You Notice?
Regular expression arguments (instead of string arguments) can be used in the methods above.
Regular expressions can make your search much more powerful (case insensitive for example).

Regular Expression Modifiers
Modifiers can be used to perform case-insensitive more global searches:

Modifier	Description	Try it
i	Perform case-insensitive matching	
g	Perform a global match (find all)	
m	Perform multiline matching	
d	Perform start and end matching (New in ES2022)	
Regular Expression Patterns
Brackets are used to find a range of characters:

Expression	Description	Try it
[abc]	Find any of the characters between the brackets	
[0-9]	Find any of the digits between the brackets	
(x|y)	Find any of the alternatives separated with |	
Metacharacters are characters with a special meaning:

Metacharacter	Description	Try it
\d	Find a digit	
\s	Find a whitespace character	
b	Find a match at the beginning of a word like this: bWORD, or at the end of a word like this: WORD b	
uxxxx	Find the Unicode character specified by the hexadecimal number xxxx	
Quantifiers define quantities:

Quantifier	Description	Try it
n+	Matches any string that contains at least one n
n*	Matches any string that contains zero or more occurrences of n
n?	Matches any string that contains zero or one occurrences of n
Using the RegExp Object
In JavaScript, the RegExp object is a regular expression object with predefined properties and methods.

Using test()
The test() method is a RegExp expression method.

It searches a string for a pattern, and returns true or false, depending on the result.

The following example searches a string for the character "e":

Example
const pattern = /e/;
pattern.test("The best things in life are free!");
Since there is an "e" in the string, the output of the code above will be:

true

You don't have to put the regular expression in a variable first. The two lines above can be shortened to one:

/e/.test("The best things in life are free!");
Using exec()
The exec() method is a RegExp expression method.

It searches a string for a specified pattern, and returns the found text as an object.

If no match is found, it returns an empty (null) object.

The following example searches a string for the character "e":

Example
/e/.exec("The best things in life are free!");
"""
    },
    {
        "topic":"JavaScript Bitwise Operations",
        "summary": """
JavaScript Bitwise Operations
JavaScript Bitwise Operators
Operator	Name	Description
&	AND	Sets each bit to 1 if both bits are 1
|	OR	Sets each bit to 1 if one of two bits is 1
^	XOR	Sets each bit to 1 if only one of two bits is 1
~	NOT	Inverts all the bits
<<	Zero fill left shift	Shifts left by pushing zeros in from the right and let the leftmost bits fall off
>>	Signed right shift	Shifts right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off
>>>	Zero fill right shift	Shifts right by pushing zeros in from the left, and let the rightmost bits fall off
Examples
Operation	Result	Same as	Result
5 & 1	1	0101 & 0001	 0001
5 | 1	5	0101 | 0001	 0101
~ 5	10	 ~0101	 1010
5 << 1	10	0101 << 1	 1010
5 ^ 1	4	0101 ^ 0001	 0100
5 >> 1	2	0101 >> 1	 0010
5 >>> 1	2	0101 >>> 1	 0010
JavaScript Uses 32 bits Bitwise Operands
JavaScript stores numbers as 64 bits floating point numbers, but all bitwise operations are performed on 32 bits binary numbers.

Before a bitwise operation is performed, JavaScript converts numbers to 32 bits signed integers.

After the bitwise operation is performed, the result is converted back to 64 bits JavaScript numbers.

The examples above uses 4 bits unsigned binary numbers. Because of this ~ 5 returns 10.

Since JavaScript uses 32 bits signed integers, it will not return 10. It will return -6.

00000000000000000000000000000101 (5)

11111111111111111111111111111010 (~5 = -6)

A signed integer uses the leftmost bit as the minus sign.

JavaScript Bitwise AND
When a bitwise AND is performed on a pair of bits, it returns 1 if both bits are 1.

One bit example:
Operation	Result
0 & 0	0
0 & 1	0
1 & 0	0
1 & 1	1
4 bits example:
Operation	Result
1111 & 0000	0000
1111 & 0001	0001
1111 & 0010	0010
1111 & 0100	0100
JavaScript Bitwise OR
When a bitwise OR is performed on a pair of bits, it returns 1 if one of the bits is 1:

One bit example:
Operation	Result
0 | 0	0
0 | 1	1 
1 | 0	1
1 | 1	1
4 bits example:
Operation	Result
1111 | 0000	1111
1111 | 0001	1111
1111 | 0010	1111
1111 | 0100	1111
JavaScript Bitwise XOR
When a bitwise XOR is performed on a pair of bits, it returns 1 if the bits are different:

One bit example:
Operation	Result
0 ^ 0	0
0 ^ 1	1 
1 ^ 0	1
1 ^ 1	0 
4 bits example:
Operation	Result
1111 ^ 0000	1111
1111 ^ 0001	1110
1111 ^ 0010	1101
1111 ^ 0100	1011
JavaScript Bitwise AND (&)
Bitwise AND returns 1 only if both bits are 1:

Decimal	Binary
5	00000000000000000000000000000101
1	00000000000000000000000000000001
5 & 1	00000000000000000000000000000001 (1)
Example
let x = 5 & 1;
JavaScript Bitwise OR (|)
Bitwise OR returns 1 if one of the bits is 1:

Decimal	Binary
5	00000000000000000000000000000101
1	00000000000000000000000000000001
5 | 1	00000000000000000000000000000101 (5)
Example
let x = 5 | 1;
JavaScript Bitwise XOR (^)
Bitwise XOR returns 1 if the bits are different:

Decimal	Binary
5	00000000000000000000000000000101
1	00000000000000000000000000000001
5 ^ 1	00000000000000000000000000000100 (4)
Example
let x = 5 ^ 1;
JavaScript Bitwise NOT (~)
Decimal	Binary
5	00000000000000000000000000000101
~5	11111111111111111111111111111010 (-6)
Example
let x = ~5;
JavaScript (Zero Fill) Bitwise Left Shift (<<)
This is a zero fill left shift. One or more zero bits are pushed in from the right, and the leftmost bits fall off:

Decimal	Binary
5	00000000000000000000000000000101
5 << 1	00000000000000000000000000001010 (10)
Example
let x = 5 << 1;
JavaScript (Sign Preserving) Bitwise Right Shift (>>)
This is a sign preserving right shift. Copies of the leftmost bit are pushed in from the left, and the rightmost bits fall off:

Decimal	Binary
-5	11111111111111111111111111111011
-5 >> 1	11111111111111111111111111111101 (-3)
Example
let x = -5 >> 1;
JavaScript (Zero Fill) Right Shift (>>>)
This is a zero fill right shift. One or more zero bits are pushed in from the left, and the rightmost bits fall off:

Decimal	Binary
5	00000000000000000000000000000101
5 >>> 1	00000000000000000000000000000010 (2)
Example
let x = 5 >>> 1;
Binary Numbers
Binary numbers with only one bit set are easy to understand:

Binary Representation	Decimal value
00000000000000000000000000000001	1
00000000000000000000000000000010	2
00000000000000000000000000000100	4
00000000000000000000000000001000	8
00000000000000000000000000010000	16
00000000000000000000000000100000	32
00000000000000000000000001000000	64
Setting a few more bits reveals the binary pattern:

Binary Representation	Decimal value
00000000000000000000000000000101	5 (4 + 1)
00000000000000000000000000001101	13 (8 + 4 + 1)
00000000000000000000000000101101	45 (32 + 8 + 4 + 1)
JavaScript binary numbers are stored in two's complement format.

This means that a negative number is the bitwise NOT of the number plus 1:

Binary Representation	Decimal value
00000000000000000000000000000101	5
11111111111111111111111111111011	-5
00000000000000000000000000000110	6
11111111111111111111111111111010	-6
00000000000000000000000000101000	40
11111111111111111111111111011000	-40
Joke:
There are only 10 types of people in the world: those who understand binary and those who don't.

Converting Decimal to Binary
Example
function dec2bin(dec){
  return (dec >>> 0).toString(2);
}
Converting Binary to Decimal
Example
function bin2dec(bin){
  return parseInt(bin, 2).toString(10);
}"""
    },
    {
        "topic":"JavaScript Classes",
        "summary": """
JavaScript Classes
ECMAScript 2015, also known as ES6, introduced JavaScript Classes.

JavaScript Classes are templates for JavaScript Objects.

JavaScript Class Syntax
Use the keyword class to create a class.

Always add a method named constructor():

Syntax
class ClassName {
  constructor() { ... }
}
Example
class Car {
  constructor(name, year) {
    this.name = name;
    this.year = year;
  }
}
The example above creates a class named "Car".

The class has two initial properties: "name" and "year".

A JavaScript class is not an object.

It is a template for JavaScript objects.

Using a Class
When you have a class, you can use the class to create objects:

Example
const myCar1 = new Car("Ford", 2014);
const myCar2 = new Car("Audi", 2019);

The example above uses the Car class to create two Car objects.

The constructor method is called automatically when a new object is created.

The Constructor Method
The constructor method is a special method:

It has to have the exact name "constructor"
It is executed automatically when a new object is created
It is used to initialize object properties
If you do not define a constructor method, JavaScript will add an empty constructor method.

Class Methods
Class methods are created with the same syntax as object methods.

Use the keyword class to create a class.

Always add a constructor() method.

Then add any number of methods.

Syntax
class ClassName {
  constructor() { ... }
  method_1() { ... }
  method_2() { ... }
  method_3() { ... }
}
Create a Class method named "age", that returns the Car age:

Example
class Car {
  constructor(name, year) {
    this.name = name;
    this.year = year;
  }
  age() {
    const date = new Date();
    return date.getFullYear() - this.year;
  }
}

const myCar = new Car("Ford", 2014);
document.getElementById("demo").innerHTML =
"My car is " + myCar.age() + " years old.";

You can send parameters to Class methods:

Example
class Car {
  constructor(name, year) {
    this.name = name;
    this.year = year;
  }
  age(x) {
    return x - this.year;
  }
}

const date = new Date();
let year = date.getFullYear();

const myCar = new Car("Ford", 2014);
document.getElementById("demo").innerHTML=
"My car is " + myCar.age(year) + " years old.";

Browser Support
The following table defines the first browser version with full support for Classes in JavaScript:

Chrome 49	Edge 12	Firefox 45	Safari 9	Opera 36
Mar, 2016	Jul, 2015	Mar, 2016	Oct, 2015	Mar, 2016

"""
    },

]
