#include <iostream>

struct product
{
    int id;
    int price;
    int stock;
};

void set_param(product name, int i, int j, int k)
{
    name.id    = i;
    name.price = j;
    name.stock = k;
}    

int main()
{
    // product pen;
    // pen.id    = 0;
    // pen.price = 100;
    // pen.stock = 200;
    product pen = set_param(pen, 0, 100, 200);

    product car;
    car.id    = 1;
    car.price = 10000;
    car.stock = 2;

    product * ptr  = &pen;
    product * cptr = &car;

    std::cout << "ID" << ptr -> id << std::endl;
    std::cout << "Price" << ptr -> price << std::endl;
    std::cout << "Stock" << ptr -> stock << std::endl;
    std::cout << "ID" << cptr -> id << std::endl;
    std::cout << "Price" << cptr -> price << std::endl;
    std::cout << "Stock" << cptr -> stock << std::endl;
}