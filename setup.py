from setuptools import setup

setup(name='sdcclient',
      version='0.1',
      description='Python client for Sysdig Cloud',
      url='http://github.com/storborg/funniest',
      author='sysdig Inc.',
      author_email='info@sysdig.com',
      license='MIT',
      packages=['sdcclient'],
      install_requires=['requests'],
      zip_safe=False)