import reprlib
print(reprlib.repr(set('supercalifragilisticexpialidocious')))
print(set('supercalifragilisticexpialidocious'))


from string import Template
t = Template('${village}folk send $$10 to $cause.')
print(t.substitute(village='Taipei', cause='the gold found'))