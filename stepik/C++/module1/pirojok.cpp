#include <iostream>

int main() {
    int array[3];
    std::cin>>array[0]>>array[1]>>array[2];
    int rub,kop,total;
    total = (array[0]*100 + array[1])*array[2];
    std::cout <<total/100<<' '<<total%100<<'\n'; 
    // put your code here
    return 0;
}