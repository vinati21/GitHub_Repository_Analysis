---
title: dython
---

# Dython

[![PyPI Version](https://img.shields.io/pypi/v/dython?style=for-the-badge)](https://pypi.org/project/dython/)
[![Stars](https://img.shields.io/github/stars/shakedzy/dython?style=for-the-badge)](https://github.com/shakedzy/dython)
[![Forks](https://img.shields.io/github/forks/shakedzy/dython?style=for-the-badge)](https://github.com/shakedzy/dython)
[![License](https://img.shields.io/pypi/l/dython?style=for-the-badge)](https://github.com/shakedzy/dython/blob/master/LICENSE)

A set of **D**ata analysis tools in p**YTHON** 3.x.

Dython was designed with analysis usage in mind - meaning ease-of-use, functionality and readability are the core 
values of this library. Production-grade performance, on the other hand, were not considered.

## Installation:
Dython can be installed directly using `pip`:
```
pip install dython
```
If you wish to install from source:
```
git clone https://github.com/shakedzy/dython.git
pip install ./dython
```

**Dependencies:** `numpy`, `pandas`, `seaborn`, `scipy`, `matplotlib`, `sklearn`

## Modules Documentation:

{% for page in site.pages %}
  {% if page.type == 'doc' %}
* [{{page.title}}]({{page.url | relative_url}})
  {% endif %}
{% endfor %}

### Examples:
Some examples are available, see descriptions [here]({{'examples.html' | relative_url}}).

-------------

### Related blogposts:
Read more about the Nominal tools on [The Search for Categorical Correlation](https://medium.com/@shakedzy/the-search-for-categorical-correlation-a1cf7f1888c9)
