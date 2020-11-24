### cookiecutter-cpp 

This cookiecutter is an attempt to alleviate some of the pain associated with setting up boilerplate for a small to medium sized cpp project that utilizes CMake with conan and vscode. 

It's not fully featured but the basic structure can easily be modified and extended to suit your project's needs. 


#### Usage 
-----------
First install cookiecutter with pip into your python environment 
```{bash}
$ pip install cookiecutter 
```

Automatically create your project folder in your current directory.
```{bash}
$ cookiecutter https://github.com/bsnacks000/cookiecutter-cpp.git 
```

This will go through some basic settings for CMake, project structure and conan dependencies. It configures gtest to work with Ctest by default using the `gtest_discover_tests()` macro and will automatically run tests before builds.

Basic vscode settings are included for allowing the IDE to read header files for your locally installed conan recipes. 


Basic project layout will look like this:
```
myproject
    .vscode             <--------- default settings for allowing vscode to intellisense conan package headers
    app/                <--------- for executables (optional with create_app_directory)
        CMakeLists.txt 
        main.cpp
    build/              <--------- local build dir for CMake and conan (optional with auto_initialize_conan)
    src/                <--------- library source code 
        myproject/      <--------- project namespace
            hello.cpp
            hello.hpp
        CMakeLists.txt
    test_package        <--------- for creating a conan package (created by `conan new myproject/0.1 -t`) 
        CMakeLists.txt
        example.cpp 
        conanfile.py 
    tests               <--------- gtest comes set up with Cmake/Ctest
        myproject/
            main.cpp 
            test_myproject.cpp
        CMakeTests.txt 
    .gitignore
    conanfile.py        <--------- basic conanfile that can be used to build a package, add/remove dependencies etc.
    LICENSE
    README.md
```

