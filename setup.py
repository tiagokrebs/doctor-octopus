import setuptools
with open("README.md", "r") as fh:
    long_description = fh.read()
setuptools.setup(
     name='octo',
     version='0.1',
     scripts=['octo'] ,
     author="Tiago Krebs",
     author_email="tiago.krebs@azion.com",
     description="A toil tasks automation tool",
     long_description=long_description,
   long_description_content_type="text/markdown",
     url="https://github.com/tiagorkrebs/doctor-octopus",
     packages=setuptools.find_packages(),
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
 )