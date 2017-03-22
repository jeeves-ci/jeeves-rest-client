from setuptools import setup


setup(
    zip_safe=True,
    name='jeeves-rest-client',
    version='0.1',
    author='adaml',
    author_email='adam.lavie@gmail.com',
    packages=[
        'jeeves_rest_client',
    ],
    license='LICENSE',
    description='Jeeves REST Client for executing requests against the '
                'Jeeves-Master RESTFUL Endpoint.',
    install_requires=[
        'requests',
    ]
)
