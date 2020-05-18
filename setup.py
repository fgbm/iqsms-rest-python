import setuptools

with open('README.md', 'r', encoding='utf-8') as fh:
    long_description = fh.read()

setuptools.setup(
    name='iqsms-rest',
    version='0.0.2',
    author='Chmelyuk Vladislav',
    author_email='neimp@yandex.ru',
    description='Модуль для работы с REST API смс-шлюза iqsms.ru (СМС Дисконт)',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/fgbm/iqsms-rest-python',
    packages=setuptools.find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    install_requires=['requests']
)
