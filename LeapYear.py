n=int(input())

if n%4 == 0:
  if n%100 == 0:
    if n%400 == 0:
        print('Y')
    else:
        print("N")
  else:
      print('Y')
else:
	print("N")
