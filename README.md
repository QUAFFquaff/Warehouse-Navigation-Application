Here is the code for our Warehouse system.

version: alpha

### set up  
Based on python and pyqt.  
version:  
python: 3.6 +  
pyqt:

### file description  

obj file saves all the classes such as Workers, Products etc.  


----------------------------------  
##Bug report  
------------------------------------  
10/29  
load_data function in main_window:  
if the path is None , system will crash.