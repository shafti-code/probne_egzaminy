using System;
using System.Collections.Generic;

/*
 * nazwa: count_score
 * opis: funkcja zlicza wynik dodanych do siebie liczb ktore maja duplikat 
 * vectorze
 * parametry: lista z wylosowanymi elementami typu danych integer
 * zwracany typ i opis: zwraca wynik losowania typu integer
 * autor: pyton_nie_ma_zastosowan_w_profesjonalnym_swiecie_IT_istnieje_lepsza_alternatywa_do_kazdej_jego_zalety_ktora_nie_executuje_sie_w_3_dni_robocze
 */
class Program
{
    static int CountScore(List<int> rolledArray)
    {
        int score = 0;
        List<int> duplicates = new List<int>();

        for (int i = 0; i < rolledArray.Count; i++)
        {
            for (int j = 0; j < rolledArray.Count; j++)
            {
                if (rolledArray[i] == rolledArray[j] && j != i)
                {
                    bool filled = false;
                    for (int k = 0; k < duplicates.Count; k++)
                    {
                        if (rolledArray[i] == duplicates[k])
                        {
                            filled = true;
                        }
                    }
                    if (!filled)
                    {
                        duplicates.Add(rolledArray[i]);
                        break;
                    }
                }
            }
        }

        for (int l = 0; l < rolledArray.Count; l++)
        {
            for (int m = 0; m < duplicates.Count; m++)
            {
                if (rolledArray[l] == duplicates[m])
                {
                    score += rolledArray[l];
                }
            }
        }
        return score;
    }

    static void Roll(int throws)
    {
        Random rand = new Random();
        List<int> rolledArray = new List<int>();

        for (int i = 0; i < throws; i++)
        {
            int rolled = rand.Next(1, 7); // 1–6 inclusive
            rolledArray.Add(rolled);
            Console.WriteLine($"Kostka {i}: {rolled}");
        }

        Console.WriteLine($"Liczba uzyskanych punktow: {CountScore(rolledArray)}");
    }

    static void Main(string[] args)
    {
        int throws = 0;
        string repeat = "t";
        bool passCheck = false;

        while (!passCheck)
        {
            Console.WriteLine("Ile kostek chcesz rzucic? (3-10)");
            throws = int.Parse(Console.ReadLine());
            if (throws > 2 && throws < 11) { passCheck = true; }
        }

        while (repeat == "t")
        {
            Roll(throws);
            Console.WriteLine("Jeszcze raz? (t/n)");
            repeat = Console.ReadLine();
        }
    }
}

