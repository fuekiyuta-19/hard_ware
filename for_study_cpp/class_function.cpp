#include <iostream>

class product
{
    int id;

public:
    int get_id() const;
    void set_value(int new_id);
};

int product::get_id() const
{
    return id;
}

void product::set_value(int new_id)
{
    id = new_id;
}

int main()
{
    const product cp{};
    std::cout << cp.get_id() << std::endl;
}