def get_city_year(p0, perc, delta, target_population, debug=False):
    years = 0  # Sākam ar 0 gadiem
    while p0 < target_population:
        change = p0 * (perc / 100) + delta  # Aprēķinām iedzīvotāju pieaugumu katru gadu
        if round(change) <= 0:  # Ja iedzīvotāju skaits samazinās vai stagnē
            print(f"Stopped at year {years} due to negative or stagnating change {change}")
            return -1
        
        years += 1  # Pievienojam vienu gadu
        p0 += change # we assume that population is always integer, could debate this :)
        if p0 <= 0 and delta <= 0:  # Ja iedzīvotāju skaits kļūst negatīvs vai nemainās
            return -1  # Atgriežam -1, ja mērķis nav sasniedzams
        if debug:
            print(f"p0={p0}, years={years}")
    return years  # Atgriežam gadus, kad sasniegts mērķis

print("get_city_year(1000, 2, -50, 5000)", get_city_year(1000, 2, -50, 5000))
print("get_city_year(1500, 5, 100, 5000)", get_city_year(1500, 5, 100, 5000))
print("get_city_year(1500000, 2.5, 10000, 2000000) ", get_city_year(1500000, 2.5, 10000, 2000000))

# let's try negative percentage and positive delta
# tricky
print("get_city_year(1000, -2, 30, 2000) ", get_city_year(1000, -2, 30, 2000, debug=True))