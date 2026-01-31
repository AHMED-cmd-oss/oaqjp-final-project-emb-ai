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
{
        f"For the given statement, the system response is"
        f"'anger':{result['anger']}, 'disgust': {result['disgust']},"
        f"'fear': {result['fear']}, 'joy': {result['joy']}"
        f"and 'sadness': {result['sadness']}."
        f"The dominant emotion is {result['dominant_emotion']}."

}

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
 ```
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



