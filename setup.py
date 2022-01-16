from pathlib import Path
from setuptools import find_packages, setup

readme = Path(__file__).parent / 'README.md'

setup(name='pytcha',
      version='0.0.1-dev',
      description='A python package to generate a captcha for various python web applications',
      long_description=readme.read_text(),
      long_description_content_type='text/markdown',
      url='https://github.com/jeremystevens/pytcha',
      doc_url='https://readthedocs.org/projects/pytcha/',
      author='Jeremy Stevens',
      author_email='jeremiahstevens@gmail.com',
      maintainer='jeremystevens',
      license='GPL-3.0',
      license_file='LICENSE',
      packages=find_packages(),
      scripts=['pytcha/pytcha.py'],
      include_package_data=True,
      classifiers=[
          'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
          'Natural Language :: English',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.7',
          'Programming Language :: Python :: 3.8',
          'Programming Language :: Python :: 3.9',
      ],
      python_requires='>=3.7',
      install_requires=['pillow','rstr'],
      zip_safe=False)
