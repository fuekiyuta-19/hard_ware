#include <iostream>

void ref_point(int a, int b)
{
    int value = a;
    int other = b;
    int* pointer = &value;
    int& reference = value;
    std::cout << "Address of value " << &value << " Value of value " << value << std::endl;
    std::cout << "Address of other " << &other << " Value of other " << other << std::endl;
    std::cout << "Address of pointer " << pointer << " Value of pointer " << *pointer << std::endl;
    std::cout << "Address of reference " << &reference << " Value of reference " << reference << std::endl;

    pointer = &other;
    reference = other;

    std::cout << std::endl;
    std::cout << "Address of value " << &value << " Value of value " << value << std::endl;
    std::cout << "Address of other " << &other << " Value of other " << other << std::endl;
    std::cout << "Address of pointer " << pointer << " Value of pointer " << *pointer << std::endl;
    std::cout << "Address of reference " << &reference << " Value of reference " << reference << std::endl;

}

int main()
{
    int value = 42;

    std::cout << "Address of value" << &value << "Value of value" << value << std::endl;

    int& reference = value;

    std::cout << "Address of reference" << &reference << "Value of reference" << reference << std::endl;

    reference = 0;

    std::cout << "Address of value" << &value << "Value of value" << value << std::endl;
    std::cout << std::endl;
    ref_point(30, 100);
}