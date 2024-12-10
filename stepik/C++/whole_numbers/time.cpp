#include <iostream>

int main() {
    int seconds {0};
    std::cin>>seconds;
    int hours = (seconds/3600)%24;
    int minutes = (seconds%3600)/60;
    int sec = seconds%60;
    char str_hours[3],str_minutes[3],str_sec[3];
    
    std::sprintf(str_hours,"%d",hours);
    if (minutes<10)
    {
        std::sprintf(str_minutes,"0%d",minutes);
    }
    else
    {
        std::sprintf(str_minutes,"%d",minutes);
    }
    if (sec<10)
    {
        std::sprintf(str_sec,"0%d",sec);
    }
    else
    {
        std::sprintf(str_sec,"%d",sec);
    }
    std::cout<<str_hours<<':'<<str_minutes<<':'<<str_sec<<'\n';
    return 0;
}