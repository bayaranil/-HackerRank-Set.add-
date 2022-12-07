# -HackerRank-Set.add-

If we want to add a single element to an existing set, we can use the .add() operation.
It adds the element to the set and returns 'None'.


# EXAMPLE 
```ruby
s = set('HackerRank')
s.add('H')
print s
set(['a', 'c', 'e', 'H', 'k', 'n', 'r', 'R'])
print s.add('HackerRank')
None
print s
set(['a', 'c', 'e', 'HackerRank', 'H', 'k', 'n', 'r', 'R'])
```

# Task
Apply your knowledge of the .add() operation to help your friend Rupal.

Rupal has a huge collection of country stamps. She decided to count the total number of distinct country stamps in her collection. She asked for your help. You pick the stamps one by one from a stack of  country stamps

----------------------------------------------------------------------------------------------------------

# Sample Input
```
7
UK
China
USA
France
New Zealand
UK
France 
```

# Sample Output
```
> 5
```


# Codes
```ruby
country_Number = input()
my_Tuple = set()
i=0
counter =0
while i < int(country_Number):
  country_Names = input ()
  my_Tuple.add(country_Names)
  i+=1
for _ in my_Tuple:
  counter+=1
print (counter)
```
