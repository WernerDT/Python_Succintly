#comment line
cost_per_hour = 1.02

#claculate cost per day
cost_per_day = cost_per_hour * 24

#cost per mont
cost_per_month = cost_per_day * 30

#print some info
print("Cost per day = ${:.2f}.".format(cost_per_day))
print("Cost per month = ${:.2f}".format(cost_per_month))