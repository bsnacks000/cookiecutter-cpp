#!/usr/bin/env python
import os
import shutil
import subprocess

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)


if __name__ == '__main__':

    if '{{ cookiecutter.create_application_directory }}'.lower() != 'y': 
        shutil.rmtree(os.path.join(PROJECT_DIRECTORY, "app"))
        
    if '{{ cookiecutter.auto_initialize_conan }}'.lower() == 'y':
        # NOTE this just installs conan libs in a build directory for local development 
        # after the cookie cutter is done... 
        # It is purely for convenience... 

        build_dir = os.path.join(PROJECT_DIRECTORY, 'build')
        if not os.path.exists(build_dir): 
            os.mkdir(build_dir)
        os.chdir(build_dir)
        os.system('conan install ..')
        os.chdir(PROJECT_DIRECTORY)