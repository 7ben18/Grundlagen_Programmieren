"""
If you have three customers with the times: [4,3,2]
the first customer is going to wait 4 minutes for his
coffee, the second customer is going to wait 4 minutes
(the time needed for the first customer to get his coffee),
another 2 minutes (the time needed to clean the machine) and
3 more minutes (the time you need to brew his coffee), so in
total: 9 minutes. The third customer, by the same logic is about
to wait: 9minutes (for the first two customers)+2 more minutes(cleaning)+2
minutes (his coffee brewing time). This order of brewing the coffee
will end up in a total waiting time of: 26 minutes, but, note that,
this may not be the minimum time needed.
"""


def brew_coffee(coffee):
   coffee = sorted(coffee, reverse = False)
   clean_time = 2
   brew_time = 2

   waiting_time = 0
   for i in coffee:
      waiting_time += (i + clean_time + brew_time)
   return waiting_time

print(brew_coffee([4,3,2]))