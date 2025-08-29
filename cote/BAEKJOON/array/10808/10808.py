string = input()

nums = [0] * 26

eng = 'abcdefghijklmnopqrstuvwxyz'

for chr in eng:
    num = string.count(chr)
    idx = eng.find(chr)
    nums[idx] = num

print(*nums)