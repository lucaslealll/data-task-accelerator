import io

from setuptools import find_packages, setup

with io.open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    author="Lucas Leal",
    author_email="lucas.o.a.l.zst@gmail.com",
    description="Dynamic data eng. functions to accelerate development and coding",
    include_package_data=True,
    keywords="data task accelerator functions gspread datetime gsheets email selenium cookies sleep wait",
    license="MIT",
    long_description=("README.md"),
    long_description=long_description,
    long_description_content_type="text/markdown",
    name="data_task_accelerator",
    # namespace_packages=("scripts",),
    package_data={"dta": [".src/*"]},
    packages=find_packages(exclude=("tests*", "system_tests*")),
    packages=find_packages(include=["data_task_accelerator"]),
    python_requires=">=3.10",
    setup_requires=["pytest-runner"],
    test_suite="tests",
    tests_require=["pytest==7.2.1"],
    url="https://github.com/lucasoal/data-task-accelerator",
    version="1.0.0",
    install_requires=[
        "google-api-core==2.22.0",
        "google-auth==2.35.0",
        "google-auth-oauthlib==1.2.1",
        "google-cloud-bigquery==2.34.4",
        "google-cloud-bigquery-storage==2.27.0",
        "google-cloud-core==2.4.1",
        "google-crc32c==1.6.0",
        "google-resumable-media==2.7.2",
        "googleapis-common-protos==1.65.0",
        "gspread==5.5.0",
        "ipykernel==6.29.5",
        "jupyter_client==8.6.3",
        "jupyter_core==5.7.2",
        "nest-asyncio==1.6.0",
        "oauthlib==3.2.2",
        "pandas==1.3.4",
        "pandas-gbq==0.14.1",
        "requests==2.32.3",
        "selenium==4.7.2",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
    ],
)
