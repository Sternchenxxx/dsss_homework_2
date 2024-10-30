from setuptools import setup, find_packages

setup(
    name="math_quiz",
    version="0.1",
    packages=find_packages(),
    install_requires=[],
    entry_points={
        "console_scripts": [
            "math_quiz=math_quiz.math_quiz:main",  
        ]
    },
    author="Yiqi Li",
    author_email="xiaoxiao_0305@126.com",
    description="math quiz",
    license="MIT",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Sternchenxxx/dsss_homework_2",
)
