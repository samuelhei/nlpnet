from setuptools import setup
from setuptools import Extension

def ext_modules():
    import numpy

    # define the extension module
    cos_module_np = Extension("nlpnet.network",
                              sources=[".","nlpnet/network.c"],

                              include_dirs=[numpy.get_include()])
    return [cos_module_np]

def readme():
    with open('README.rst') as f:
        text = f.read()
    return text

setup(
    name='nlpnet',
    description='Neural networks for NLP tasks',
    packages=['nlpnet', 'nlpnet.pos', 'nlpnet.srl', 'nlpnet.parse'],
    #ext_modules=ext_modules(),
    scripts=[
        'bin/nlpnet-tag.py',
        'bin/nlpnet-train.py',
        'bin/nlpnet-test.py',
        'bin/nlpnet-load-embeddings.py'
    ],
    install_requires=[
        'numpy',
        'nltk>=3.2.2',
        'six>=1.10',
        'h5py>=2.8.0rc1'
    ],
    setup_requires=['numpy'],
    license='MIT',
    version='1.2.3',
    author='Erick Fonseca',
    author_email='erickrfonseca@gmail.com',
    url='http://nilc.icmc.usp.br/nlpnet',
    long_description=readme()
)