#include <iostream>
#include <string>

class person
{
    std::string m_name;
    int m_age;
    person(int age);

public:
    person();
    person(std::string m_name, int age);

    void set_name(std::string m_name);
    void set_age(int age);

    std::string name() const;
    int age() const;
};

person::person(int age) : m_age(age)
{
    std::cout << "共通コンストラクター" << std::endl;
}

person::person() : person(-1)
{
    std::cout << "引数なしコンストラクター" << std::endl;
}

person::person(std::string name, int age) : person(age)
{
    std::cout << "引数付きコンストラククター" << std::endl;

    set_name(name);
}

void person::set_name(std::string name)
{
    m_name = name;
}

void person::set_age(int age)
{
    m_age = age;
}

std::string person::name() const
{
    return m_name;
}

int person::age() const
{
    return m_age;
}

int main()
{
    person alice("ailce", 15);
    std::cout << alice.name() << std::endl;
}