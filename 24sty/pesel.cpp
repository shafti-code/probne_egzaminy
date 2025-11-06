#include <iostream>

char check_gender(int pesel[11]){
    return pesel[9] % 2 == 0 ? 'K' : 'M';
}
bool validate_pesel(int pesel[11],int weigths[10]){
    int s = 0;
    for (int i = 0; i < 10; i++){
        s += pesel[i] * weigths[i];
    }
    int m = s % 10;
    int r = m == 0 ? 0 : 10 - m;
    return r == pesel[10] ? true : false;
}
int main (int argc, char *argv[]) {
    // int pesel[] = {5,5,0,3,0,1,0,1,1,9,3};
    int pesel[] = {0,7,2,4,2,5,0,9,4,1,4};
    int weigths[] = {1,3,7,9,1,3,7,9,1,3};

    char gender = check_gender(pesel);
    bool valid = validate_pesel(pesel, weigths);

    std::cout << (valid == true ? "valid\n" : "not valid\n");
    std::cout << (gender == 'K' ? "Kobieta\n" : "Mężczyzna\n");
    return 0;
}
