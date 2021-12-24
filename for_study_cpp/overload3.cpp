#include <iostream>

void show_value(int a)
{
    std::cout << a <<std::endl;
}

void show_value(double a)
{
    std::cout << a <<std::endl;
}

struct vector2d
{
    int x;
    int y;
};

int add(int left, int right)
{
    return left + right;
}

double add(double left, double right)
{
    return left + right;
}

vector2d add(vector2d left, vector2d right)
{
    vector2d v;
    v.x = left.x + right.x;
    v.y = left.y + right.y;
    return v;
}

int main()
{
    int integer = add(1, 2);
    show_value(integer);

    double floating = add(3.14, 4.99);
    show_value(floating);

    vector2d v = {1, 2};
    vector2d u = {2, 8};
    vector2d w = add(u, v);
    std::cout << w.x << ", " << w.y << std::endl;
}