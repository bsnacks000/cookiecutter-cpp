include(GoogleTest)

set(testname {{cookiecutter.project_name}}tests)

set(sources
    ${proj_name}/main.cpp 
    ${proj_name}/test_{{cookiecutter.project_name}}.cpp
    # add other test source cpp/hpp here..   
)

add_executable( ${testname} ${sources} )
gtest_discover_tests( ${testname} )

target_link_libraries(${testname} PUBLIC
    ${CONAN_LIBS}
    ${proj_name}
)
