# torqata-demo
Demo

The focus for demo was to show
1. SQLAlchemy classes and assocations
2. Marshmellow for marshelling objects to send via json
3. Config setup for factory creation of flask app
4. Simple Angular html for viewing data

## Build Frontend
To build for production you would need to 
``` cd frontend ```

``` ng build --stats-json ```

``` cd ../ ```

``` node deploy/generate_angular_json.js ```

The above commands build the front end and create manifest for the flask application to use in a jinja2 template.

## Run flask

``` pip3 install -r requirements.txt ```
``` flask run ```


## Config
Since we are using OAuth there are ids associated with google that allows it to connect to the OAuth provider by google. To ensure login works you will need to provide a .env file for the system you are deploying to. 
