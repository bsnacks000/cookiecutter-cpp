set(testname {{cookiecutter.project_name}}tests)

set(sources
    ${proj_name}/test_main.cpp 
    # add other test source cpp/hpp here..   
)

add_executable( ${testname} ${sources} )

target_link_libraries(${testname} PUBLIC
    ${CONAN_LIBS}
    ${proj_name}
)

