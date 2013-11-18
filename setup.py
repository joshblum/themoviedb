import distutils.core
import setuptools

distutils.core.setup(
    name="tmdb",
    packages=["tmdb"],
    install_requires=['requests>=0.11.1'],
)
