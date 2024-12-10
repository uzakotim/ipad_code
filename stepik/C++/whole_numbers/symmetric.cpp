#include <iostream>
#include <vector>
int main()
{
    int number;
    bool ok = true;

    std::cin>>number;
    
    std::vector<int> digits;
    int n = number;
    int k = 1000;
    while(k!=1)
    {
        digits.push_back(n/k);
        n = n%k;
        k /= 10;
    }
    digits.push_back(n/k);
    
    for (int i =0;i<4;i++)
    {
        if (digits[i] != digits[3-i])
        {
            ok = false;
        }
    }

    int result = (ok==true) ? 1: 37;
    std::cout << result <<'\n';
    return 0;

}