import setuptools

setuptools.setup(
    name="myproject",
    version="1.0.0",
    author="Your Name",
    author_email="your@email.com",
    description="My project description",
    packages=[""],
    py_modules=["main", "symmetric_encryption", "asymmetric_encryption", "homomorphic_encryption", "preprocessing", "utils"],
    install_requires=[
        "numpy",
        "scipy",
        "pandas",
        "sklearn",
        "pycryptodome"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
