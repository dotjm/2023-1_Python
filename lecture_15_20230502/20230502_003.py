chr = ["k", "r", "p", "s", "o"]
lists = ["a", "b", "c", "d", "e"]

t_char = lists + chr # cpmcatmate
print(t_char)

t_char = t_char + ['a', 'b']*3
print(t_char)


chr1 = ['k', 'r', 'p']
chr2 = ['a', 'd', 'b']
print(chr1 != chr2)

# 복사
# 얇은복사(같은 내용) vs 깊은복사(아예 분리)

# 얇은 복사 : 값이 같게 관리됨
chr1 = ['k', 'r', 'p']
chr0 = chr1

print("chr0 : ", chr0)
print("chr1 : ", chr1)
chr1.append('f')
print("chr0 : ", chr0)
print("chr1 : ", chr1)

# 깊은 복사 : 별개로 관리
chr3 = ['k', 'r', 'p']
chr4 = list(chr3)

print("chr3 : ", chr3)
print("chr4 : ", chr4)
chr3.append('f')
print("chr3 : ", chr3)
print("chr4 : ", chr4)