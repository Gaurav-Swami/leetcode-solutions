

def is_palindrome(s: str)->bool:
	left = 0
	right = len(s)-1

	while left<=right:
		while left<right and not is_alphanum(s[left]):
			left += 1
		while left<right and not is_alphanum(s[right]):
			right -= 1

		if s[left].lower()!=s[right].lower():
			return False

		left += 1
		right -= 1

	return True


def is_alphanum(c:str)->bool:
	return((ord('A') <= ord(c) <= ord('Z')) or
		   (ord('a') <= ord(c) <= ord('z')) or
		   (ord('0') <= ord(c) <= ord('9')))

s = "A man, a plan, a canal: Panam"
print (is_palindrome(s))

		