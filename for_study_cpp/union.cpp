#include <iostream>

struct S
{
    int a;
    int b;
    int c;
};

union U
{
    int a;
    int b;
    int c;
};

int main()
{

    U u = {42};
    S s = {40};


    std::cout << "u.a" << u.a << std::endl;
    std::cout << "u.b" << u.b << std::endl;
    std::cout << "u.c" << u.c << std::endl;

    std::cout << "s.a" << s.a << std::endl;
    std::cout << "s.b" << s.b << std::endl;
    std::cout << "s.c" << s.c << std::endl;

    std::cout << "s.a address" << &s.a << std::endl;
    std::cout << "s.b address" << &s.b << std::endl;
    std::cout << "s.c address" << &s.c << std::endl;

    std::cout << "u.a address" << &u.a << std::endl;
    std::cout << "u.b address" << &u.b << std::endl;
    std::cout << "u.c address" << &u.c << std::endl;

    u.c = 100;
    s.c = 100;
    std::cout << "u.a" << u.a << std::endl;
    std::cout << "u.b" << u.b << std::endl;
    std::cout << "u.c" << u.c << std::endl;

    std::cout << "s.a" << s.a << std::endl;
    std::cout << "s.b" << s.b << std::endl;
    std::cout << "s.c" << s.c << std::endl;
}