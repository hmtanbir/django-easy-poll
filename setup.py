from setuptools import setup, find_packages

# Dynamically calculate the version based on django.VERSION.
version = __import__('poll').get_version()

setup(
    name='django-easy-poll',
    version=version,
    description='Django easy poll application',
    author='Hasan Mohammad Tanbir',
    author_email='tanbir2025@gmail.com',
    url='https://github.com/hmtanbir/django-easy-poll',
    download_url='https://github.com/hmtanbir/django-easy-poll/archive/master.zip',
    packages=find_packages(),
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ],
    include_package_data=True,
)
