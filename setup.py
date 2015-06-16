'''
pytz setup script
'''

try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup


me = 'Abhinav Kotak'
memail = 'in.abhi9@gmail.com'

packages = ['djangofuture.']

setup(
    name='djangofuture',
    version='0.0.1',
    zip_safe=True,
    description='Cherry-picked feature to use with django 1.8',
    author=me,
    author_email=memail,
    maintainer=me,
    maintainer_email=memail,
    url='https://github.com/inabhi9/djangofuture',
    license='MIT',
    keywords=['djangofuture'],
    packages=find_packages(),
    platforms=['Independant'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)