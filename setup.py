import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="random_user_agent",
    version="0.0.3",
    author="Luqman Ud Din Muhammad",
    author_email="luqmanuddinm@gmail.com",
    description="A package to get random user agents based filters provided by user",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/LuqmanUdDinMuhammad/random-user-agent/",
    packages=setuptools.find_packages(),
    license='MIT',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        "scrapy",
    ],
)
