scholarec
=========
Recommendation of Scholarly Works 
---------------------------------

**Usage**

Refer to README.md at https://github.com/arcolife/scholarec/ for instructions 
on how to install scholarec for use in this django project.

* In order to continue, you need to have:
    
    1.     Django>=1.5 installed.
    	   (Refer: https://www.djangoproject.com/download/ )
    2.	   ElasticSearch(0.90.11) instance up and running. 
    	   (Refer: http://elasticsearch.org )

For first usage, run following on a Linux console:
``` 
    $ ./setup
```

For normal usage, go to 'scholarec_web/', and run:
```
    $ ./manage.py runserver
```

- NOTE: You need to run the following when changes to DB are made:
```
 $ ./manage.py syncdb
```
***

**FAQ**

Q. In requirements.txt, how do I install scholarec directly from source ?

A. Simply include "-e git+https://github.com/arcolife/scholarec.git#egg=scholarec"

***

**LICENSE**

[![GPL V3](http://www.gnu.org/graphics/gplv3-127x51.png)](http://www.gnu.org/licenses/gpl-3.0-standalone.html)

***

**REFERENCES**
- Python Social Auth - http://psa.matiasaguirre.net/docs/index.html
