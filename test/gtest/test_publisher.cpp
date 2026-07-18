/**
 * @file test_publisher.cpp
 * @brief Unit test for the ros2 publisher node.
 * 
 * This files contains test cases to verify the functionality of our minimal publisher.
 * we test main things:
 * 1. That the node iis created correctly with the right name and topic
 * 2.. That is publishes the expected "Hello World!" message
 * 
 * Testing Framework:
 *  Google Test (gtest) for C++ unit testing
 * 
 * Tests:
 *   TestNodeCreation: Verifies node name and publisher setup
 *   TestMessageContent: Verifies publisher message format
 * 
 * @author Pal
 * @date July 18, 2026
 */

#include <gtest/gtest.h>
#include "rclcpp/rclcpp.hpp"
#include "std_msgs/msg/String.hpp"

class MinimalCppPublisher;

#define Testing_Exclude_Main
#include "../../src/cpp_minimal_publisher.cpp"

class TestMinimalPublisher : public :: testing::Test
{
protected:
    void SetUp() override
    {
        rclcpp::init(0, nullptr);
        node = std::make_shared<MinimalCppPublisher>();

    }
    void TearDown() override
    {
        node.reset();
        rclcpp::shutdown();
    }
    std::shared_ptr<MinimalCppPublisher> node;
};

TEST_F(TestMinimalPublisher, TestNodeCreation)
{
    EXPECT_EQ(std::string(node->get_name()), std::string(""))
}

