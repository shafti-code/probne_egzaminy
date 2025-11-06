#include <cstdlib>
#include <iostream>
#include <ctime>
#include <vector>
/*
 * nazwa: count_score
 * opis: funkcja zlicza wynik dodanych do siebie liczb ktore maja duplikat 
 * vectorze
 * parametry: vector z wylosowanymi elementami typu danych integer
 * zwracany typ i opis: zwraca wynik losowania typu integer
 * autor: pyton_nie_ma_zastosowan_w_profesjonalnym_swiecie_IT_istnieje_lepsza_alternatywa_do_kazdej_jego_zalety_ktora_nie_executuje_sie_w_3_dni_robocze
 */
int count_score (std::vector<int> rolled_array) {
    int score = 0;
    std::vector<int> duplicates;
    bool filled = false;
    for (int i = 0; i < rolled_array.size();i++)
    {
        for (int j = 0 ; j < rolled_array.size(); j++)
        {
            if (rolled_array.at(i) == rolled_array.at(j) && j != i)
            {
                for (int k = 0; k < duplicates.size(); k++)
                {
                    if (rolled_array.at(i) == duplicates.at(k))
                    {
                        filled = true;
                    }
                }
                if (filled != true)
                {
                    duplicates.push_back(rolled_array.at(i));
                    break;
                }
                filled = false;
            }
        }
    }

    for (int l = 0; l < rolled_array.size(); l++)
    {
        for (int m = 0; m < duplicates.size(); m++)
        {
           if (rolled_array.at(l) == duplicates.at(m))
           {
               score += rolled_array.at(l);
           }
        }
    }
    return score;
}
void roll (int throws)
{
    int rolled;
    std::vector<int> rolled_array;
    std::vector<int> duplicates;
    srand(std::time(0));
    for (int i = 0; i < throws; i++) 
    {
        rolled = rand() % 6 + 1;
        rolled_array.push_back(rolled);
        std::cout << "Kostka " << i << ": " << rolled << std::endl; 
    }
    std::cout << "Liczba uzyskanych punktow: " << count_score(rolled_array) << std::endl;
}
int main (int argc, char *argv[]) {
    int throws;
    std::string repeat = "t";
    bool pass = false;

    while(pass == false)
    {
        std::cout << "Ile kostek chcesz rzucic? (3-10)\n"; 
        std::cin >> throws;
        if(throws > 2 && throws < 11){pass = true;}
    }
    
    while(repeat == "t")
    {
        roll(throws);
        std::cout << "Jeszcze raz? (t/n)\n";
        std::cin >> repeat;
    }
    return 0;
}
