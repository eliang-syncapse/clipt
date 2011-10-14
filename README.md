Clipt
=====

usage: clipt.py [-h] {read,write,list,delete} [key] [value]

Description
-----------
Save and retrieve text snippets from the command line. I was inspired by [Boom](https://github.com/holman/boom)

__Uses__

* fun
* helping out with deploys (store shared text snippets, host names, commands)
* ???

__Requirements__

* Python 3 (along with 2to3)
* Nose (and coverage plugin) to run unittests and code coverage

__Notes__

* The local storage writer uses sqlite
* Thrift interface for remote storage (not implemented)
* Thrift doesn't support Python 3 so 2to3 is required (Makefile takes care of this)

__Configuration__

* Standard ini-file configuration, ~/.clipt/config
* [main] section:
    * 'storage' => Which storage engine to use : {local, remote}
* [local] section:
    * 'database' => Location of sqlite database : defaults to ~/.clipt/data
