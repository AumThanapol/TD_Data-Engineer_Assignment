# TD_Data-Engineer_Assignment

## Set up
```shell
$ python3 -m venv env
$ source env/bin/activate
$ pip install -r requirements.txt
```
---
## Q2_text_sanitizer
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
Document in file [Q3_sql/sql.html](TD_Data-Engineer_Assignment/Q3_sql/sql.html)
### Step
1. Mockup data
    1. Extract data from shopee.com (category, product, price)
    2. Random sales_transaction
2. SQL

| Tables        | Description           
| ------------- |:-------------
| sales_transaction      | Transaction from user 
| product      | Master Product      
| product_class | Master Product class/category