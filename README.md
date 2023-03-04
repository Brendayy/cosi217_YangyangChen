# cosi217_YangyangChen

### 1. RESTful API
1. Under /assignment1, change directory to restful_API_and_flask
```bash
$ cd restful_API_and_flask
```
2. run following command
```bash
$ python3 restful_api_and_flask.py
```
3. To have the API respond to GET and POST, run the following command:

NOTE: localhost:5000 sometimes gets denied, possibly related with Apple M1 chip. Therefore I changed the port to 5002. You may change it to another if encountering the same problem. 
```bash
$ curl http://127.0.0.1:5002/api
$ curl -H "Content-Type: text/plain" -X POST -d@input.txt http://127.0.0.1:5002/api
```
(input.txt is under the same directory)

### 2. Flask webserver
1. With `restful_api_and_flask.py` still running from the first homework, access http://127.0.0.1:5002/form
2. Input any text in the text box, and click submit
3. page with recognzied named entities result should appear

### 3. Streamlit
1. quit any server that serving restful_API_and_flask, change directory to streamlit folder, for example
```bash
$ cd ../streamlit
```
2. run the following command:
```bash
$ streamlit run streamlit.py
```
3. Input any text in the text box, and click submit
4. NER result should appear on the same page under submit button
