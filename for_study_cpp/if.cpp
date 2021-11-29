#include <iostream>

void compare(int a)
{
    if (10 < a)
    {
        std::cout << "A is larger than 10" << std::endl;
    }

    else
    {
        std::cout << "A is smaller than 10" << std::endl;
    }
}

void show_message(int value)
{
    if (10 <= value && value < 20)
    {
        std::cout << value << "is between 10 and 20" << std::endl;
    }
    else
    {
        std::cout << value << "is not between 10 and 20" << std::endl;
    }
}

int main()
{
    compare(9);
    compare(20);
    show_message(9);
    show_message(15);
}