from setuptools import setup

setup(
    name='django-colorbox',
    version='1.5.10',
    url='https://github.com/renat2017/django-colorbox',
    description='Django package for jquery-colorbox: A lightweight customizable lightbox plugin for jQuery',
    author='Jack Moore',
    maintainer='Renat Galimov',
    maintainer_email='renat2017@gmail.com',
    license='MIT',
    keywords=['django', 'jquery', 'lightbox', 'staticfiles', 'overlay', 'image'],
    platforms='any',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Utilities',
    ],
    packages=['django_colorbox'],
    package_data={'django_colorbox': ['static/js/django_colorbox/*.js', 'static/js/django_colorbox/i18n/*.js']}
)
