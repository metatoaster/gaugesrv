from setuptools import setup
from setuptools import find_packages

version = '0.0.1'

classifiers = """
Development Status :: 4 - Beta
License :: OSI Approved :: GNU General Public License v2 or later (GPLv2+)
Operating System :: OS Independent
Programming Language :: JavaScript
Programming Language :: Python
Programming Language :: Python :: 3.4
Programming Language :: Python :: 3.5
Programming Language :: Python :: 3.6
Programming Language :: Python :: Implementation :: CPython
Programming Language :: Python :: Implementation :: PyPy
Topic :: Utilities
""".strip().splitlines()

package_json = {
    'dependencies': {
        'gaugeJS': '~1.3.0',
        'jquery': '~3.0.0',
    },
}

setup(
    name='gaugesrv',
    version=version,
    description='A silly service for serving gauges to browsers',
    long_description=(
        open('README.rst').read() + "\n" +
        open('CHANGES.rst').read()
    ),
    classifiers=classifiers,
    keywords='',
    author='Tommy Yu',
    author_email='y@metatoaster.com',
    url='https://github.com/metatoaster/gaugesrv',
    license='GPL',
    packages=find_packages('src', exclude=['ez_setup']),
    package_dir={'': 'src'},
    namespace_packages=[],
    zip_safe=False,
    install_requires=[
        'calmjs',
        'sanic',
    ],
    package_json=package_json,
    extras_require={
        'dev': [
            'calmjs.dev',
        ],
        'rjs': [
             'calmjs.rjs',
        ],
        'webpack': [
             'calmjs.webpack',
        ],
        'scss': [
             'calmjs.sassy[libsass]',
        ],
    },
    extras_calmjs={
        'node_modules': {
            'gaugeJS': 'gaugeJS/dist/gauge.js',
            'jquery': 'jquery/dist/jquery.js',
        },
    },
    include_package_data=True,
    python_requires='>=3.4',
    calmjs_module_registry=['calmjs.module'],
    calmjs_scss_module_registry=['calmjs.scss'],
    build_calmjs_artifacts=True,
    entry_points={
        'calmjs.module': [
            'gaugesrv = gaugesrv',
        ],
        'calmjs.scss': [
            'gaugesrv = gaugesrv',
        ],
        'calmjs.artifacts': [
            'webpack.js = calmjs.webpack.artifact:complete_webpack',
            'styles.css = calmjs.sassy.artifact:complete_css',
        ],
    },
    test_suite="gaugesrv.tests.make_suite",
)
