/**
 * @file talker.cpp
 * @author your name (you@domain.com)
 * @brief 演示发布者的使用
 * @version 0.1
 * @date 2024-11-17
 * 
 * @copyright Copyright (c) 2024
 * 
 */
#include "base/node.hpp"
#include "base/publisher.hpp"
#include "message/std_msgs.hpp"
#include <string>

using namespace huleibao;

int main() {

  // - create talker node
  Node node("talker");

  // - create publisher
  Publisher<std_msgs::String>::Ptr pub =
      node.Advertise<std_msgs::String>("topic_color", 1);

  // - create rate
  Rate rate(1);

  while (Ok()) {
    // - create message
    std_msgs::String msg;
    msg.data = "red";
    // - publish message
    pub->Publish(msg);
    std::cout << "I say: " << msg.data << std::endl;
    rate.Sleep();
  }

  return 0;
}