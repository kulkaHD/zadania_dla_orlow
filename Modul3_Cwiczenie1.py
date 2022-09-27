numbers = [5,32,56,2,2,16,7,10,23,100]
mean_number = 0
mod_numbers = []
for i in numbers:
  i = round(i, -1)
  mod_numbers.append(i)

mod_numbers = sorted(mod_numbers)
print(mod_numbers)
del (mod_numbers[0], mod_numbers[-1])
print (mod_numbers)

mean_number = (sum(mod_numbers))/(len(mod_numbers))
print (mean_number)
