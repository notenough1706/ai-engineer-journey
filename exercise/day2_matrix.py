import numpy as np
# np.random.seed(0)
# data = np.random.rand(5, 3) * 100     # 5 mẫu × 3 đặc trưng (giả lập: tuổi, lương, điểm)

# mean = data.mean(axis=0)              # shape (3,) — mean từng cột
# std  = data.std(axis=0)               # shape (3,)

# normalized = (data - mean) / std      # ⭐ BROADCASTING ⭐
#                                        # mean/std bị "kéo" xuống từng hàng

# print(normalized.mean(axis=0))         # ~[0 0 0] ✅
# print(normalized.std(axis=0))          # ~[1 1 1] ✅

# ----------------------------------------------------------------

# a = np.arange(12)          # [0 1 2 3 4 5 6 7 8 9 10 11] — shape (12,)

# print(a.reshape(3, 4))     # ma trận 3 hàng 4 cột
# print(a.reshape(4, 3))     # 4 hàng 3 cột
# print(a.reshape(3, 2, 2))  # mảng 3 CHIỀU!

# # ⭐ Trick: dùng -1 để bảo numpy "tự tính chiều này giúp tôi"
# print(a.reshape(3, -1))    # 3 hàng, cột tự tính = 4
# print(a.reshape(-1))       # duỗi phẳng về 1 chiều (flatten)

# b = a.reshape(3, 4)
# print(b.flatten())         # [0 1 ... 11] — về lại 1D

# --------------------------------------------------------------------


# u = np.array([1, 2, 3])
# v = np.array([2, 0, 1])

# # (a) DOT PRODUCT — nhân từng cặp rồi cộng lại
# print(np.dot(u, v))          # 1*2 + 2*0 + 3*1 = 5

# # (b) NORM — độ dài của vector (Pythagore mở rộng)
# print(np.linalg.norm(u))     # √(1+4+9) = √14 ≈ 3.74
# print(np.linalg.norm(v))    


# # (c) COSINE SIMILARITY — cos góc giữa 2 vector
# cos_sim = np.dot(u, v) / (np.linalg.norm(u) * np.linalg.norm(v))
# print(cos_sim)               # ~0.59

# ---------------------------------------------------------------------

