import setuptools

setuptools.setup(
    name='mac-open-apps',
    install_requires=open('requirements.txt').read().splitlines(),
    packages=setuptools.find_packages(),
    scripts=['scripts/open-apps']
)
