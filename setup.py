import sys
import os

try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup
    from distutils.util import convert_path

    def _find_packages(where='.', exclude=()):
        """Return a list all Python packages found within directory 'where'

        'where' should be supplied as a "cross-platform" (i.e. URL-style) path; it
        will be converted to the appropriate local path syntax.  'exclude' is a
        sequence of package names to exclude; '*' can be used as a wildcard in the
        names, such that 'foo.*' will exclude all subpackages of 'foo' (but not
        'foo' itself).
        """
        out = []
        stack = [(convert_path(where), '')]
        while stack:
            where, prefix = stack.pop(0)
            for name in os.listdir(where):
                fn = os.path.join(where, name)
                if ('.' not in name and os.path.isdir(fn) and
                        os.path.isfile(os.path.join(fn, '__init__.py'))):
                    out.append(prefix+name)
                    stack.append((fn, prefix + name + '.'))
        for pat in list(exclude)+['ez_setup', 'distribute_setup']:
            from fnmatch import fnmatchcase
            out = [item for item in out if not fnmatchcase(item, pat)]
        return out

    find_packages = _find_packages
    
setup(
    name = 'uberdoc',
    version = '1.0.0',
    packages = find_packages('src'),
    description = 'Pandoc wrapper for large, multi-chapter documents.',
    author='Stephan Brosinski',
    author_email='sbrosinski@gmail.com',
    url = 'http://github.com/sbrosinski/uberdoc',
	keywords = ["pandoc", "markdown"],
    classifiers = [
        "Programming Language :: Python",
        "Development Status :: 4 - Beta",
        "Environment :: Other Environment",
        "Intended Audience :: Developers"
        ],
    package_dir={'':'src'},
    package_data={'uberdoc': ['templates/*.*', 'style/*.*', 'uberdoc.cfg']},
    include_package_data = True,
    entry_points = {
    	'console_scripts': [
    		'uberdoc = uberdoc.uberdoc:main'
    	]
    }
)