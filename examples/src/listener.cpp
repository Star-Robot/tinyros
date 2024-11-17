/**
 * @file listener.cpp
 * @author your name (you@domain.com)
 * @brief 演示订阅者的使用
 * @version 0.1
 * @date 2024-11-17
 * 
 * @copyright Copyright (c) 2024
 * 
 */
#include "base/node.hpp"
#include "base/subscriber.hpp"
#include "message/std_msgs.hpp"

using namespace huleibao;

/**
 * @brief Callback function
 * 
 * @param msg 
 */
void Callback(std_msgs::String::ConstPtr msg) {
  std::cout << "I heard: " << msg->data << std::endl;
}

int main() {

  // - create listener node
  Node node("listener");

  // - subscrib topic_difference
  Subscriber<std_msgs::String>::Ptr sub =
      node.Subscribe<std_msgs::String>("topic_color", 1, Callback);

  // - spin
  Spin();

  return 0;
}