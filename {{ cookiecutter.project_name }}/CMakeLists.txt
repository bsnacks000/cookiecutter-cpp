cmake_minimum_required(VERSION 3.10)

set(proj_name {{cookiecutter.project_name}})

# project 
project( ${proj_name}  VERSION 0.1.0 LANGUAGES C CXX)

# conan config 
include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake) 
conan_basic_setup()

# everyone needs threads... everyone...
find_package(Threads REQUIRED)


# set language things
set(CMAKE_CXX_STANDARD {{cookiecutter.cxx_standard}})  # XXX add this to cc
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)
set(CMAKE_C_STANDARD {{cookiecutter.c_standard}})  # XXX add this to cc
set(CMAKE_C_STANDARD_REQUIRED ON)


set(sources_to_format "")
set(targets_to_tidy "")


{% if cookiecutter.create_extern_directory == 'y' %}
add_subdirectory(extern) # included if user chooses to add and configure an extern directory for non-conan based projects
{% endif %}
add_subdirectory(src)
{% if cookiecutter.create_application_directory == 'y' %}
add_subdirectory(app) #included if user chooses create_application
{% endif %}
add_subdirectory(tests)
