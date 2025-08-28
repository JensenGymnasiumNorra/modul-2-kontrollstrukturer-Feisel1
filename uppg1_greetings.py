"""
Låt användaren mata in sitt namn och ålder. 
Välkomna användaren till programmet och skriv ut ett meddelande baserat på dens ålder.
Det ska finnas minst 3 olika meddelanden som kan skrivas ut baserat på åldern.

Exempel på utskrift, det inom () ska ändras om variablerna ändras:
Hej (Ulrika)!
Oj vad du är gammal.
"""

namn = input("vad heter du? ")
ålder = int(input("hur gammal är du? "))
if ålder <=19:
    print(f"Hej {namn}! Oj vad du är ung, du får inte komma in i hemsidan.")
elif 20 <= ålder <= 50:
    print(f"Hej {namn}! Välkommen till hemsidan.")
else:
    print(f"Hej {namn}! Oj vad du är gammal, men du är fortfarande välkomen.")