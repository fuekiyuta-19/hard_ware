#include <iostream>

struct product
{
    int id;
    int price;
    int stock;
};

int main()
{
    product pen = {0, 100, 200};

    product car = {1, 10000, 2};

    product * ptr  = &pen;
    product * cptr = &car;

    std::cout << "ID" << ptr -> id << std::endl;
    std::cout << "Price" << ptr -> price << std::endl;
    std::cout << "Stock" << ptr -> stock << std::endl;
    std::cout << "ID" << cptr -> id << std::endl;
    std::cout << "Price" << cptr -> price << std::endl;
    std::cout << "Stock" << cptr -> stock << std::endl;
}