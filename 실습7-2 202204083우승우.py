spell_re = ['r','e']
spell_serve = ['s','e','r','v','e']

spell_reserve = spell_re + spell_serve
print(spell_reserve)

spell_reserve[0:2] = ['o','b']
print(spell_reserve)