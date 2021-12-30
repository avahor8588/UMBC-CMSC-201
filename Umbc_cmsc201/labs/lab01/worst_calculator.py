Last login: Wed Sep  8 19:25:27 on ttys000
shamilvahora@Aamils-laptop ~ % ssh aamilv1@gl.umbc.edu
WARNING: UNAUTHORIZED ACCESS to this computer is in violation of Criminal Law
         Article section 8-606 and 7-302 of the Annotated Code of MD.

NOTICE:  This system is for the use of authorized users only. Individuals using
         this computer system without authority, or in excess of their authority
         , are subject to having all of their activities on this system
         monitored and recorded by system personnel.

aamilv1@gl.umbc.edu's password: 

UMBC Division of Information Technology                    http://doit.umbc.edu/
--------------------------------------------------------------------------------
If you have any questions or problems regarding these systems, please call the
DoIT Technology Support Center at 410-455-3838, or submit your request on the
web by visiting http://my.umbc.edu/help/request

Remember that the Division of Information Technology will never ask for your
password. Do NOT give out this information under any circumstances.
--------------------------------------------------------------------------------

Last login: Wed Sep  8 19:26:14 2021 from 130.85.248.255
[aamilv1@linux6 ~] cd cmsc201
[aamilv1@linux6 ~/cmsc201] cd labs
[aamilv1@linux6 labs] cd lab01
[aamilv1@linux6 lab01] emacs worst_calculator.py
[aamilv1@linux6 lab01] python3 worst_calculator.py
enter integer 1: 1
eneter integer 2: 2
the sume of the integers 1 and 2 is 3
enter float 1: 3
enter float 2: 4
enter float 3: 5
the product of the floats  3.0 4.0 and  5.0 is 60.0
[aamilv1@linux6 lab01] emacs worst_calculator.py
[aamilv1@linux6 lab01] python3 worst_calculator.py
enter integer 1: 1
eneter integer 2: 2
the sume of the integers 1 and 2 is 3
enter float 1: 1
enter float 2: 2
enter float 3: 3
the product of the floats 1.0 2.0 and 3.0 is 6.0
[aamilv1@linux6 lab01] emacs worst_calculator.py
[aamilv1@linux6 lab01] python3 worst_calculator.py
enter integer 1: 1
eneter integer 2: 2
the sume of the integers 1 and 2 is 3
enter float 1: 1
enter float 2: 2
enter float 3: 3
the product of the floats 1.0 , 2.0 , and 3.0 is 6.0
[aamilv1@linux6 lab01] emacs worst_calculator.py

File Edit Options Buffers Tools Python Help                                     
"""                                                                             
File:         worst_calculator.py                                               
Author:       aamil vahora                                                      
Date:         9/07/2020                                                         
Section:      42                                                                
E-mail:       aamilv1@umbc.edu                                                  
Description:  use integers and floats to create programs to add and multiply se\
ts of numbers through python, to create expressions.                            
"""

num1 = int(input("enter integer 1: "))
num2 = int(input('eneter integer 2: '))
output = num1 + num2
print("the sume of the integers", num1, "and", num2, "is" ,output)

num1 = float(input("enter float 1: "))
num2 = float(input("enter float 2: "))
num3 = float(input("enter float 3: "))
output = num1 * num2 * num3
print("the product of the floats", num1,",",  num2,",", "and", num3, "is", outp\
ut)
-UU-:----F1  worst_calculator.py   Top L1     (Python ElDoc) -------------------
Can’t guess python-indent-offset, using defaults: 4
