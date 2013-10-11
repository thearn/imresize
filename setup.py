from setuptools import setup, find_packages

setup(name='imresize',
      version='0.1',
      install_requires=['numpy', 'scipy'],
      description="Replacement for scipy.misc.imresize that does not require PIL",
      author='Tristan Hearn',
      author_email='tristanhearn@gmail.com',
      url='https://github.com/thearn/imresize',
      license='Apache 2.0',
      packages=['imresize']
      )
