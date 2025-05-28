from setuptools import setup, find_packages

setup(
    name='portfolio_optimizer',         # 🔸 Project/package name
    version='0.1.0',                    # 🔸 Version number
    author='Thongtada (Lion) Thongsawang',                 # 🔸 Replace with your name
    description='A portfolio optimization toolkit using yfinance data',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    packages=find_packages(where='src'),  # ✅ Finds packages under src/
    package_dir={'': 'src'},              # ✅ Tells setuptools that src/ is root
    install_requires=[
        'yfinance>=0.2.36',
        'pandas',
        'numpy',
        'matplotlib',
        'scikit-learn'
    ],
    python_requires='>=3.8',
    include_package_data=True,
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
)
