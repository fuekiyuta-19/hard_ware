#include <iostream>
#include <string>

int main(){

    std::string strA = "Hello, ";
    std::string strB = "World.";

    std::string strC = strA + strB;
    std::cout << strC << std::endl;

    if (strC == "Hello, World."){
        std::cout << "OK." << std::endl;
    }else{
        std::cout << "Different." << std::endl;
    }

    std::string s0;
    std::cout << "s0: " << s0 << std::endl;

    std::string s1 = "Hello";
    std::cout << "s1: " << s1 << std::endl;

    std::string s2 = {"Hello", 4};
    std::cout << "s2: " << s2 << std::endl;

    std::string s3 = s1;
    std::cout << "s3: " << s3 << std::endl;

    std::string s4 = {3, '?'};
    std::cout << "s4: " << s4 << std::endl;

    std::string s5 = {'a', 'b', 'c'};
    std::cout << "s5: " << s5 << std::endl;

    std::string s6{s1.begin() + 1, s1.end() - 1};
    std::cout << "s6: " << s6 << std::endl;

    std::string str{"Hello\0world", 11};
    std::cout << str << std::endl;

    for (char ch : str)
    {
        std::cout << (ch == '\0' ? '_' : ch);

    }
    std::cout << std::endl;
}
