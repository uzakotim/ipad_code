//Libraries for Function
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <iostream>
#include <vector>

/* ----------------------------------------------------- */
bool err;
#define IS_TRUE(x) {if (!(x)) {\
    std::cerr<<"⛔️ :"  <<" FAILED" <<std::endl;\
    err = true;}}
/* ----------------------------------------------------- */
// Function
std::vector<int> findPrimes(int value)
{
    std::vector<int> result = {};
    bool isPrime = false;
    for(int i =2;i<=value;i++)
    {
        isPrime = true;
        for (int j=2;j<i;j++)
        {
            if ((i%j)==0){
                isPrime = false;
                break;
            }
        }
        if (isPrime)
        {
            result.push_back(i);
        }
        else
        {
            continue;
        }
    }
    return result;
}

/* ----------------------------------------------------- */
// Tests
void handleTest(int test_number, int input, std::vector<int> check)
{
    std::vector<int> result = findPrimes(input);
    std::cout<<"TEST "<<test_number<<":"<<std::endl;
    IS_TRUE(result==check);
    if (err==false)
        std::cout<<"✅ : PASSED\n";
}

void execute_tests()
{
    // handleTest(test number, input, reference)
    std::vector<int> reference = {2,3};
    handleTest(1,3,reference);   
    reference = {2,3,5};
    handleTest(2,6,reference);
    reference = {2,3,5,7,11};
    handleTest(3,11,reference);
}

/* ----------------------------------------------------- */
int main(void)
{ 
    execute_tests();
    if (err == false) std::cout<<"All tests are passed\n";
}