

# ---------------------------------------------------------
# Copyright (c) 2026 Mark. All rights reserved.
# Unauthorized copying of this file, via any medium, is
# strictly prohibited. Written by Mark (iamnothimbutwe) on Github.
# ---------------------------------------------------------

from setuptools import setup, find_packages
#import sys
#import astlo
#from packaging import version


#try:
 #   import astlo
  #  from packaging import version
   # 
    #required_version = version.parse("v5.62.53")
  #  installed_version = version.parse(astlo.__version__)
#    
 #   if installed_version < required_version:
  #      print("\n❌🚫 ERROR: Solsynder requires astlo >= 5.62.53")
   #     print(f"   You have astlo {astlo.__version__} installed.")
    #    print("   Please upgrade with:   pip install ¦new .whl file¦ the .whl files are available in the releases section of the public repo to astlo")
       # print("   Then try installing Solsynder again.\n")
#        sys.exit(1)
 #       
#except ImportError as r:
   # print("\n❌🚫 ERROR: Solsynder requires astlo to be installed first.")
    #print("   Please install astlo with: astlo>=5.62.53 from the public repo to astlo")
  #  print("   Then try installing Solsynder again.\n")
 #   print(f'{r}')
#    sys.exit(1)

#except Exception as e:
    # Fallback in case packaging module is missing
 #   print(f"\n⚠️🚫  Warning: Could not verify astlo version ({e})")
  #  print("   Continuing anyway...\n")
    #pass


##Normal setup##

setup(
    name="solsynder",
    version="v0.3.64",
    packages=find_packages(),
    install_requires=["plotext", "rich", "click", 'astlo>=v5.65.61'], #dont ned to add astlo here becose its handled at the top
    include_package_data=True,
    entry_points={
        "console_scripts": [
            "solsynder = synder.main:sin",
        ],
    },
    python_requires=">=3.8",
    author="@iamnothimbutwe Github and Gitlab. Macharia",
    author_email="markmacgh@gmail.com/hecateare@gmail.com",
    description="A Real-time solar system calendar that focuses on presenting the data in a readable format to the user from astlo",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/iamnothimbutwe/Solsynder",
    license="Copyright (c) 2026. All rights reserved",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: COPYRIGHT",
        "Operating System :: OS Independent",
        "Topic :: Scientific/Engeneering :: Astronomy :: Astrophysics",
    ],
)
