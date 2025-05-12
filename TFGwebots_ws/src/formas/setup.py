from setuptools import setup

setup(
    name='formas',
    version='0.0.0',
    packages=['formas'],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/formas']),
        ('share/formas', ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='echedey',
    maintainer_email='ahechedey@gmail.com',
    description='Paquete para dibujar formas con el turtlebot4 y obtener datos de sus sensores y actuadores',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'cuadrado = formas.cuadrado:main',
            'sala = formas.sala_completa:main',
        ],
    },
)
