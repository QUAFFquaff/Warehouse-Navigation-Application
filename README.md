Here is the code for our Warehouse system.

version: alpha

### set up  
Based on python and pyqt.  
version:  
python: 3.6 +  
pyqt:
-------------------
**Packages**: 

anaconda3  
Python 3.8  
PyQt5 5.15.1
PyQt5-tools  
PyQtWebEngine 5.15.1 
matplotlib 3.3.2
numpy  
---------------------


### file description  

obj file saves all the classes such as Workers, Products etc.  

data file shows all the data such as the information of the products and the path(the graph)  

UI file shows ui controllers, qt_designer are the files build GUI  

main.py is the file should run  

----------------------------------  
## Bug report  
------------------------------------  
10/29  
load_data function in main_window:  
if the path is None , system will crash. 

10/30  
the font size in the picture is not clear.
and it may looks weird when generate path cause there is a new node (start node) added into the graph.   
