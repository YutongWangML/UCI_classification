import os
import zipfile  # Make sure to import zipfile here
import shutil
from setuptools import setup, find_packages
from setuptools.command.install import install

class PostInstallCommand(install):
    """Post-installation for installation mode."""
    def run(self):
        install.run(self)
        print("hello world!")
        self.execute_post_install_scripts()

    def execute_post_install_scripts(self):
        self.unzip_data()
        self.cleanup_directories()

    def unzip_data(self):
        zip_path = 'UCI_classification/data_py.zip'  # Path relative to the package
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall('UCI_classification/')  # Unzip into the desired directory


    def cleanup_directories(self):
        base_path = 'UCI_classification/data'
        os.remove(os.path.join(base_path, 'abalone_py.dat'))

        dirs_to_rename = {
            'oocytes_merluccius_nucleus_4d': 'oocytes-merluccius-nucleus-4d',
            'oocytes_merluccius_states_2f': 'oocytes-merluccius-states-2f',
            'oocytes_trisopterus_nucleus_2f': 'oocytes-trisopterus-nucleus-2f',
            'oocytes_trisopterus_states_5b': 'oocytes-trisopterus-states-5b',
        }

        for old_name, new_name in dirs_to_rename.items():
            print("renaming: ", old_name)
            old_dir = os.path.join(base_path, old_name)
            new_dir = os.path.join(base_path, new_name)
            print("old_dir", old_dir)
            print("new_dir", new_dir)
            shutil.move(old_dir, new_dir)
            print("renamed dir")
            old_file = os.path.join(new_dir, old_name + '_py.dat')
            new_file = os.path.join(new_dir, new_name + '_py.dat')
            print("old_file", old_file)
            print("new_file", new_file)
            shutil.move(old_file, new_file)
            print("renamed file")


setup(
    name='UCI_classification',
    version='0.1',
    description='UCI classification datasets loading utilities.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/YutongWangUMich/UCI_classification',
    packages=find_packages(),
    package_data={
        'UCI_classification': ['data_lists/*.txt', 'metadata/*.csv', 'data_py.zip'],
    },
    include_package_data=True,
    cmdclass={
        'install': PostInstallCommand,
    },
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    python_requires='>=3.6',
    zip_safe=False
)
