// Created on iPad.

#include <iostream>
#include <thread>

void thread_function(void){
   std::cout<<"hello world\n";
   return;
}
int main() {
   std::thread th(thread_function);
   th.join();
   return 0;
}