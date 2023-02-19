# TD_Data-Engineer_Assignment

Slide Present in file [Present_Thanapol_Thanamit.pdf](Present_Thanapol_Thanamit.pdf)
---
## How to Set up projects
```shell
$ python3 -m venv env
$ source env/bin/activate
$ pip install -r requirements.txt
```
---
## Q2_text_sanitizer
Script in file [Q2_text_sanitizer/text_sanitizer.py](Q2_text_sanitizer/text_sanitizer.py)

```$ python3 text_sanitizer.py [source] [target]```

### Example
```shell
$ python3 text_sanitizer.py source.txt
$ python3 text_sanitizer.py source.txt target.txt
$ python3 text_sanitizer.py config.cfg
$ python3 text_sanitizer.py config.cfg cli
$ python3 text_sanitizer.py config.cfg target2.txt
```
---
## Q3_SQL
Document in file [Q3_sql/document_sql.pdf](Q3_sql/document_sql.pdf)

### Step
1. Mockup data
    1. Extract data from shopee.com (category, product, price)
    2. Mockup sales_transaction by random
2. SQL

| Tables        | Description           
| ------------- |:-------------
| sales_transaction      | Transaction from user 
| product      | Master Product      
| product_class | Master Product class/category