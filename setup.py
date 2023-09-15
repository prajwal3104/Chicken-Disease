import setuptools

with open("README.md", "r") as fh:
    log_description = fh.read()

    __version__ = "0.0.1"

    REPONAME = "Chicken-Disease"
    AUTHOR_USER_NAME = "prajwal3104"
    SRC_REPO = "cnnClassifier"
    AUTHOR_EMAIL = "prajwal0836@gmail.com"

    setuptools.setup(
        name=f"{REPONAME}-{SRC_REPO}",
        version=__version__,
        author=f"{AUTHOR_USER_NAME}",
        author_email=f"{AUTHOR_EMAIL}",
        description="A small example package",
        long_description=log_description,
        long_description_content_type="text/markdown",
        url=f"https://github.com/{AUTHOR_USER_NAME}/{REPONAME}",
        project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPONAME}/issues",
        },
        package_dir={"": "src"},
        packages=setuptools.find_packages(where="src")
    )
