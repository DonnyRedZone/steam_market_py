from setuptools import setup , find_packages

def readme():
    with open('README.md') as f:
        return f.read()

setup(name='Steam Market Py',
      version='0.0.3',
      description='Allows you to easily interact with Steam Market',
      long_description=readme(),
      long_description_content_type='text/markdown',
      keywords = 'Steam Market API Python',
      url='http://github.com/DonnyRedZone/steam_market_py',
      author='Donny',
      author_email='Donovannelson99@gmail.com',
      license='MIT',
      packages=['SteamMarket'],
      package_data={
      'SteamMarket': ['cookie.ini'],
   },
      include_package_data = True,
      install_requires=[
      "requests >= 2.25.1",
      "configparser == 5.0.1",
],
      zip_safe=True)