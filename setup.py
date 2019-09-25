from setuptools import setup

setup(name='sdcclient',
      version='0.10.0-dev',
      description='Python client for Sysdig Cloud',
      url='http://github.com/draios/python-sdc-client',
      author='sysdig Inc.',
      author_email='info@sysdig.com',
      license='MIT',
      packages=['sdcclient'],
      install_requires=['requests', 'pyaml'],
      zip_safe=False)
