import io
from setuptools import find_packages, setup

with io.open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="quati_toolkit",
    version="1.1.1-beta",
    author="Lucas Leal",
    author_email="lucas.o.a.l.zst@gmail.com",
    description="Dynamic data eng. functions to accelerate development and coding",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/lucaslealll/quati-toolkit",
    license="MIT",
    packages=find_packages(include=["quati", "quati.*"]),
    include_package_data=True,
    package_data={"quati": ["src/*"]},
    python_requires=">=3.10",
    install_requires=[
        "google-cloud-bigquery==2.34.4",
        "google-cloud-bigquery-storage==2.27.0",
        "gspread==5.5.0",
        "oauthlib==3.2.2",
        "pandas==1.3.4",
        "pandas-gbq==0.14.1",
        "requests==2.32.3",
        "selenium==4.7.2",
        "tqdm==4.67.1",
    ],
    setup_requires=["pytest-runner"],
    tests_require=["pytest==7.2.1"],
    test_suite="tests",
    keywords="quick actions toolkit functions gspread datetime gsheets email selenium cookies sleep wait",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.10",
        "Topic :: Software Development :: Libraries",
    ],
)
