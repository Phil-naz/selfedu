from jinja2 import Template

name = "Fedor"
age = 28

tm = Template("I am {{ a*2 }} years old and my name is {{ n.upper() }}")
msg = tm.render(n=name, a=age)   # Method 'render' of class Template

print(msg)

class Person1:
    def __init__(self, name1, age1):
        self.name1 = name1
        self.age1 = age1

per1 = Person1('Kirill', 33)
tm1 = Template("I am {{ p1.age1 }} years old and my name is {{ p1.name1 }}")
msg1 = tm1.render(p1 = per1)

print(msg1)

per2 = { 'name2': 'Sveta', 'age2': 34}

tm2 = Template("I am {{ p2.age2 }} years old and my name is {{ p2.name2 }}")

msg2 = tm2.render(p2 = per2)

print(msg2)

persons = [
    {"name": "aleks", "old": 18, "weight": 78.5},
    {"name": "kolya", "old": 28, "weight": 82.3},
    {"name": "ivan", "old": 33, "weight": 94.0},
]

tpl = '''
{%- for u in users -%}
{% filter upper %}{{u.name}}{% endfilter %}
{% endfor %}
'''

tm = Template(tpl)
msg = tm.render(users = persons)

print(msg)