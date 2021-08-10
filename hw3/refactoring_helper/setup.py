from setuptools import setup, find_namespace_packages


setup(
    name='refactoring_helper',
    version='1.1.5',
    description='Personal assistant-helper. Addressbook. Notesbook. Folder cleaner',
    url='https://github.com/tritochky/goit-python-web/tree/dev',
    author='Olga Fomenko, Anna Khodyka, Nykyforets Volodymyr',
    author_email='helga.fomenko@gmail.com',
    license='MIT',
    entry_points={'console_scripts': [
        'refactoring_helper=refactoring_helper.main:main']},
    include_package_data=True, packages=find_namespace_packages())
