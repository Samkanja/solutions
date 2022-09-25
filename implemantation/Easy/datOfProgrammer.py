def datOfProgrammer(year):
    if (year >= 1918 and (year % 400==0 or (year % 4 ==0 and year % 100 != 0))) or (year < 1919 and year % 4 ==0):
        return f'{str(256 - 244)}.09.{str(year)}'
    return f"{str(256 - 243)}.09.{str(year)}"


year = int(input('year: ').strip())
print(datOfProgrammer(year))