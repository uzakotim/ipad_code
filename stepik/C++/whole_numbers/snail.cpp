#include <iostream>

int main()
{
    int h,a,b;
    std::cin >> h >> a >> b;
    int counter {0};
    int cur_height{0};
    while (cur_height < h)
    {
        cur_height+=a;
        counter+=1;
        if (cur_height>=h)
        {
            break;
        }
        cur_height-=b;
        if (cur_height>=h)
        {
            break;
        }
    }   
    std::cout<<counter<<'\n';
}