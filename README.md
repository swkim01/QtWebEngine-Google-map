# QtWebEngine-Google-map
A sample QtWebEngine Based project to render a google map


### How to build

```sh
$ git clone https://github.com/Vinodsathyaseelan/QtWebEngine-Google-map.git
$ cd QtWebEngine-Google-map 
```
1. C++ / qmake
```sh
$ qmake Google-map.pro 
$ make
```
2. python
```sh
$ sudo apt install pyqt5-dev-tools
$ pyrcc5 resources.qrc -o resources.py
```
### Run the program
1. C++ / qmake
```sh
$ ./Google-map 
```
2. python
```sh
$ sudo apt install python3-pyqt5.qtwebengine
$ python3 maptest.py 
```