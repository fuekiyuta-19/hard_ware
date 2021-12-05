#include <iostream>
#include <string>

void array()
{
    int array[] = {4, 2, 1, 9, 5};
    std::cout << array[0] << std::endl;
    std::cout << array[1] << std::endl;
    std::cout << array[2] << std::endl;
    std::cout << array[3] << std::endl;
    std::cout << array[4] << std::endl;
}

int main()
{
    std::string hello = "Hello";
    std::cout << hello << std::endl;
    hello = ", String";
    std::cout << hello << std::endl;
    array();
}
