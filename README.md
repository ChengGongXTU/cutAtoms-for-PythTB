# cutAtoms-for-PythTB
A helpful library for PythTB tool.

Introduce: 
  1,This is a python's library for using PythTB version 1.7. It implements some functions, including cuting specific atoms on material's surface，and delete the effect of specific atoms.
  
  2,The function "cutAtom(list,mod)" must be used after building TB model and set hopping and on-site energy. It delete the effect of atoms which is stored in the "list", and changes the TB model which is named "mode" in function. By this way, wo can reconstruction the cell of material, and keep some atoms existing to research.
  
  3,I use this library to calculate the band stucture of surface state in 3D semimetal, but you can also use it in different way,such as 2D edge state, and 2D semimetal defects and so on. 

Usage:
  When you set the tb_model, on-site and hopping energy in PythTB, the index of atoms will be stored in some array, you can check them. For example: all atoms and hoppings are stored in tb_model._hoppings array, if you use the "cut_piece" code to build a supercell, the index of atoms will be sorted in this array.
  And then, chose the atoms' subscripts you want to delete, put the subscript of choosen atoms in a list, and input this array and TB_model'name into cutAtoms().
  Finally, the origin TB_model will be changed, and you can use it to calculate some properties. 
  
  
  
Notice that:
  It is under the terms of the GNU GPL public license, and don't include any source code of PythTB.
  
  If you have some problems or suggestions,  send it to my email: chenggong.office@foxmail.com. 
  
What is PythTB?
  “Python Tight Binding” (PythTB) code is created by the group of David Vanderbilt at Rutgers University. You can visit their web to get more information：http://www.physics.rutgers.edu/pythtb/about.html.
