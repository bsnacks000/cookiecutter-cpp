#!/usr/bin/env python
import os
import shutil

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)


if __name__ == '__main__':

    if '{{ cookiecutter.create_extern_directory }}'.lower() != 'y':
        shutil.rmtree(os.path.join(PROJECT_DIRECTORY, "extern"))

    if '{{ cookiecutter.create_application_directory }}'.lower() != 'y': 
        shutil.rmtree(os.path.join(PROJECT_DIRECTORY, "app"))

    if '{{ cookiecutter.create_public_headers_directory }}'.lower() != 'y': 
        shutil.rmtree(os.path.join(PROJECT_DIRECTORY, "include"))