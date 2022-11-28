# Introduction
This is a basic repository designed for the purposes of Task assigned by Deus Ex Machina by Evangelos Tikas.
I am a MSc student in Electronics experienced in Python and other languages. The whole 
purpose of this project is to employ functional tests.


## Instructions
We need to test some cases between 2 messages, one from user login and one from user update. A succesfull login request returns status 200
while an erroneous one returns 400. Some basic requirements have to be fullfiled. The Host section must be the same in both requests (probably the access token too).
In update user message the "role" field can only be one of the following: admin, executor or reporter. Value of "active" field can be true or false.


## Assumptions
Python3 is the latest example and we are using Python3.8.13 for our purpose. Python 2 suppport is possible, but out of the scope of this solution.

I am not using any 3rd party applications for the core application. Performance could be improved using other packages, or other versions of Python (perhaps PyPy).

Regarding testing approach I employed pytest for its simplicity and speed. There are a lot more options.
Robot Framework is a common open-source automation framework for Acceptance Testing, Acceptance  
Test-Driven Development (ATTD), and Robotic Process Automation (RPA). A good old alternative could be unittest.

### 2) Running Steps
There are 2 options: run it directly using python command or run it by script.

If you wish to execute the script simply:

```bash
chmod +x test_setup.sh
./test_setup.sh
```

In this way a virtual environment with all the dependencies installed will be created!
      
You can run it with the python command directly.

```bash
pytest test_run/test_run.py
```

If you have pytest installed. If not run:

```bash
pip3 install pytest
```

or 

```bash
python -m pip install pytest
```

Expected message:

```
./test_setup.sh 
Creating python virtual environment
Activating the venv
Installing python libraries
Collecting pytest==7.2.0
  Using cached pytest-7.2.0-py3-none-any.whl (316 kB)
Collecting packaging
  Using cached packaging-21.3-py3-none-any.whl (40 kB)
Collecting attrs>=19.2.0
  Using cached attrs-22.1.0-py2.py3-none-any.whl (58 kB)
Collecting exceptiongroup>=1.0.0rc8
  Using cached exceptiongroup-1.0.4-py3-none-any.whl (14 kB)
Collecting pluggy<2.0,>=0.12
  Using cached pluggy-1.0.0-py2.py3-none-any.whl (13 kB)
Collecting iniconfig
  Using cached iniconfig-1.1.1-py2.py3-none-any.whl (5.0 kB)
Collecting tomli>=1.0.0
  Using cached tomli-2.0.1-py3-none-any.whl (12 kB)
Collecting pyparsing!=3.0.5,>=2.0.2
  Using cached pyparsing-3.0.9-py3-none-any.whl (98 kB)
Installing collected packages: iniconfig, tomli, pyparsing, pluggy, exceptiongroup, attrs, packaging, pytest
Successfully installed attrs-22.1.0 exceptiongroup-1.0.4 iniconfig-1.1.1 packaging-21.3 pluggy-1.0.0 pyparsing-3.0.9 pytest-7.2.0 tomli-2.0.1
WARNING: You are using pip version 22.0.4; however, version 22.3.1 is available.
You should consider upgrading via the '/home/evangelost/Python/Automation_test/venv/bin/python3 -m pip install --upgrade pip' command.
Running the python script
============================= test session starts ==============================
platform linux -- Python 3.8.13, pytest-7.2.0, pluggy-1.0.0
rootdir: /home/evangelost/Python/Automation_test
collected 3 items                                                              

test_run/test_run.py ...                                                 [100%]

============================== 3 passed in 0.03s ===============================
Deactivting the venv

Time spent in user mode   (CPU seconds) : 10.487s
Time spent in kernel mode (CPU seconds) : 1.637s
Total time                              : 0:21.77s
CPU utilisation (percentage)            : 55.6%
Times the process was swapped           : 0
Times of major page faults              : 0
Times of minor page faults              : 180484
```








- 📫 How to reach me:

> [facebook]

> [instagram]

> [linkedin]

> [researchgate]

Main applications, tests, tutorials and any exercises involved in MSc Electronics, Physics AUTh!

      
      
<br>

[website]: https://www.geeksforgeeks.org/map-associative-containers-the-c-standard-template-library-stl/?ref=leftbar-rightbar
[facebook]: https://www.facebook.com/vagelis.tikas/
[instagram]: https://www.instagram.com/vaggelis_tikas/
[linkedin]: https://www.linkedin.com/notifications/
[researchgate]: https://www.researchgate.net/profile/Evangelos-Tikas
