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
The procedure here was tested on Windows 10. Nevertheless, it should also work on any other relatively modern version of Windows OS.

  1. Download the 64-bit Python 3.5.2 installer from [here](https://www.python.org/ftp/python/3.5.2/python-3.5.2-amd64.exe).
  2. Run the installer.
  3. Check "Add Python 3.5 to PATH".
  4. Click on "Install Now".
  5. When installer is finished, verify Python is installed by running `python` at the command line. You should see output similar to `Python 3.5.2 (v3.5.2:4def2a2901a5, Jun 25 2016, 22:18:55) [MSC v.1900 64 bit (AMD64)] on win32`.
  6. At the PowerShell command line, run `python -m pip install --upgrade pip`
  7. At the command line, change directory to your `Documents` (or preferred project) directory.
  8. Run `mkdir venvs`. This will create a directory to hold virtual Python environments.
  9. Run `python -m venv .\venvs\cv`.
  10. Run `.\venvs\cv\Scripts\Activate.ps1`. You should see a `(cv)` at the beginning of your command prompt. When the virtual environment is activated like this, all packages you install will now be isolated in this virtual environment.
  11. Download `opencv_python-3.1.0+contrib_opencl-cp35-cp35m-win_amd64.whl` from <http://www.lfd.uci.edu/~gohlke/pythonlibs/#opencv>.
  12. Once downloaded, note where the downloaded file is saved. From the command prompt, run `pip install <downloaded file>`. For example, I ran `pip install D:\Users\Jeff\Downloads\opencv_python-3.1.0+contrib_opencl-cp35-cp35m-win_amd64.whl`.
  13. Download and install Cmake for windows <https://cmake.org/download/>.
  14. Download and install Microsoft Visual Studio Community <https://www.visualstudio.com/>. Install with C++.
  15. Download and unzip OpenCV source code <https://github.com/opencv/opencv/archive/3.1.0.zip> to `C:\opencv\sources`.
  16. Run Cmake GUI and browse to the source code for "Where is the source code" text entry box.
  17. Create a build directory `C:\opencv\build` and enter that directory in Cmake's "Where to build the binaries" text entry box.
  18. Click the "Configure" button. After running, Python 3 option should be checked in the checklist with the red background.
  19. Click the "Generate" button to build Visual Studio Project files in the `C:\opencv\build` directory.
  20. In Explorer, navigate to `D:\opencv\build` and double-click the `ALL_BUILD.vcxproj` file to open the project in VS.
  21. In the "Build" menu, select "Build Solution". This step will take a while.
  22. If successful, in the "Build" menu, select "Build -> INSTALL"
  23. At the command line, check the installation:

    ```
     python
     Python 3.5.2 (v3.5.2:4def2a2901a5, Jun 25 2016, 22:01:18) [MSC v.1900 32 bit (Intel)] on win32
     Type "help", "copyright", "credits" or "license" for more information.
     >>> import cv2
     >>> cv2.__version__
     '3.1.0'
     >>>
    ```

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
