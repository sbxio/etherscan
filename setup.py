import setuptools

with open("README.md", "r") as readme:
    long_description = readme.read()

setuptools.setup(
    name="etherscan",
    version="0.1.0",
    author="sbx",
    author_email="sbx.softdev@gmail.com",
    description="etherscan api client",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/sbxio/etherscan",
    packages=setuptools.find_packages("src"),
    package_dir={"": "src"},
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
    ],
    python_requires=">=3.6",
    install_requires=[
        "requests==2.31.0",
    ],
)
