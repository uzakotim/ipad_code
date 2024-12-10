// Created on iPad.
#include <stdio.h>
#include <pthread.h>


void* thread_function()
{
   printf("helllo world\n");
}

int main() {
   pthread_t thread;
   pthread_create(&thread, NULL, thread_function, NULL);
   pthread_join(thread,NULL);
   return 0;
}