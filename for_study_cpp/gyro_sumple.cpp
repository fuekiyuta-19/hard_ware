#include <iostream>
#include <sstream>
#include <string>
#include <stdio.h>
#include <stdlib.h>
#include <cmath>

class sumple_msg{
    std::string m_msg;
    float yaw_ang;
    float yaw_rate;

public:
    sumple_msg();

    void set_msg(std::string msg);
    std::string msg();
    int decord_yaw(std::string msg);
    int decord_yawrate(std::string msg);
};

sumple_msg::sumple_msg() : m_msg("0"){
    // std::cout << "Initialized" << std::endl;
}

std::string sumple_msg::msg(){
    return m_msg;
}

void sumple_msg::set_msg(std::string msg){
    m_msg = msg;
}

int sumple_msg::decord_yaw(std::string msg){
    std::string yaw_hex = msg.substr(6, 4);
    int yawang = atoi(yaw_hex.c_str());
    yaw_ang    = yawang * 180.0 / (std::pow(2.0, 15.0));
    return yaw_ang;
}

int sumple_msg::decord_yawrate(std::string msg){
    std::string yawrate_hex = msg.substr(10, 4);
    int yawrate = atoi(yawrate_hex.c_str());
    yaw_rate    = yawrate * 200.0 / (std::pow(2.0, 15.0));
    return yaw_rate;
}

int main(){
    sumple_msg sumple_one;
    // std::cout << sumple_one.msg() << std::endl;
    sumple_one.set_msg("02812012345678900D");
    std::cout << sumple_one.msg() << std::endl;
    std::cout << sumple_one.decord_yaw(sumple_one.msg()) << "," << sumple_one.decord_yawrate(sumple_one.msg()) << std::endl;
}
