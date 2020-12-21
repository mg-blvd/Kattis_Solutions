#work in progress
import sys
max_earth = 365
max_mars = 687
cases = 0

while(True):
    cases += 1
    nums = input()
    if nums == '':
        break
    nums = nums.split()
    earth_day = int(nums[0])
    mars_day = int(nums[1])
    days_passed = 0
    while(True):
        if earth_day == mars_day:
            break;
        earth_day += 1
        mars_day += 1
        if earth_day >= max_earth:
            earth_day = 0
        if mars_day >= max_mars:
            mars_day = 0
        days_passed += 1
    print(f"Case {cases}: {days_passed}")
