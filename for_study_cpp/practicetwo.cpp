#include <iostream>

void Hello_world()
{
    std::cout << "Hello, World" << std::endl;
}

int sum(int a, int b, int c)
{
    int x = a + b;
    int y = x + c;
    return y;
}

int main()
{
    Hello_world();
    std::cout << "sum(1, 2, 3): " << sum(1, 2, 3) << std::endl;
}