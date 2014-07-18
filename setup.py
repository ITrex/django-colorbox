from setuptools import setup

'''Django package for jquery-colorbox:
A lightweight customizable lightbox plugin for jQuery'''

setup(
    name='django-colorbox',
    version='1.5.10-r1',
    url='https://github.com/renat2017/django-colorbox',
    description=locals()['__doc__'],
    author='Jack Moore',
    maintainer='Renat Galimov',
    maintainer_email='renat2017@gmail.com',
    license='MIT License',
    keywords=['django', 'jquery', 'lightbox',
              'staticfiles', 'overlay', 'image'],
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
    zip_safe=False,
    package_data={
        'django_colorbox': [
            'static/js/django_colorbox/*.js',
            'static/js/django_colorbox/i18n/*.js'
        ]
    },
    install_requires=(
        'Django'
    )

)
