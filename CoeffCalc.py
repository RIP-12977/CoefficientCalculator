def calcError(val,act):
  err = val / act 
  return err 

msg = '''Find the error coefficient to multiply target by. Pass the actual value the robot traveled and the desired value to travel, both in inches. '''
actual = 0 
desired = 0 
error = 0 

# Main Loop 

print(msg)
while True:
  actual = float(input("\nActual Value: "))
  desired = float(input("Desired Value: "))
  error = calcError(actual, desired)
  print("Your coefficient is " + str(round(error,3)))
