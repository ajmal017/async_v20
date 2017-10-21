from setuptools import setup, find_packages
version = '1.1.1a1'

setup(name='async_v20',
      version=version,
      description="Asynchronous wrapper for OANDA's v20 REST API",
      long_description="Asynchronous wrapper for OANDA's v20 REST API. Client methods return coroutines that can be run"
                       "inside an asyncio event loop",
      author='James Peter Schinner',
      author_email='james.peter.schinner@gmail.com',
      url='https://github.com/jamespeterschinner/async_v20',
      license='MIT',
      packages=find_packages(),
      install_requires=['aiohttp>=2.2.5',
                        'pytest>=3.2.2',
                        'ujson==1.35',
                        'yarl==0.12.0',
                        'inflection==0.3.1',
                        'pandas==0.20.3'],
      classifiers=['Programming Language :: Python :: 3.6', 'Development Status :: 3 - Alpha',
                   'Framework :: AsyncIO',
                   'Intended Audience :: Developers',
                   'License :: OSI Approved :: MIT License',
                   'Operating System :: OS Independent',
                   'Topic :: Internet :: WWW/HTTP :: Session'],
      keywords='algorithmic trading oanda v20 REST asyncio ',
      )
