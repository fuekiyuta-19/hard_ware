#include <iostream>

// int one()
// {
//     return 1;
// }

void auto_()
{
    int array[] = {0, 1, 2, 3, 4};
    for (auto e : array)
    {
        std::cout << e << std::endl;
    }
}

decltype(1) one()
{
    return 1;
}

int main()
{
    // auto d = 3.14;

    // d = 2.17f;

    // std::cout << d << std::endl;

    // auto i = one();
    // i = 42.195;

    // std::cout << i << std::endl;

    auto k = one();

    decltype(k) l;

    l = 42.195;
    std::cout << l << std::endl;
}