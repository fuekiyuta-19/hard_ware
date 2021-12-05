#include <iostream>

void array(int i, int j, int l)
{
    int array[5] = {i, j, l};
    std::cout << "array[0] = " << array[0] << std::endl;
    std::cout << "array[1] = " << array[1] << std::endl;
    std::cout << "array[2] = " << array[2] << std::endl;
    std::cout << "array[3] = " << array[3] << std::endl;
    std::cout << "array[4] = " << array[4] << std::endl;
}

void char_raw()
{
    char hello[] = "Hello";
    char array[6] = {'a', 'r', 'r'};
    array[3] = 'a';
    array[4] = 'y';
    array[5] = '\0';
    std::cout << hello  << array << std::endl;
}

int main()
{
    array(3, 4, 5);
    int array[10] = {};
    std::cout << "size of array" << sizeof(array) << "size of int" << sizeof(int) << std::endl;
    std::size_t length = sizeof(array) / sizeof(array[0]);
    std::cout << "array[" << length << "]" << std::endl;
    int ay[2] = {};
    std::cout << "size of ay" << sizeof(ay) << std::endl;
    char_raw();

}