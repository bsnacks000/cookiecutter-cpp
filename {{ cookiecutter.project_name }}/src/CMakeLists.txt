# Configure the project sources and headers within the project namespace
{% if cookiecutter.create_public_headers_directory == 'y' %}
set(public_headers 
    ${CMAKE_CURRENT_SOURCE_DIR}/include/${proj_name}/public.hpp
)
{% endif %}

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
    {%if cookiecutter.create_public_headers_directory == 'y' %}
    ${public_headers}
    {%endif%}
    ${sources}
)

target_include_directories(${proj_name}
    PUBLIC
    {%if cookiecutter.create_public_headers_directory == 'y' %}
    ${CMAKE_SOURCE_DIR}/include 
    {%endif%}
    ${CMAKE_CURRENT_SOURCE_DIR}
    ${CONAN_LIBS}
)


