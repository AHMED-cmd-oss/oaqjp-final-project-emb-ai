# Repository for final project
This is a API project using Flask.
## About
This is flask API project.It makes a request to WATSON-EMOTION which IBM created .
The backend is linked with simple frontend which you can write the sentencs on it and response with 
the result.
## Example
```
/emotionDetection # post request
{
 "raw-document": "I love this technology"
}

# Response in case response code is 200 from the model.
(
       For the given statement, the system response is
       'anger': 0.006274985, 'disgust': 0.0025598293,
       'fear': 0.009251528, 'joy': 0.9680386 and 'sadness': 0.049744144.
       The dominant emotion is joy.

)

# Response in case response code is 400 from the model.
{
"Invalid input!"
}


```
## Technology
- python
 ## packages
 - flask
 - unittest-> for testing.
 - requests-> for HTTP request to get result from the model
 ## installing and importing packages
 ### installing packages
 ```bash
 pip install flask
 pip install unittest
 pip install requests
 ```
### importing packages
```
from flask import Flask,render_template,request
import unittest
import requests
```
## How to run
``` bash
git clone
flask --app server run --debug

```
## Project Structure
- static
- templates
- EmotionDetection
- test_emotion_detection.py
- readme.md
- server.py



