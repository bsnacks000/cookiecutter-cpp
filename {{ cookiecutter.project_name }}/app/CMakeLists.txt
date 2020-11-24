set(proj_name {{ cookiecutter.project_name }})

add_executable(app main.cpp)

target_link_libraries( app PUBLIC
    ${CONAN_LIBS}
    ${proj_name}
)