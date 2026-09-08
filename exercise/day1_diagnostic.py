# numbers = [3, 8, 15, 22, 7, 40, 11, 6]
# for i in numbers:
#     if i%2==0:
#         print(i)



# text = "AI is powerful. I love AI. Ai changes everything."
# wordtofind = 'AI'
# count = text.upper().count(wordtofind.upper())
# print(count)


# Bài 3: Viết function nhận vào list số, trả về list mới với mỗi số bình phương
# def square_list(lst):
#     result = []
#     for x in lst:
#         result.append(x ** 2)
#     return result

# print(square_list([1,2,3,4]))

# Bài 4: Cho dictionary sau, in ra tên học viên có điểm cao nhất
# students = {"An": 8.5, "Bình": 9.2, "Chi": 7.8, "Dũng": 9.0}

# best_name = None
# best_score = -1

# for name,score in students.items():
#     if score > best_score:
#         best_name = name
# print(best_name)

# best_name = max(students, key=students.get)
# print(best_name)


# # # Bài 5: Đảo ngược một chuỗi (vd: "hello" → "olleh")
# text = "hello"
# print(text[::-1])   # "olleh"

# # Bài 6: Tính tổng tất cả số từ 1 đến 100 (dùng vòng lặp)

# total = 0
# for i in range(1, 101):
#     total = total + i
# print(total)

# # # Bài 7: Cho list các dict, lọc ra những người trên 25 tuổi
# people = [
#     {"name": "Lan", "age": 22},
#     {"name": "Hùng", "age": 28},
#     {"name": "Mai", "age": 30},
#     {"name": "Tùng", "age": 19},
# ]

# result = []
# for p in people:
#     if p["age"] > 25:
#         result.append(p)

# print(result)


# BTVN
# import numpy as np

# np.random.seed(42)   # (bonus) cố định random — chạy nhiều lần ra cùng kết quả

# m = np.random.rand(4, 4)
# print(m)

# print("Giá trị lớn nhất:", m.max())
# print("Vị trí (hàng, cột):", np.unravel_index(m.argmax(), m.shape))

import numpy as np
scores = np.array([[8, 7, 9],
                   [6, 9, 7],
                   [9, 8, 8],
                   [7, 6, 5],
                   [10, 9, 10]])

# a) TB từng học viên → tính NGANG qua hàng → axis=1
tb_hoc_vien = scores.mean(axis=1)
print(tb_hoc_vien)     # [8.   7.33 8.33 6.   9.67]

# b) TB từng môn → tính DỌC xuống cột → axis=0
tb_mon = scores.mean(axis=0)
print(tb_mon)          # [8.  7.8 7.8]

# c) Học viên giỏi nhất
vi_tri = tb_hoc_vien.argmax()      # index trong list tb_hoc_vien
ten = ["SV1", "SV2", "SV3", "SV4", "SV5"]
print("Học viên giỏi nhất:", ten[vi_tri])   # SV5