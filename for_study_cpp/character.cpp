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


}
