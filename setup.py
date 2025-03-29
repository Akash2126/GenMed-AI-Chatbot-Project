from setuptools import setup, find_packages

setup(
    name='GenMed-AI-Chatbot',
    version='0.1',
    author='Akash Kumar Tiwari',
    author_email='your_email@example.com',
    description='A medical AI chatbot for healthcare assistance',
    packages=find_packages(),
    install_requires=[
        'flask',  # Add the required dependencies here
        'requests',
        'numpy',
        'pandas'
    ],
)
