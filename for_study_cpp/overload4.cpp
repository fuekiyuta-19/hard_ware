#include <iostream>

class product
{
    int id;

public:
    int get_id();
    int get_id() const;
};

int product::get_id()
{
    std::cout << "get_id from anti const member function is called" << std::endl;
    return id;
}

int product::get_id() const
{
    std::cout << "get_id from const member function is called" << std::endl;
    return id;
}

int main()
{
    product p;
    p.get_id();

    const product cp{};
    cp.get_id();

}