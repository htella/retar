retar
=====

A one off utility for re-taring the archive produced when building ZooKeeper.

The tar file produced after compiling, zookeeper-3.3.4.tar.gz, needs to be untared and retared because as it is everything inside the archive is in a single folder zookeeper-3.3.4/. And the cloudformation template for ZooKeeper is setup to expect everything within zookeeper-3.3.4/ to just be at the top level of the archive.

The utility does that re-taring for you. 

usage
=====

python retar.py something.tar.gz


this will produce two files 

something.tar.gz -- the newly re-tared file
something.tar.gz.orig -- the original tar fed into the utility

