# Mach Calculator App with pytkinter

This is a GUI App which lets you calculate the maximum inlet mach in a converging entrained flow corresponding to choked flow.
The GUI is build on pytkinter and the complex 6th degree equation is solved using python numpy.
As inputs the user enters the diameter of the tube and the object inside the tube.
The inputs are then used to create an instance of solve class wherein they are fed into the following equation to calculate possible inlet values. 

**NOTE:** The fluid is hard coded as AIR into the solver!!


![Equation](https://latex.codecogs.com/gif.latex?%5Cfrac%7BA_1%7D%7BA_2%7D%3D%5Cfrac%7BM_2%7D%7BM_1%7D%5Ccdot%20%5Cfrac%7B1&plus;%5Cfrac%7B%5CGamma%20-1%7D%7B2%7DM_1%5E2%7D%7B1&plus;%5Cfrac%7B%5CGamma%20-1%7D%7B2%7DM_2%5E2%7D%5E%7B%5Cfrac%7B%5CGamma&plus;1%7D%7B2%28%5CGamma-1%29%7D%7D)


Here, A_1 = C.S area of tube and A_2 = C.S area of throat;

**Disclaimer:** No code has been implemented at the moment to explain the results intuitively. But the general idea stems from compressible flow physics such as isentropic limits and choking. 

*Among the 6 roots we get, if all are complex (i.e they have non zero imaginary terms) then it means that the area ratio between tube and object is not sufficient/too small for the flow to reach Mach 1 (maximum mass flow rate) at throat (provided Mach at inlet is <1) thus rendering the solution a non-realistic or impossible one.*

For possible cases of inlet Mach and Area ratios, the solution should output two perfectly real numbers (usually 5th and 6th ones in the List Tab) corresponding to the isentropic limits.

**Running the App**

Run the file **paanduv_main.py** from your terminal/CMD. 

**Preview**

**Home Screen**


![home_screen](https://user-images.githubusercontent.com/31100400/151651620-e56ab3e1-3472-4c2d-9ea0-c61f89e97be1.png)


**Calculator Screen**


![calculator_tab](https://user-images.githubusercontent.com/31100400/151651889-c979ca8e-9dec-458b-a32d-4ba8b5714394.png)

**Results**

![results](https://user-images.githubusercontent.com/31100400/151651900-e0fdd2ce-62a3-432e-b160-156c6643aec9.png)


**Modules**

The tkinter is already installed with latest versions of python; apart from that some of the other modules you may need are:

---> Pillow for Image and ImageTk
---> tkinter.font
---> tkinter messagebox
---> python numpy

If these are not installed you may have to install them using pip install command from your terminal.

Happy Coding !!!
