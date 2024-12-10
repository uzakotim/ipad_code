#include <iostream>
#include <string.h>
int findSumOfDigits(char * number )
{   
    char digits[strlen(number)+1];
    strcpy(digits,number);
    int sum = 0;
    for(int i =0;i<strlen(number);i++)
    {
        sum+=digits[i]-'0';
    }    
    return sum;
}
int main() {
       // put your code here
    int a;
    std::cin >> a;
    char num_char[100];
    std::sprintf(num_char, "%d", a);
    int result = findSumOfDigits(num_char);
    std::cout<<result<<'\n';
    return 0;
}