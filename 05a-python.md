# Learn Python

Read Allen Downey's [Think Python](http://www.greenteapress.com/thinkpython/) for getting up to speed with Python 2.7 and computer science topics. It's completely available online, or you can buy a physical copy if you would like.

<a href="http://www.greenteapress.com/thinkpython/"><img src="img/think_python.png" style="width: 100px;" target="_blank"></a>

For quick and easy interactive practice with Python, many people enjoy [Codecademy's Python track](http://www.codecademy.com/en/tracks/python). There's also [Learn Python The Hard Way](http://learnpythonthehardway.org/book/) and [The Python Tutorial](https://docs.python.org/2/tutorial/).

---

###Q1. Lists &amp; Tuples

How are Python lists and tuples similar and different? Which will work as keys in dictionaries? Why?

Tuples are immutable (the values cannot be changed or added after initial assignment), while lists are mutable. Only immutable elements can be used as dictionary keys.
Dicts and sets must use a hash for efficient lookup in a hash table, because changing the hash will mess up the data structures and cause the dict or set to fail

---

###Q2. Lists &amp; Sets

How are Python lists and sets similar and different? Give examples of using both. How does performance compare between lists and sets for finding an element. Why?

Both set and list are similar for storing a sequence of items.
A list is for an ordered collection of items and a set is for an unordered set of items which are not duplicated.

Sets are implemented using hash tables. Whenever you add an object to a set, the position within the memory of the set object is determined using the hash of the object to be added. When testing for membership, all that needs to be done is basically to look if the object is at the position determined by its hash, so the speed of this operation does not depend on the size of the set. For lists, in contrast, the whole list needs to be searched, which will become slower as the list grows.

---

###Q3. Lambda Function

Describe Python's `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`.

Lamda function is anonymous functions (i.e. functions that are not bound to a name) at runtime used for some simple operations. 

>>> sorted(["hello", "world", "i", "am", "Computer"], key=lambda x: x.lower())
This sorts out the words in the list according to alphabetical order irrespective of the letter case. 

---

###Q4. List Comprehension, Map &amp; Filter

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.

List comprehensions are a tool for transforming one list into another list. During this transformation, elements can be conditionally included in the new list and each element can be transformed as needed.
>>> map(lambda x,y:x*y, [1,2,3],[4,5,6])
map() will apply its lambda function to the elements of the argument lists

>>> filter(lambda x: x>=2, [1,2,3])
filter will apply its lambda functions to each element of the list and return a list only if each element is True

Set comprehension
>>> s = { x for x in range(10) }

Dictionary comprehension
>>> dict([(i, i*i) for i in range(4)])


---

###Complete the following problems by editing the files below:

###Q5. Datetime
Use Python to compute days between start and stop date.   
a.  

```
date_start = '01-02-2013'    
date_stop = '07-28-2015'
```

import datetime
start = datetime.datetime.strptime(date_start, '%m-%d-%Y')
end  = datetime.datetime.strptime(date_stop, '%m-%d-%Y')
delta = end - start
print delta.days

b.  
```
date_start = '12312013'  
date_stop = '05282015'  
```

import datetime
start = datetime.datetime.strptime(date_start, '%m%d%Y')
end  = datetime.datetime.strptime(date_stop, '%m%d%Y')
delta = end - start
print delta.days

c.  
```
date_start = '15-Jan-1994'      
date_stop = '14-Jul-2015'  
```

import datetime
start = datetime.datetime.strptime(date_start, '%d-%b-%Y')
end  = datetime.datetime.strptime(date_stop, '%d-%b-%Y')
delta = end - start
print delta.days

Place code in this file: [q5_datetime.py](python/q5_datetime.py)

---

###Q6. Strings
Edit the 7 functions in [q6_strings.py](python/q6_strings.py)

---

###Q7. Lists
Edit the 5 functions in [q7_lists.py](python/q7_lists.py)

---

###Q8. Parsing
Edit the 3 functions in [q8_parsing.py](python/q8_parsing.py)





