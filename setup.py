import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="yams", # Replace with your own username
    version="0.0.1-experimental",
    author="L. Pham-Trong, S. Vallette",
    author_email="spam@lucasanss.xyz",
    description="YAMS (Yet Another Messaging System) is a modular and extensible messaging system",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/toto112358/YAMS",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
        "Operating System :: OS Independent",
    ],
      install_requires=[
          'twofish',
      ],
    python_requires='>=3.6',
)
