from setuptools import find_packages, setup

setup(
    name="pplay-pygame",
    packages=find_packages(include=["src/pplay-pygame"]),
    version="2.0.0",
    description="A simple game abstraction framework to pygame",
    author=(
        "Prof. Esteban Clua, "
        "Prof. Anselmo Montenegro, "
        "Gabriel Saldanha, "
        "Adônis Gasiglia, "
        "Yuri Nogueira"
    ),
    author_email=(
        "esteban@ic.uff.br, "
        "anselmo@ic.uff.br, "
        "gabrielcrsaldanha@gmail.com, "
        "adonisgasiglia@id.uff.br, "
        "yurinogueira@id.uff.br"
    ),
    license="GPL-2",
    install_requires=["pygame>=2.1.2"],
    setup_requires=["pytest-runner>=6.0.0"],
    tests_require=["pytest>=7.1.2"],
)
