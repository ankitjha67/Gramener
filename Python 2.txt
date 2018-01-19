from datetime import date   # Calling date from datetime library
date1=date(1990,1,1)        # Input date 1
date2=date(2000,12,31)      # Input date 2
diff=date2-date1            # Calculate difference between 2 dates
print(diff)                 # print difference
print(diff.days/7+1)        # Calculate number of thursday in that period keeping in mind the leap years