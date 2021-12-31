#include <iostream>
#include <string>

class person
{
    std::string m_name;
    int m_age;

public:
    person();
    ~person();

    void set_name(std::string name);
    void set_age(int age);

    std::string name() const;
    int age() const;
};

//person class内のageを-1と初期化
person::person() : m_age(-1)
{
    std::cout << "Called constructer function" << std::endl;
}

//main関数終了後、関数の定義を消去
person::~person()
{
    std::cout << "Called deconstructer function" << std::endl;
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
    person bob;

    std::cout << "Age after initialize" << bob.age() << std::endl;
    bob.set_name("BOB");
    bob.set_age(20);
    std::cout << "Name is " << bob.name() << std::endl;
    std::cout << "Age is " << bob.age() << std::endl;
    std::cout << "Finish main function" << std::endl;
}