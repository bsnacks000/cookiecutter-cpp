#include <gtest/gtest.h>
#include <{{cookiecutter.project_name}}/hello.hpp>

TEST(hellotest, sayHello) {
    hello::Say();
}