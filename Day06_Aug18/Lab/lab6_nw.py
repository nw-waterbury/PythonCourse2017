def divisor(a,b):
    r=a%b
    if r == 0: return b
    else: return divisor(b,r)
def prime(num):
	prime_list = []
	def is_prime(number):
		for i in range(1,number):
			if number % i ==0:
				pass
			else:
				prime_list.append(number)
	for i in range(1,num):
		is_prime(i)
	return prime_list
