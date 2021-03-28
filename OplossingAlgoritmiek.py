#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Opdracht:
Beantwoord onderstaande vragen en werk onderstaande functies uit.
Voeg commentaar toe om je code toe te lichten.
Je kunt je functies testen met het gegeven raamwerk door het bestand
uit te voeren (of met behulp van pytest, als je weet hoe dat werkt).
Lever je werk in op Canvas als alle tests slagen.
Let op! Het is niet toegestaan om bestaande modules te importeren en te
        gebruiken, zoals `math` en `statistics`.
"""

# Vul hier je naam, klas en studentnummer in
naam = "Achraf"
klas = "A"
studentnummer = 0

"""
1.  Sorteeralgoritme
    Hieronder staat de pseudocode van een sorteeralgoritme:
    1. Startend vanaf het begin van een lijst, vergelijk elk element met zijn volgende buur.
    2. Als het element groter is dan zijn volgende buur, verwissel ze van plaats.
    3. Doorloop zo de lijst tot het eind.
    4. Als er verwisselingen zijn geweest bij stap 2., ga naar stap 1.
    1a. Handmatig toepassen
        Gegeven is de lijst l = [ 4, 3, 1, 2 ]. Geef de waardes die deze
        lijst aanneemt bij álle tussenstappen bij toepassing van
        bovenstaand sorteeralgoritme.

        [4, 3, 1, 2]
        [3, 4, 1, 2]
        [3, 1, 4, 2]
        [3, 1, 2, 4]
        [1, 3, 2, 4]
        [1, 2, 3, 4]
        [1, 2, 3, 4]
        [1, 2, 3, 4]
        [1, 2, 3, 4]
        

    1b. Implementatie
        Implementeer het sorteeralgoritme in Python in een functie
        hieronder genaamd my_sort(lst).
    1c. Best en worst case
        -   Stel je hebt een lijst met de waarden 1, 2 en 3. Bij welke
            volgorde van de waarden in de lijst is het sorteeralgoritme
            het snelste klaar (best-case scenario)?
            Hoeveel vergelijkingen (zoals beschreven in stap 1. van de
            pseudocode) zijn nodig geweest?

            Het best case scenario is bij de input [1,2,3], er gebeuren slechts 2 vergelijkingen

        -   Bij welke volgorde van de waarden in de lijst is het
            sorteeralgoritme het minst snel klaar (worst-case scenario)?
            Hoeveel vergelijkingen zijn nodig geweest?

            Het worst case scenario is bij de input [3,2,1], er gebeuren 6 vergelijkingen

        -   Stel je hebt een lijst met de waarden 1 tot en met 4.
            Wat is nu het best-case scenario? 
            Hoeveel vergelijkingen zijn er nodig?
            En wat is nu het worst-case scenario?
            Hoeveel vergelijkingen zijn er nodig?

            Best case scenario  [1,2,3,4], er gebeuren 3 vergelijkingen
            Worst case scenario [4,3,2,1], er gebeuren 12 vergelijkingen
            
        -   Stel je hebt een lijst met de waarden 1 tot en met n
            (je weet nu dus niet precies hoeveel waarden er in de lijst
            zitten, het zijn er 'n').
            Wat is nu het best-case scenario?           
            Hoeveel vergelijkingen zijn er nodig?
            En wat is nu het worst-case scenario?            
            Hoeveel vergelijkingen zijn er nodig?

            In het best-case scenario is de lijst reeds gesorteerd het aantal vergelijkinge is n-1 
            In het worst-case scenario is de lijst reversed, het aantal vergelijkingen is dan n*(n-1)
"""

def linear_search_recursive(lst, target):
    #als de lijst leeg is zit het element er zeker niet in 
    if(len(lst) == 0):
        return False
    else: 
        return lst[0] == target or linear_search_recursive(lst[1:len(lst)],target)
        #oftewel is het eerste element van de lijst het target, zoniet zoek het in de rest van de lijst
        

#neemt een lijst en verwisselt het i en j-de element
def swap(lst,i,j):
    lst[i],lst[j] = lst[j], lst[i]
    return lst
    
#voert stappen 1,2 en 3 uit. Als er verwisselingen voorkomen geeft het true terug, anders false
def swap_to_end(lst):
    swaps_performed = False 
    for i in range(len(lst)-1):
        if(lst[i]> lst[i+1]):
            swap(lst,i,i+1)
            swaps_performed = True
    return swaps_performed

def my_sort(lst):
    lst_copy = lst.copy()    
    while(swap_to_end(lst_copy)):
        pass
    return lst_copy


def binary_search_recursive(lst, target):
    def binary_search_recursive_internal(lst,min,max,target):
        if min > max: 
            return False
        else: 
            mid = (min + max)//2   #gehele deling
            if(lst[mid] == target):
                return True
            elif(lst[mid] > target):
                return binary_search_recursive_internal(lst, min,mid-1,target)
            elif(lst[mid] < target):
                return binary_search_recursive_internal(lst, mid+1 ,max,target)
    return binary_search_recursive_internal(lst,0,len(lst)-1, target)

import random


def test_id():
    assert naam != "", "Je moet je naam nog invullen!"
    assert studentnummer != -1, "Je moet je studentnummer nog invullen!"
    assert klas != "", "Je moet je klas nog invullen!"


def test_my_sort():
    lst_test = random.choices(range(-99, 100), k=6)
    lst_copy = lst_test.copy()
    lst_output = my_sort(lst_test)

    assert lst_copy == lst_test, "Fout: my_sort(lst) verandert de inhoud van lijst lst"
    assert lst_output == sorted(lst_test), \
        f"Fout: my_sort({lst_test}) geeft {lst_output} in plaats van {sorted(lst_test)}"


def test_linear_search_recursive():
    for _ in range(10):
        lst_test = random.sample(range(20), 6)
        target = random.randrange(20)
        found = target in lst_test
        lst_copy = lst_test.copy()

        outcome = linear_search_recursive(lst_test, target)
        assert lst_copy == lst_test, "Fout: linear_search_recursive(lst, target) verandert de inhoud van lijst lst"
        assert outcome == found, \
            f"Fout: linear_search_recursive({lst_test}, {target}) geeft {outcome} in plaats van {found}"


def test_binary_search_recursive():
    for _ in range(10):
        lst_test = sorted(random.sample(range(20), 6))
        target = random.randrange(20)
        found = target in lst_test
        lst_copy = lst_test.copy()

        outcome = binary_search_recursive(lst_test, target)
        assert outcome == found, \
            f"Fout: binary_search_recursive({lst_test}, {target}) geeft {outcome} in plaats van {found}"
        assert lst_copy == lst_test, "Fout: binary_search_recursive(lst, target) verandert de inhoud van lijst lst"


def main():
    try:
        print("\x1b[0;32m")
        test_id()

        test_my_sort()
        print("Je functie my_sort() werkt goed!")

        test_linear_search_recursive()
        print("Je functie linear_search_recursive() werkt goed!")

        test_binary_search_recursive()
        print("Je functie binary_search_recursive() werkt goed!")

        print("\nGefeliciteerd, alles lijkt te werken!")
        print("Lever je werk nu in op Canvas...")

    except AssertionError as ae:
        print("\x1b[0;31m")
        print(ae)


if __name__ == '__main__':
    main()



