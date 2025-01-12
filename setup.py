from setuptools import setup, find_packages

setup(
    name="uconndatascienceclub",
    version="0.1.0",
    description="UConn Data Science Club's personal Python package; used for data science & ML resources",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="UConn Data Science Club",
    author_email="uconndatascience@gmail.com",
    url="https://github.com/JadenAstle/uconndatascienceclub",
    packages=find_packages(),
    install_requires=[
        "numpy",
        "pandas",
        "matplotlib",
        "sklearn" 
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    include_package_data=True, 
    package_data={"uconndatascienceclub": ["datasets/*.csv"]},
)
