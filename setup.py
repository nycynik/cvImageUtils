from setuptools import setup

setup(name='cvImageUtils',
      version='0.1',
      description='Simple Open CV Library of utilities',
      url='http://github.com:nycynik/cvImageUtils',
      author='MikeLynchGames',
      author_email='nycynik@gmail.com',
      license='MIT',
      install_requires=[
            'numpy',
            'cv2',
      ],
      packages=['cvImageUtils'],
      zip_safe=False)
