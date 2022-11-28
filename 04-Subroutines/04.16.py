def month(num):
    switch={
        1:'styczeń',
        2:'luty',
        3:'marzec',
        4:'kwiecień',
        5:'maj',
        6:'czerwiec',
        7:'lipiec',
        8:'sierpień',
        9:'wrzesień',
        10:'październik',
        11:'listopad',
        12:'grudzień'
     }
    return switch.get(num,"Invalid input")
print(month(3))
print(month(11))
print(month(0))