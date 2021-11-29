#include <iostream>

void check_value(int a)
{
    switch (a + 1)
    {
        case 1:
            std::cout << "a + 1 = 1" << std::endl;
            break;

        case 2:
            std::cout << "a + 1 = 2" << std::endl;
            break;

        case 3:
            std::cout << "a + 1 = 3" << std::endl;
            break;
        
        default:
            std::cout << "Other value" << std::endl;
            break;
    }
}

void check_thorough(int a)
{
    switch(2)
    {
        case 1: //FALL THROUGH
        case 2: //FALL THROUGH
        case 3:
            std::cout << "Value is 1 or 2 or 3" << std::endl;
    }
}

void absvalue(int a)
{
    int abs = a < 0 ? -a : a; //a<0なら-aで違うならa
    std::cout << abs << std::endl; 
}

int main()
{
    check_value(1);
    check_value(2);
    check_value(3);
    check_value(4);
    absvalue(-5);
    absvalue(3);
}