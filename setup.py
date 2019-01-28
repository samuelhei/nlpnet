from setuptools import setup
from setuptools import Extension
from Cython.Distutils import build_ext

class CustomBuildExtCommand(build_ext):
    def run(self):
        import numpy
        self.include_dirs.append(numpy.get_include())
        build_ext.run(self)

def readme():
    with open('README.rst') as f:
        text = f.read()
    return text

setup(
    name='nlpnet',
    cmdclass = {'build_ext': CustomBuildExtCommand},
    description='Neural networks for NLP tasks',
    packages=['nlpnet', 'nlpnet.pos', 'nlpnet.srl', 'nlpnet.parse'],
    ext_modules=[
        Extension(
            "nlpnet.network",
            ["nlpnet/network.c"]
        )
    ],
    scripts=[
        'bin/nlpnet-tag.py',
        'bin/nlpnet-train.py',
        'bin/nlpnet-test.py',
        'bin/nlpnet-load-embeddings.py'
    ],
    install_requires=[
        'numpy>=1.16',
        'nltk>=3.4',
        'six>=1.10',
        'h5py>=2.9.0'
    ],
    license='MIT',
    version='1.2.3',
    author='Erick Fonseca',
    author_email='erickrfonseca@gmail.com',
    url='http://nilc.icmc.usp.br/nlpnet',
    long_description=readme()
)
