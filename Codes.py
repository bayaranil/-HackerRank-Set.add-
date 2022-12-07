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
