#include <iostream>
#include <string>

int main()
{
    // int i;
    // std::cout << "Please enter the number>"  ;
    // std::cin >> i;
    // std::cout << "Number is\"" << i << "\"です" << std::endl; 

    std::string s;
    std::cout << "Please enter the words>"  ;
    // std::cin >> s;
    std::getline(std::cin, s);
    std::cout << "Word is\"" << s << "\"です" << std::endl; 
}