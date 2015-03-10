import os
import glob
from setuptools import setup

f = open(os.path.join(os.path.dirname(__file__), 'README.md'))
readme = f.read()
f.close()

setup(
    name='DDict',
    version=0.1,
    description='A Youdao client for Linux',
    long_description=readme,
    author='lzjqsdd',
    author_email='lzj7179@163.com',
    url='http://github.com/lzjqsdd/DDict',
    py_modules=['wordutil'],
    data_files = [("/usr/share/applications/", ['DDict.desktop']),
		("/usr/share/doc/DDict",['LICENSE','README.md']),
		("/usr/share/DDict",glob.glob("cache/*.html")),
		("/usr/lib/DDict",glob.glob("*.py")),
		("/usr/share/DDict/images/icon/",['images/logo.png']),
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
	'Environment :: X11 Applications :: GTK',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
	'Topic :: Utilities'
    ],
    scripts = ['scripts/DDict'],
)
