import setuptools

setuptools.setup(
    name="sci-api-req",
    version="0.1.1",
    author="miki164",
    author_email="miki3867@gmail.com",
    description="Provider for scientific APIs",
    long_description="Library providing easy way to use NASA and other organisation APIs(In future)",
    url="https://github.com/miki164/sci-api-req",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        'requests'
    ]
)