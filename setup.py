from setuptools import setup, find_packages

setup(name="django-simple-cities",
           version="0.1",
           description="Simple City DB for Django, includes Ajax select filtering.",
           author="David Novakovic <dpn@dpn.name>",
           packages=find_packages(),
           include_package_data=True,
)