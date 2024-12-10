#include <iostream>

int main() {
    int result[3];
    int array[3];
    std::cin>>array[0]>>array[1]>>array[2];
    for(int i =0;i<3;i++)
    {
        if(array[i]%2==0)
        {
            result[i] = array[i]/2;
        }
        else
        {
            result[i] = array[i]/2 + 1;
        }
    }
    int total =0;
    for(int value : result)
    {
        total+=value;
    }
    std::cout << total << '\n';
    // put your code here
    return 0;
}