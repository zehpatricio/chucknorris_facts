import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='chucknorrisfacts',
    version='0.0.2',
    author='José Patrício de Sousa Filho',
    author_email='jpegx100@gmail.com',
    description='Chuck Norris facts package',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/zehpatricio/chucknorris_facts',
    project_urls = {
        "Bug Tracker": "https://github.com/zehpatricio/chucknorris_facts/issues"
    },
    license='MIT',
    packages=['chucknorrisfacts'],
    install_requires=['requests'],
)