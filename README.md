# Country Language JSON Generator

This script generates dictionary lookup for native names for countries and languages.

**Countries**:
```
{ 'cn': {'de': 'China', 'en': 'China', 'th': 'จีน', 'zh': '中国'},
  'de': {'de': 'Deutschland', 'en': 'Germany', 'th': 'เยอรมนี', 'zh': '德国'},
  'th': {'de': 'Thailand', 'en': 'Thailand', 'th': 'ไทย', 'zh': '泰国'},
  'us': { 'de': 'Vereinigte Staaten',
          'en': 'United States',
          'th': 'สหรัฐอเมริกา',
          'zh': '美国'}}
```

**Languages**:
```
{ 'de': {'de': 'Deutsch', 'en': 'German', 'th': 'เยอรมัน', 'zh': '德文'},
  'en': {'de': 'Englisch', 'en': 'English', 'th': 'อังกฤษ', 'zh': '英文'},
  'th': {'de': 'Thailändisch', 'en': 'Thai', 'th': 'ไทย', 'zh': '泰文'},
  'zh': {'de': 'Chinesisch', 'en': 'Chinese', 'th': 'จีน', 'zh': '中文'}}
```

The currently supported output is JSON. These files can be hard coded into an application.


## Getting Started

- Copy `sample_config.yml` to `config.yml`. 
- Update the `countries` and `languages` sections to match your requirements
- Run `python3 generate.py`


## Design Principles

- Countries and languages are generally a static list of data. Instead of using modules or a dynamic data store, it would probably be better to hard code this data into an application. 

- Public data sets didn't seem easy to modify or trust the source. How can the source be inspected or updated? 


## Data Source

- https://github.com/umpirsky/country-list
- https://github.com/umpirsky/language-list
