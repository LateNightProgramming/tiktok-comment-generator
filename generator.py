import random as r

main = ''
p1 = ['bro is','his fade be','ayo','he be lookin']
p2 = ['vovacious','zesty','sus','a silly billy','carmunkulous']
p2_1 = ['vovacious','zesty','sus','carmunkulous']
p3 = ['🔥','💀','🥶','🥵','❗','😂','😬']

p1text = r.choice(p1)
if p1text == 'ayo':
    main += p1text
    main += ' '
    p1.remove('ayo')
    p1text = r.choice(p1)
main += p1text
main += ' '
if p1text == 'his fade be' or p1text == 'he be lookin':
    p2text = r.choice(p2_1)
    main += p2text
else:
    p2text = r.choice(p2)
    main += p2text
p4 = r.choice([True, False])
if p4 == True:
    main += r.choice([' in ohio',', only in ohio',' in oklahoma',' only in oklahoma'])
times = r.randint(2,15)
for x in range(times):
    p3text = r.choice(p3)
    main += p3text
print(main)
