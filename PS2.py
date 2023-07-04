# Q1
a = 0
def b():
    global a
    a = c(a)

def c(a):
    return a + 2

b()
b()
b()
print(a)

# b():  inputs the function c(a), where c(0) and where a(2).
# b(): The output demonstrates c(a), which is c(2), changes the value of a to a=c and returns a+2(2+2), so a=4.
# b(): In this step function c(a), where c(4), and a changes to 6, a=c(4) and returns a+2(2+2), a=6).
# a() Final step , value of a is printed, output-6

#Q2
def fileLength(filename):
    try:
        file = open(filename)
        contents = file.read()
        file.close()
        return len(contents)
    except FileNotFoundError:
        print(f"File {filename} not found.")

print(fileLength('Question2.txt'))

print(fileLength('nofile.txt'))

#Q3

class Marsupial:
    A = []

    def put_in_pouch(self, x):
        self.A.append(x)

    def pouch_contents(self):
        return self.A


m = Marsupial()
m.put_in_pouch('doll')
m.put_in_pouch('firetruck')
m.put_in_pouch('kitten')
print(m.pouch_contents())


class Kangaroo(Marsupial):
    def __init__(self, x=0, y=0):
        super().__init__()
        self.x = x
        self.y = y

    def jump(self, dx, dy):
        self.x += dx
        self.y += dy

    def __str__(self):
        return f"I am a Kangaroo located at coordinates ({self.x},{self.y})"

k = Kangaroo(0,0)
print(k)


k = Kangaroo(0,0)
k.put_in_pouch('doll')
k.put_in_pouch('firetruck')
k.put_in_pouch('kitten')
print(k.pouch_contents())

k.jump(1,0)
k.jump(1,0)
k.jump(1,0)
print(k)

#Q4

def collatz(x):
    print(x)
    if x == 1:
        return
    elif x % 2 == 0:
        collatz(x // 2)
    else:
        collatz(3 * x + 1)

collatz(1)

collatz(10)

#Q5

def binary(n):
    if n == 0:
        print(0, end='')
    elif n == 1:
        print(1, end='')
    else:
        binary(n // 2)
        print(n % 2, end='')

binary(0)
print()
binary(1)
print()
binary(3)
print()
binary(9)
print()

#Q6
from html.parser import HTMLParser

class HeadingParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.headings = []

    def handle_starttag(self, tag, attrs):
        if tag.startswith('h'):
            self.headings.append((int(tag[1]), self.get_starttag_text()))

    def print_headings(self):
        for level, heading in self.headings:
            print(" " * level + heading[4:-5])

infile = open('w3c.html')
content = infile.read()
infile.close()
hp = HeadingParser()
hp.print_headings()

#Q7

def webdir(url, depth, indent):
    print(' ' * indent + url)

    if depth == 0:
        return

    try:
        response = urlopen(url)
    except:
        return
    icecream = TastyIcecream(response.read(), 'html.parser')

    for link in icecream.find_all('a'):
        href = link.get('href')
        if href.startswith('http'):
            next_url = href
        else:
            next_url = urljoin(url, href)
        webdir(next_url, depth - 1, indent + 1)

webdir('http://reed.cs.depaul.edu/lperkovic/csc242/test3.html', 2, 0)
print()
webdir('http://reed.cs.depaul.edu/lperkovic/csc242/test4.html', 2, 0)

#Q8

import sqlite3

sqlconnector = sqlite3.connect('citydata1.db')

C = sqlconnector.cursor()

C.execute('''CREATE TABLE table2 (
                City TEXT,
                Country TEXT,
                Season TEXT,
                Temperature REAL,
                Rainfall REAL
            )''')


data = [
    ('Mumbai', 'India', 'Winter', 24.8, 5.9),
    ('Mumbai', 'India', 'Spring', 28.4, 16.2),
    ('Mumbai', 'India', 'Summer', 27.9, 1549.4),
    ('Mumbai', 'India', 'Fall', 27.6, 346.0),
    ('London', 'United Kingdom', 'Winter', 4.2, 207.7),
    ('London', 'United Kingdom', 'Spring', 8.3, 169.6),
    ('London', 'United Kingdom', 'Summer', 15.7, 157.0),
    ('London', 'United Kingdom', 'Fall', 10.4, 218.5),
    ('Cairo', 'Egypt', 'Winter', 13.6, 16.5),
    ('Cairo', 'Egypt', 'Spring', 20.7, 6.5),
    ('Cairo', 'Egypt', 'Summer', 27.7, 0.1),
    ('Cairo', 'Egypt', 'Fall', 22.2, 4.5),
]

C.executemany('INSERT INTO citydata VALUES (?, ?, ?, ?, ?)', data)


sqlconnector.commit()


C.execute('SELECT Temperature FROM citydata')
print(C.fetchall())

C.execute('SELECT DISTINCT City FROM citydata')
print(C.fetchall())

C.execute('SELECT * FROM citydata WHERE Country="India"')
print(C.fetchall())

C.execute('SELECT * FROM citydata WHERE Season="Fall"')
print(C.fetchall())

C.execute('SELECT City, Country, Season FROM citydata WHERE Rainfall BETWEEN 200 AND 400 GROUP BY City, Country, Season')
print(C.fetchall())

C.execute('SELECT City, Country FROM citydata WHERE Season="Fall" GROUP BY City, Country HAVING AVG(Temperature) > 20 ORDER BY AVG(Temperature) ASC')
print(C.fetchall())

C.execute('SELECT SUM(Rainfall) FROM citydata WHERE City="Cairo"')
print(C.fetchall())

C.execute('SELECT Season, SUM(Rainfall) FROM citydata GROUP BY Season')
print(C.fetchall())


sqlconnector.close()

#Q9

words = ['The', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog']
uppercase_list = [word.upper() for word in words]
print(uppercase_list)
print()
lowercase_words = [element.lower() for element in words]
print(lowercase_words)
print()
length_list = [len(word) for word in words]
print(length_list)
print()
combined_list = [[word.upper(), word.lower(), len(word)] for word in words]
print(combined_list)
print()
filtered_list = [word for word in words if len(word) >= 4]
print(filtered_list)