from sys import argv

if len(argv) < 4:
    print('error attributes less 3 digits')
    exit()

values = []

for el in argv[1:]:
    try:
        el = int(el)
        values.append(el)
    except ValueError:
        print('you need use 3 digits\n[выработка в часах] [ставка в час] [премия]')
        exit() 

#values = [20, 300, 2050]
#print(lambda work_time, mp_hour, prem: (work_time * mp_hour) + prem, values)

def out_final(*args):
    params = args[0]
    out = params[0] * params[1] + params[2]
    return out 

print(out_final(values))
exit()
