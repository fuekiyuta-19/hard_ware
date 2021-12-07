#include <iostream>

enum class Category
{
    Value1,
    Value2,
    Value3 = 100,
    Value4,
};

class product
{
    int id;
    int price;
    int stock;

public:
    int get_id();
    void set_id(int new_id);

    int get_price();
    void set_price(int new_price);

    int get_stock();
    void set_stock(int new_stock);
};

int product::get_id()
{
    return id;
}

void product::set_id(int new_id)
{
    id = new_id;
}

int product::get_price()
{
    return price;
}

void product::set_price(int new_price)
{
    if(new_price < 0)
    {
        std::cout << "Error" << std::endl;
        return;
    }
    price = new_price;
}

int product::get_stock()
{
    return stock;
}

void product::set_stock(int new_stock)
{
    if(new_stock < 0)
    {
        std::cout << "Error" << std::endl;
        return;
    }
    stock = new_stock;
}

int main()
{
    Category cat = Category::Value3;
    std::cout << static_cast<int>(cat) << std::endl;

    product pen;
    pen.set_id(0);
    pen.set_price(100);
    pen.set_stock(1000);

    product * ptr = &pen;
    std::cout << ptr -> get_id() << std::endl;

}