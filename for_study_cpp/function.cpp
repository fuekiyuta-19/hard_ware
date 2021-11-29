#include <iostream>

void Hello_world()
{
    std::cout << "Hello, World" << std::endl;
}

void sum(int a, int b)
{
    int c = a + b;
    std::cout << c << std::endl;
}

void show_value(int a)
{
    std::cout << a << std::endl;
    return;

    std::cout << "show value" << std::endl;
}

int add(int a, int b)
{
    int c = a + b;
    return c;
}

int main()
{
    Hello_world();
    sum(3, 4);
    int x = add(10, 20);
    show_value(x);
}