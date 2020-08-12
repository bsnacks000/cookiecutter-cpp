{% if cookiecutter.unittest_framework == "gtest" %}
#include <gtest/gtest.h>
#include <{{cookiecutter.project_name}}/hello.hpp>

TEST(hellotest, sayHello) {
    hello::say();
}
{% else %}
#define CATCH_CONFIG_MAIN
#include <catch2/catch.hpp>

#include <{{cookiecutter.project_name}}/hello.hpp>

TEST_CASE("hello was said", "[hello]") {
    hello::say();
}

{% endif %}
