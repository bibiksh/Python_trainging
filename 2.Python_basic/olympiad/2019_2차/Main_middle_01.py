def main():
	L = set()
	
	N = int(input())
	a = list(map(int, input().split()))
	t = sum(a)
	
	def dfs(x, s):
		if x == N:
			if 0 < s <= t:
				L.add(s)
		else:
			dfs(x+1, s-a[x])
			dfs(x+1, s)
			dfs(x+1, s+a[x])
	
	dfs(0, 0)
	
	print(t - len(L))

main()