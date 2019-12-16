from distutils.core import setup

setup(
    name='auto-ysoserial',
    author="Raúl Sampedro",
    author_email="rsrdesarrollo@gmail.com",
    version='0.0.1',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    scripts=["auto-ysoserial"],
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    install_requires=["requests"]
)
