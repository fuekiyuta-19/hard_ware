#include <iostream>

void nochange(int i)
{
    i = 42;
}

void setvalue(int *pi)
{
    *pi = 42;
}

int main()
{
    int i = 0;

    nochange(i);

    std::cout << i << std::endl;

    setvalue(&i);

    std::cout << i << std::endl;

}