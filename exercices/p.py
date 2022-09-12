days = ["lundi", "mardi", "mercredi", "jeudi", "vendredi", "samedi", "dimanche"]

for day in days:
    if day == "lundi" or day == "mardi" or day == "mercredi" or day == "jeudi":
        print("travail")
    elif day == "vendredi":
        print("soon w-e")
    else:
        print("BBQ")

for day in days:
    if day in ["lundi", "mardi", "mercredi", "jeudi"]:
        print("travail")
    elif day in ["samedi", "dimanche"]:
        print("BBQ")
    else:
        print("soon -we")

# pour chaque jour dans jours:
#     si jour est lundi ou mardi ou mercredi ou jeudi
#         imprimer travail
#     si jour est vendredi
#         imprimer soon w-e
#     si jour est samedi ou dimamche
#         imprimer BBQ