from distutils.core import setup
ficheiros=["*"]
setup(name="proyecto",
      version="0.01",
      description="proyecto",
      long_description="descripcion larga",
      author="brian",
      author_email="briandistribuciones@hotmail.com",
      url="www.google.com",
      keywords="proba,distribucion",
      platforms="linux,mac",
      packages=["paquete"],
      package_data={"paquete":ficheiros},
      scripts=["lanzador"]
      )

