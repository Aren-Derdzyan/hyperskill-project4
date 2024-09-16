import random
dict = {}
global_total = 0
try:
   n = int(input('Enter the number of friends joining (including you):\n'))
   if n < 1:
      print("No one is joining for the party")
      exit()
except Exception:
   print("No one is joining for the party")
   exit()
else:
   print("Enter the name of every friend (including you), each on a new line: ")
   for i in range(n):
      name = input()
      dict[name] = 0

   print("Enter the total bill value: ")
   total = int(input())
   global_total = total
   each = round(total/n, 2)
   for i in dict:
      dict[i] = each
name = ""
print('Do you want to use the "Who is lucky?" feature? Write Yes/No:')
answer = input()
if (answer == "Yes"):
   lucky = random.choice(list(dict))
   dict[lucky] = 0
   name = dict[lucky]
   print(f"{lucky} is the lucky one!")
else:
   print("No one is going to be lucky")
   print(dict)
   exit()
each = round(global_total/(n-1), 2)
for i in dict:
   if (dict[i] == name):
      continue
   dict[i] = each

print(dict)