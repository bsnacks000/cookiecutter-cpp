from conans import ConanFile, CMake, tools


class HelloConan(ConanFile):
    name = "{{ cookiecutter.project_name }}"
    version = "0.1"
    license = "<Put the package license here>"
    author = "<Put your name here> <And your email here>"
    url = "<Package recipe repository url here, for issues about the package>"
    description = "{{ cookiecutter.short_project_description }}"
    topics = ("<Put some tag here>", "<here>", "<and here>")
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = {"shared": False}
    generators = "cmake"
    requires = (
        {% if cookiecutter.include_boost == 'y' %}
            'boost/1.71.0@conan/stable',
        {% endif %}

        {% if cookiecutter.include_spdlog == 'y' %}
            'spdlog/1.4.2@bincrafters/stable',
        {% endif %}

        {% if cookiecutter.include_cli11 == 'y' %}
            'cli11/1.6.1@bincrafters/stable',
        {% endif %}
    )
    build_requires = ('gtest/1.8.1@bincrafters/stable',)    
    exports_sources = (
        'CMakeLists.txt',
        'src/*',
        'tests/*',
        {% if cookiecutter.create_application_directory == 'y' %}
        'app/*',
        {% endif %}
    )
    
    source_folder = '.'
    build_folder = './build'


    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()
        cmake.test()


    def package(self):
        self.copy("*.h", dst="include", src="{{ cookiecutter.project_name }}")
        self.copy("*.hpp", dst='include',)
        self.copy("*{{ cookiecutter.project_name }}.lib", dst="lib", keep_path=False)
        self.copy("*.dll", dst="bin", keep_path=False)
        self.copy("*.so", dst="lib", keep_path=False)
        self.copy("*.dylib", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["{{ cookiecutter.project_name }}"]

