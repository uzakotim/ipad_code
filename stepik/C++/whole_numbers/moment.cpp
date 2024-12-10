#include <iostream>

int main()
{
    int h1,m1,s1,h2,m2,s2;
    std::cin>>h1>>m1>>s1>>h2>>m2>>s2;
    int sec1,sec2;
    sec1 = s1+m1*60+h1*3600;
    sec2 = s2+m2*60+h2*3600;
    
    std::cout<<sec2-sec1<<'\n';
    return 0;
}

/*
1
1
1
2
2
2
*/