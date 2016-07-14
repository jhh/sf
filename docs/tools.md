# Development Tools

Various options for Python and C++ development environments.

## Python

We use Python for learning programming, experimentation and prototyping algorithms.

### Python on the Web

There are several good tools for running Python on the web. Many include programming tutorials.

- [Trinket.io](https://trinket.io) : An easy way to run Python in the browser. It includes visual introduction to code using the Python programming language and Turtles.
- [Computer Science Circles](http://cscircles.cemc.uwaterloo.ca/) : This website teaches computer programming using Python.
- [Checkio.org](https://checkio.org) : Checkio is the game for coders.

### Python

See the [Downloading Python](https://wiki.python.org/moin/BeginnersGuide/Download) on the Python wiki.

### Python with OpenCV

#### Windows

See the OpenCV [instructions](http://docs.opencv.org/2.4/doc/tutorials/introduction/windows_install/windows_install.html#windows-install-prebuild). We haven't tested this method yet.

#### Mac OS X

1. Install [Homebrew](http://brew.sh).
2. Install Python 3

  ```sh
  brew install python3
  ```

3. Install [Cuda](https://developer.nvidia.com/cuda-downloads) and edit `$PATH` to include development tools.

  ```sh
  brew cask install cuda
  export PATH=/Developer/NVIDIA/CUDA-7.5/bin:$PATH
  ```

4. Install OpenCV

  ```sh
  brew tap homebrew/science
  brew install opencv3 --with-contrib --with-cuda --with-ffmpeg --with-tbb --with-qt5 --c++11 --with-python3
  ```

5. Install `virtualenv`

  ```sh
  pip3 install virtualenv virtualenvwrapper
  ```

  Now that both virtualenv and virtualenvwrapper have been installed, update ~/.profile file to include the following lines at the bottom of the file

  ```sh
  # virtualenv and virtualenvwrapper
  export WORKON_HOME=$HOME/.virtualenvs
  source /usr/local/bin/virtualenvwrapper.sh
  ```

  Close terminal instance and open a new one to reload `~/.profile`.

6. Create Python virtual environments

  ```
  mkvirtualenv cv -p python3
  ```

7. Install NumPy in your virtual environment

  ```
  pip install numpy
  ```

8. Link the OpenCV Python 3 bindings to your virtual environment. Note: the command below assumes Python 3.5

  ```sh
  cd ~/.virtualenvs/cv/lib/python3.5/site-packages
  ln -s `brew --prefix opencv3`/lib/python3.5/site-packages/cv2.cpython-35m-darwin.so .
  ```

9. Check installation

  ```
  python
  Python 3.5.2 (default, Jul  2 2016, 03:10:20)
  [GCC 4.2.1 Compatible Apple LLVM 7.3.0 (clang-703.0.31)] on darwin
  Type "help", "copyright", "credits" or "license" for more information.
  >>> import cv2
  >>> cv2.__version__
  '3.1.0'
  >>>
  ```

  #### Linux

These instructions are adapted from PyImageSearch's Raspbian installation [instructions](http://www.pyimagesearch.com/2016/04/18/install-guide-raspberry-pi-3-raspbian-jessie-opencv-3/).

### TODO
- C++
- C++ with exercism: cmake, Boost
- C++ with OpenCV
- C++ with WPI and ARM toolchain
