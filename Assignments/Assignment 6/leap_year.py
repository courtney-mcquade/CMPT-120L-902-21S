def leap_year(year):
   if (year % 4 == 0):
        return("Is a leap year")    
   else: 
        return("Is not a leap year")

if __name__ == "__main__":
    years = [2000, 1994, 1912, 3002, 1700, 1400]
    answers = []
    for year in years:
        answers.append(leap_year(year))
    
    print(answers)