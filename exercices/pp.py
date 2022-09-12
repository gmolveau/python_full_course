days = ["jeudi", "vendredi", "samedi", "dimanche", "lundi", "mardi", "mercredi",]

n = 0
for day in days:
    if day == "lundi":
        print(n)
    else:
        n = n + 1

for i in range(len(days)):
    if days[i] == "lundi":
        print(i)

for i, day in enumerate(days):
    if day == "lundi":
        print(i)

found = False
for i, day in enumerate(days):
    if day == "lundi":
        found = True
        break
if not found:
    print( -1)
print( i)

for i, day in enumerate(days):
    if day == "lundi":
        break
else: # seulement si ya pas de break
    print( -1)
print( i)

