#include <iostream>
int NWD (int a, int b)
{
    
    while (true)
    {
        if (a == b)
        {
            break;
        }
        if (a > b)
        {
            a = a-b;
        }
        else 
        {
            b =  b-a;
        }
    }
    return a;
}

int main () 
{
    int a,b;
    std::cout << "Podaj a: ";
    std::cin >> a;
    std::cout << "Podaj b: ";
    std::cin >> b;
    std::cout << "NWD is: " << NWD(a,b) << std::endl;
    return 0;
}
