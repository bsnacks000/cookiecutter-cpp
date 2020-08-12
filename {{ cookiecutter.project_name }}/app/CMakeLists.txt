
set(proj_name {{ cookiecutter.project_name }})
set(app_name {{ cookiecutter.app_name }})

add_executable(${app_name} ${app_name}/main.cpp)

target_link_libraries( ${app_name} PUBLIC
    ${CONAN_LIBS}
    ${proj_name}
)