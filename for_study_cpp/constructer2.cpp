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

    person(const person& other);

    void set_name(std::string m_name);
    void set_age(int age);

    std::string name() const;
    int age() const;
};

class A
{
    int m_v;

public:
    // A(int);

    explicit A(int);
    int v() const;
};

A::A(int v) : m_v(v)
{
}

int A::v() const
{
    return m_v;
}

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

person::person(const person& other)
{
    std::cout << "コピーインストラクター" << std::endl;
    set_name(other.name());
    set_age(other.age());
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
    // person alice;
    std::cout << alice.name() << std::endl;
    std::cout << alice.age() << std::endl;

    person copy(alice);
    std::cout << copy.name() << std::endl;
    std::cout << copy.age() << std::endl;

    A x = 42;
    if (x.v() == 42)
    {
        std::cout << "A.v = 42" << std::endl;
    }

    else
    {
        std::cout << "A.v /= 42" << std::endl;
    }
}