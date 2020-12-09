Here is the code for our Warehouse system.

**If you have the virtual environment [venv](./venv) under this folder and using
windows, use [run.bat](./run.bat) to excute the program.**

### set up  
Based on python and pyqt.  
version:  
python: 3.6 +  
run the following commands to install the packages:
```bash
$ pip install PyQt5==5.15.1
$ pip install PyQt5-tools 
$ pip install numpy
$ pip install PyQtWebEngine==5.15.1 
$ pip install matplotlib==3.3.2
$ pip install pyecharts==1.9.0
```


To run the program, use 
```bash
$ python main.py 
```
to excute it. 

Unfinished orders will be stored in data/unfinished_orders.txt 
and it will be loaded into the system once the graph is loaded.
If you don't want load previous orders just clear the content in
that file.
-------------------
**Packages**: 
 
Python 3.8  
PyQt5 5.15.1

PyQt5-tools  
PyQtWebEngine 5.15.1 

pyecharts 1.9.0

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
if the path is None, system will crash. 

10/30  
the font size in the picture is not clear.
and it may looks weird when generate path cause there is a new node (start node) added into the graph.   
