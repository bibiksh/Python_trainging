def main():
	for _ in range(int(input())) :
		s = input()
		n = len(s)

		chk = -1
		for i in range(n):
			if s[i] != s[n-i-1]:
				chk = i
				break

		if chk == -1:
			print("0")
			continue

		chk2 = n-1-chk
		p1 = s[:chk] + s[chk+1:]
		p2 = s[:chk2] + s[chk2+1:]
		if p1 == p1[::-1] or p2 == p2[::-1]:
			print("1")
		else:
			print("2")

main()