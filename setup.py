import distutils.core
import setuptools

distutils.core.setup(
    name="tmdb",
    version="0.0.1",
    packages=["tmdb"],
    install_requires=['requests>=0.11.1', 'fuzzywuzzy==0.2'],
)
