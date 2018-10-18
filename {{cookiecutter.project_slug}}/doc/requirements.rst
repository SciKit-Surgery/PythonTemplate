.. highlight:: shell

===============================================
Requirements for {{ cookiecutter.project_name }}
===============================================

{{ cookiecutter.project_name }} forms part of SNAPPY, a collection of software
developed by the Wellcome EPSRC Centre for Surgical Sciences and Interventions. 
SNAPPY is being developed to support faster translation of advanced surgical 
research from the bench to the bed side. SNAPPY does this by supporting and
encouraging the development of small but well engineered software components that 
can;
* be used and developed during early stage research, and;
* easily be built into high quality clinical applications that be appropriately certified in less than 2 years.

It is important therefore that the individual of components of SNAPPY 
i.e. {{ cookiecutter.project_name }} are well engineered. More information on this
process can be found is SNAPPY.rst. Software engineering begins with thinking about and 
writing down what it is the software is supposed to do to what. These are the known 
as the software requirements. The table below lists the minimum requirements of 
any SNAPPY module, and where they are tested. 
Requirements should be necessary, verifiable, and attainable. 

Take a little time before you start coding to think about what you want your
software to achieve, and write it down here. A badly written requirement is better
than an unwritten requirement, and requirements can always be changed as the 
software evolves. Ideally requirements should have corresponding unit tests, which 
can be listed below, however it is better to write the requirement and not test it 
than to not write it at all.

Requirements
~~~~~~~~~~~~
+--------------------------+--------------------------------------------------------------------------------+
| ::         |                                                        |                                     |
|            |                                                        |                                     |
|    ID      |  Description                                           |  Unit test ?                        |
+--------------------------+--------------------------------------------------------------------------------+
| ::         |                                                        |                                     |
|            |                                                        |                                     |
|    0000    |  -h flag returns a help page                           |  Unit test ?                        |
+--------------------------+--------------------------------------------------------------------------------+
| ::         |                                                        |                                     |
|            |                                                        |                                     |
|    0001    |  -v flag returns version number                        |  Unit test ?                        |
+--------------------------+--------------------------------------------------------------------------------+



