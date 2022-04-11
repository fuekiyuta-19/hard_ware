#include <iostream>
#include <sstream>
#include <string>
#include <stdio.h>
#include <stdlib.h>

class sumple_msg{
    std::string m_msg;
    int msg_hex;

public:
    sumple_msg();

    void set_msg(std::string msg);
    std::string msg();
    int decord(std::string msg);
};

sumple_msg::sumple_msg() : m_msg("0"){
    std::cout << "Initialized" << std::endl;
}

std::string sumple_msg::msg(){
    return m_msg;
}

void sumple_msg::set_msg(std::string msg){
    m_msg = msg;
}

int sumple_msg::decord(std::string msg){
    unsigned int out = 0;
    for (int i = 0, size = msg.size() ; i < size ; ++i){
        out *= 2;
        out += ((int)msg[i] == 49) ? 1 : 0;
    }
    std::ostringstream oss;
    oss << out;
    msg_hex = std::stoi(oss.str());
    return msg_hex;
}

int main(){
    sumple_msg sumple_one;

    std::cout << sumple_one.msg() << std::endl;
    sumple_one.set_msg("00010010");
    std::cout << sumple_one.msg() << std::endl;
    std::cout << sumple_one.decord(sumple_one.msg()) << std::endl;
}
