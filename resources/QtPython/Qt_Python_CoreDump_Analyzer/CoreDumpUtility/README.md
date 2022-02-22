# Description - What is it for ?

This project is to build coredump analysis utility - a GUI based. In general, some one has to keep typing command in the terminal.
In certain situations, this can be quite cumbersome. This project is to cater that need. I feel that the customer for this project will be
the integration engineer or test engineer. They can just run the bt on the corefile to tell the developer on the problem. This is helpful to give more
insight on the problem reported.

*What is it supporting currently?*
Currently, we are supporting X86 and MIPS.

*What it can support?*
We would like it to extend so that it can support other architecture also. 

--------------------------------------------------
## Architecture 

The GUI is developed in Qt - Qt designer. In order to change something on the GUI - open the qt creator in linux/mac or windows.
Next, browse the file XPlatformCoreDump.pro , then click the button Edit on the left hand pane of the Qt Creator IDE. This should load the entire
project in the Qt Creator designer.

Next, convert the qt created gui - UI form in the python code.
In the command line - do the following.
$pyuic4 coredumputilframe.ui > coredumputilframe.py

[note] - You need to install certain packages to make GUI using Python. In UBUNTU, these packages can be installed by

* sudo pip install pyqt
* sudo apt-get install qt4-designer
* sudo apt-get install pyqt4-dev-tools
* sudo apt-get install python-kde4


You should never manually changed the file - coredumputilframe.py. This is an auto-generated file. 


*Main file -- entry point*

Main Python file - our workspace to add logic to the GUI.

The main python file is mainXCoreUtility.py. 

*Expectation ---*

I expect this file to get updated everytime, we add or modify the python logic. 
If we want to add some rich functionalites - add-ons, then we can bifurcate the functionality into other files. 


*Code Ethics -*


It is better, if we keep the button prefix as 'b'. The label prefix as 'l'. We can stick with this nomenclature for other type of widgets
too. 

Try to improve the code. Add comments wherever possible.

Never use print directly instead use dbgLog function. In the release build, we can change the dbgLog to pass rather than printing the message.

Desire - To use python in object oriented fashion. 

The GIT Tutorial to modify the files in this project are available in the file -

gitReadme.txt

*How to deploy this Application?*

Firstly, install pyinstaller - 

In ubuntu, you can install pyinstaller with the help of pip

sudo pip install PyInstaller

Next, in order to deploy this product - do the following.

$pyinstaller <mainPythonProgramScript> 

This will create a build directory, which will have the entire required library and the program.









