import random
import time

"""
 * nazwa: count_score
 * opis: funkcja zlicza wynik dodanych do siebie liczb ktore maja duplikat
 * parametry: lista z wylosowanymi elementami typu danych integer
 * zwracany typ i opis: zwraca wynik losowania typu integer
 * autor: pyton_nie_ma_zastosowan_w_profesjonalnym_swiecie_IT_istnieje_lepsza_alternatywa_do_kazdej_jego_zalety_ktora_nie_executuje_sie_w_3_dni_robocze
"""
def count_score(rolled_array: list[int]) -> int:
    score = 0
    duplicates = []

    for i in range(len(rolled_array)):
        for j in range(len(rolled_array)):
            if rolled_array[i] == rolled_array[j] and j != i:
                filled = False
                for k in range(len(duplicates)):
                    if rolled_array[i] == duplicates[k]:
                        filled = True
                if not filled:
                    duplicates.append(rolled_array[i])
                    break

    for l in range(len(rolled_array)):
        for m in range(len(duplicates)):
            if rolled_array[l] == duplicates[m]:
                score += rolled_array[l]

    return score


def roll(throws: int):
    rolled_array = []
    random.seed(time.time())
    for i in range(throws):
        rolled = random.randint(1, 6)
        rolled_array.append(rolled)
        print(f"Kostka {i}: {rolled}")

    print(f"Liczba uzyskanych punktow: {count_score(rolled_array)}")


def main():
    repeat = "t"
    pass_check = False

    while not pass_check:
        throws = int(input("Ile kostek chcesz rzucic? (3-10)\n"))
        if 2 < throws < 11:
            pass_check = True

    while repeat == "t":
        roll(throws)
        repeat = input("Jeszcze raz? (t/n)\n")


if __name__ == "__main__":
    main()

