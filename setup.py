from setuptools import setup, find_packages

setup(
    name="comp0034-week3",
    version="1.0",
    description="Activies and apps for COMP0034 week 3",
    packages=find_packages(),
    include_package_data=True,  # automatically install any data files found
    install_requires=[
        "dash",
        "pandas",
        "dash-bootstrap-components",
        "plotly",
        "colorlover",
    ],
)
