"""
5. WAF bonus(salary, rate=0.10) that calculates new salary after applying a bonus
   rate. Call the function once using positional args and once using kwargs. Show a 
   case where incorrect mixing of positional and kwargs shows error
"""

def bonus(salary, rate=0.10):
    new_salary = salary + salary*rate
    return new_salary
# positional args
print(bonus(50000, 10))
# kwargs 
print(bonus(rate=10, salary=60000))
"""
# positional and keyword args
print(bonus(rate=10, 10000))
# positional argument follows keyword argument : error
"""