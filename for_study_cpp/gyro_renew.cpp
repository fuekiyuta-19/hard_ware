#include <iostream>
#include <sstream>
#include <string>
#include <cmath>
#include <stdio.h>
#include <stdlib.h> /*exit()*/
#include <termios.h>
#include <string.h> /*memset()*/
#include <fcntl.h> /*open(), O_RDWR*/
#include <termios.h>
#include <unistd.h> /*read()*/
#include <ros/ros.h>
#include <std_msgs/String.h>

#define DEV_DIR "/dev/ttyUSB"
#define BAUD_RATE 1200
#define PUB_RATE 10
#define BUFF_SIZE 70

const std::string START_MSG = "02 81 20 12 34 56 78 90 0D";
const std::string RESET_MSG = "02 85 30 30 30 30 45 0D";

class Gyro{
    std::string m_msg;
    float yaw_ang;
    float yaw_rate;

public:
    Gyro();

    void set_msg(std::string msg);
    std::string msg();
    int decord_yaw(std::string msg);
    int decord_yawrate(std::string msg);

    ~Gyro();
};

Gyro::Gyro() : m_msg("0"){
    // std::cout << "Initialized" << std::endl;
}

Gyro::~Gyro(){
}

void msgCallback(const std_msgs::String& msg)
{
  ROS_INFO("subscribe: %s", msg.data.c_str());
}

int Gyro::subscriber(int argc, char** argv)
{
  ros::init(argc, argv, "basic_simple_listener");
  ros::NodeHandle nh;
  ros::Subscriber sub = nh.subscribe("chatter", BUFF_SIZE, msgCallback);

  ros::spin();
  return 0;
  
}

std::string Gyro::msg(){
    return m_msg;
}

void Gyro::set_msg(std::string msg){
    m_msg = msg;
}

int Gyro::decord_yaw(std::string msg){
    std::string yaw_hex = msg.substr(6, 4);
    int yawang = atoi(yaw_hex.c_str());
    yaw_ang    = yawang * 180.0 / (std::pow(2.0, 15.0));
    return yaw_ang;
}

int Gyro::decord_yawrate(std::string msg){
    std::string yawrate_hex = msg.substr(10, 4);
    int yawrate = atoi(yawrate_hex.c_str());
    yaw_rate    = yawrate * 200.0 / (std::pow(2.0, 15.0));
    return yaw_rate;
}

int Gyro::publisher(int argc, char** argv)
{
  ros::init(argc, argv, "ROS_NODE");
  ros::NodeHandle nh;
  ros::Publisher chatter_pub = nh.advertise<std_msgs::String>("chatter", BUFF_SIZE);
  ros::Rate loop_rate(10);

  while (ros::ok())
  {
    std_msgs::String msg;
    msg.data = "hello world!";
    ROS_INFO("publish: %s", msg.data.c_str());
    chatter_pub.publish(msg);

    ros::spinOnce();
    loop_rate.sleep();
  }
  return 0;
}

int main(){
    Gyro sumple_one;
    // std::cout << sumple_one.msg() << std::endl;
    // sumple_one.set_msg(RESET_MSG);
    sumple_one.set_msg(START_MSG);
    // std::cout << sumple_one.msg() << std::endl;
    std::cout << sumple_one.decord_yaw(sumple_one.msg()) << "," << sumple_one.decord_yawrate(sumple_one.msg()) << std::endl;
}
