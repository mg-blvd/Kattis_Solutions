signs = {
    'Mar' : {
        1 : 'Pisces',
        2 : 'Aries'
    },
    'Apr' : {
        1 : 'Aries',
        2 : 'Taurus'
    },
    'May' : {
        1 : 'Taurus',
        2 : 'Gemini'
    },
    'Jun' : {
        1 : 'Gemini',
        2 : 'Cancer'
    },
    'Jul' : {
        1 : 'Cancer',
        2 : 'Leo'
    },
    'Aug' : {
        1 : 'Leo',
        2 : 'Virgo'
    },
    'Sep' : {
        1 : 'Virgo',
        2 : 'Libra'
    },
    'Oct' : {
        1 : 'Libra',
        2 : 'Scorpio'
    },
    'Nov' : {
        1 : 'Scorpio',
        2 : 'Sagittarius'
    },
    'Dec' : {
        1 : 'Sagittarius',
        2 : 'Capricorn'
    },
    'Jan' : {
        1 : 'Capricorn',
        2 : 'Aquarius'
    },
    'Feb' : {
        1 : 'Aquarius',
        2 : 'Pisces'
    }
}

num_dates = int(input())

for num in range(num_dates):
    day, month = input().split()
    day = int(day)
    section = 0

    if month == 'Mar' or month == 'Apr' or month == 'May' or month == 'Jan':
        if day >= 21:
            section = 2
        else:
            section = 1
    elif month == 'Jun' or month == 'Sep' or month == 'Dec':
        if day >= 22:
            section = 2
        else:
            section = 1
    elif month == 'Jul' or month == 'Aug' or month == 'Oct' or month == 'Nov':
        if day >= 23:
            section = 2
        else:
            section = 1
    else:
        if day >= 20:
            section = 2
        else:
            section = 1

    print(signs[month][section])
