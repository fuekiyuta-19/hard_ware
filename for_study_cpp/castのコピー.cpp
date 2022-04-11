#include <iostream>

int main()
{
    char c = 99;

    std::cout << c << std::endl;
    std::cout << static_cast<int>(c) << std::endl;
}