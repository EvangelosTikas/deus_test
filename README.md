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
pip3 install pytest```
or 
```bash
python -m pip install pytest
```

Expected message:









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
