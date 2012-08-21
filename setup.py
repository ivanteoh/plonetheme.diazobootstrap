from setuptools import setup, find_packages

version = '2.1.0'

long_description = (
    open('README.md').read()
    + '\n' +
    'Contributors\n'
    '============\n'
    + '\n' +
    open('CONTRIBUTORS.md').read()
    + '\n' +
    open('CHANGES.md').read()
    + '\n')

setup(name='plonetheme.diazobootstrap',
    version=version,
    description="Diazo Theme based on Twitter's diazobootstrap",
    long_description=long_description,
    # Get more strings from
    # http://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Framework :: Plone',
        'Programming Language :: Python',
        ],
    keywords='diazo plone theme',
    author='Ivan Teoh',
    author_email='contact@ivanteoh.com',
    url='http://svn.plone.org/svn/collective/',
    license='GPL',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    namespace_packages=['plonetheme'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'setuptools',
        # -*- Extra requirements: -*-
        'plone.app.theming',
    ],
    extras_require={'test': ['plone.app.testing']},
    entry_points="""
    # -*- Entry points: -*-
    [z3c.autoinclude.plugin]
    target = plone
    """,
    )
