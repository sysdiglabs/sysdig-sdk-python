from setuptools import setup, find_packages

setup(
    name="sdcclient",
    version="0.13.1",
    description="Python client for Sysdig Cloud",
    url="http://github.com/sysdiglabs/sysdig-sdk-python",
    author="Sysdig Inc.",
    author_email="info@sysdig.com",
    classifiers=[
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
    ],
    packages=find_packages(
        exclude=["contrib", "doc", "specs", "tests", "examples", "utils"]
    ),
    python_requires=">=3.8, <4",
    install_requires=[
        "certifi>=2020.6.20",
        "chardet>=3.0.4",
        "idna>=2.10; python_version >= '2.7' and python_version not in '3.0, 3.1, 3.2, 3.3'",
        "pyaml>=20.4.0",
        "pyyaml>=5.3.1",
        "requests>=2.23.0",
        "requests-toolbelt>=0.9.1",
        "tatsu>=5.5.0",
        "urllib3>=1.25.8",
    ],
    extras_require={"dev": []},
    project_urls={
        "Bug Reports": "https://github.com/sysdiglabs/sysdig-sdk-python/issues",
        "Source": "https://github.com/sysdiglabs/sysdig-sdk-python/",
    },
)
