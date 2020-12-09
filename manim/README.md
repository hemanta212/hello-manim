# Manim-Bloomn

A manim fork incorporating customization of the library for work in bloom nepal animation videos

This fork adds
* A custom pi_creature svg.
* Integration with chanim (chemistry animation for manim)

## Installation
  The installation is same as original [manim repo](https://github.com/3b1b/manim).

  Incase you already have installed 3b1b/manim. Clone this repo, navigate to it and 

  ```
  $ python setup.py install
  ```

## Chemfig/Chanim Usage

  ```
  from manimlib.imports import *
  
  class Test(Scene):
    def construct(self)
      water_mol = ChemObject("H_2O")
      self.play(Write(water_mol)) 
  ```

  You can put any valid chemfig command inside ChemObject. 
  The additional chemistry related files are;

  - manimlib/chem_objects.py
  - manimlib/compounds.py 

  View additional info in [chanim repo:](https://github.com/raghavg123/chanim)
