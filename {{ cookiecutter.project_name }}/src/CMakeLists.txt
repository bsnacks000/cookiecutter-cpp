# Configure the project sources and headers within the project namespace

set (sources 
    ${proj_name}/hello.hpp 
    ${proj_name}/hello.cpp    
    # add more hpp/cpp files here    
)


add_library( ${proj_name}
    {%if cookiecutter.library_type == 'static' %}
    STATIC
    {%else%}
    SHARED
    {%endif%}
    ${sources}
)

target_include_directories(${proj_name}
    PUBLIC
    ${CMAKE_CURRENT_SOURCE_DIR}
    ${CONAN_LIBS}
)

include_directories(${proj_name})

