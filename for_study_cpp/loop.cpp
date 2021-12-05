#include <iostream>

void loop()
{
    int i = 0;
    while(i<5)
    {
        std::cout << "Hello, World" << std::endl;
        i += 1;
    }
}

void break_cont()
{
    int value[] = {-20, 10, 5, -40, 0, 10, -30};

    int i = 0;
    while(i < 7)
    {
        if(value[i] < 0)
        {
            std::cout << "continue" << value[i] << std::endl;
            ++i;
            continue; 
        }

        if(value[i] == 0)
        {
            std::cout << "break" << std::endl;
            break;
        }

        std::cout << value[i] << std::endl;
        ++i;
    }
    std::cout << "Finish while loop" << std::endl;

}

void forloop()
{
    int value[] = {-20, 10, 5, -40, 0, 10, -30};
    for (int i = 0; i < 7; ++i)
    {
        if(value[i] < 0)
        {
            std::cout << "continue" << value[i] << std::endl;
            continue; 
        }

        if(value[i] == 0)
        {
            std::cout << "break" << std::endl;
            break;
        }

        std::cout << value[i] << std::endl;
    }
    std::cout << "Finish for loop" << std::endl;
    
}

void scan()
{
    int value[] = {-20, 10, 5, -40, 0, 10, -30};

    for (int elem : value)
    {
        if (elem < 0)
        {
            std::cout << "continue" << std::endl;
            continue;
        }

        if (elem == 0)
        {
            std::cout << "break" << std::endl;
            break;
        }

        std::cout << "elem =" << elem << std::endl;

    }

}

void doloop()
{
    int value[] = {-20, 10, 5, -40, 0, 10, -30};
    int i = 0;

    do
    {
        if(value[i] < 0)
        {
            std::cout << "continue" << std::endl;
            ++i;
            continue;
        }

        if (value[i] == 0)
        {
            std::cout << "break" << std::endl;
            break;
        }

        std::cout << "Larger than 0" << std::endl;
        ++i;
    } while (i < 7);

    std::cout << "Finish do loop" << std::endl;
}

int main()
{
    loop();
    break_cont();
    forloop();
    scan();
    doloop();
}