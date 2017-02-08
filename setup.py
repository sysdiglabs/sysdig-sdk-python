from setuptools import setup

setup(name='sdcclient',
      version='0.5.0',
      description='Python client for Sysdig Cloud',
      url='http://github.com/draios/python-sdc-client',
      author='sysdig Inc.',
      author_email='info@sysdig.com',
      license='MIT',
      packages=['sdcclient'],
      install_requires=['requests'],
      zip_safe=False)
