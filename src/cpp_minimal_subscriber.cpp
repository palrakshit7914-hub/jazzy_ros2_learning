/**
 * @file cpp_minimal_subscriber.cpp
 * @author Pal
 * @brief Demonstrates subscribing to msg on a ros2 topic 
 * @version 0.1
 * @date 2026-07-14
 * 
 * @copyright Copyright (c) 2025
 * 
 * -------
 * Subscriber Topic:
 * String msg
 * /cpp_example_topic - std_msgs/String
 * -----
 * Publishing Topic:
 * None
 * 
 */

#include "rclcpp/rclcpp.hpp" //Ros 2 C++ Client Library
#include "std_msgs/msg/string.hpp"// Handling String messages

using std::placeholders::_1; //placeholder for callback function

class MinimalCppSubscriber : public rclcpp::Node
{
public:
    MinimalCppSubscriber() : Node("minimal_cpp_subscriber")
    {
        subscriber_ = create_subscription<std_msgs::msg::String>
        (
            "/cpp_example_topic",
            10,
            std::bind(
                &MinimalCppSubscriber::topicCallback,
                this,
                _1
            )
        );

    }

    void topicCallback(const std_msgs::msg::String & msg) const
    {
        RCLCPP_INFO_STREAM(get_logger(), "I heard: " << msg.data.c_str());
    }

private:
    //Member variable
    rclcpp::Subscription<std_msgs::msg::String>::SharedPtr subscriber_;
};

int main(int argc , char * argv[])
{
    rclcpp::init(argc, argv);

    auto minimal_cpp_subscriber_node = std::make_shared<MinimalCppSubscriber>();
    rclcpp::spin(minimal_cpp_subscriber_node);

    rclcpp::shutdown();

    return 0;
}
