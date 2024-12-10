#include <iostream>

int main() {
    // put your code here
    int v,t;
    std::cin >> v>>t;
    int distance = v*t;
    int reduced_dist = distance%109;
    if (reduced_dist>0)
    {
        std::cout<<0+reduced_dist<<'\n';
    }else
    {   
        std::cout<<109+reduced_dist<<'\n';
    }    
    return 0;
}