from jinja2 import Template, escape

name = "Fedor"
age = 28

tm = Template("Hello, my name is {{ n.upper }}, I\'m {{ a*2 }}")
# Возможно писать консрукции языка питон, так: tm = Template("Hello, my name is {{ n.upper() }}, I\'m {{ a*2 }}")
msg = tm.render(n = name, a = age)

# Альтернативно можно использовать f строку
msg2 = f"Hello {name}"

# print(msg, msg2, sep="\n")
print(msg, msg2, sep="\n")

# Alternative method

print('\nAlternative method')
class Person:
    def __init__(self, name3, age3):
        self.name3 = name3
        self.age3 = age3

per = Person("Philip", 33)

tm = Template("My name is {{ p.name3 }}, I\'m {{ p.age3 }}.")
msg3 = tm.render(p = per)

print(msg3)

print('\nWorking with list FOR')

cities = [{'id': 1, 'city': "Moscow"},
          {'id': 5, 'city': "Twer\'"},
          {'id': 7, 'city': "Minsk"},
          {'id': 8, 'city': "Smolensk"},
          {'id': 11, 'city': "Kaluga"}]

link = '''<select name="cities">
{% for c in cities -%}
    <option value="{{c['id']}}">{{c['city']}}</option>
{% endfor -%}
</select>'''

tm = Template(link)
msg3 = tm.render(cities = cities)

print(msg3)