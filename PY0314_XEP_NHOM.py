import sys


def solve():
  # Đọc toàn bộ input dưới dạng danh sách các token (từ, số) cách nhau bởi khoảng trắng/xuống dòng.
  # Cách này xử lý được mọi bài toán nhập xuất tự do, không sợ lỗi định dạng dòng.
  input_data = sys.stdin.read().split()
  if not input_data:
    return

  iterator = iter(input_data)

  try:
    num_tests_str = next(iterator)
    num_tests = int(num_tests_str)
  except StopIteration:
    return

  for _ in range(num_tests):
    n = int(next(iterator))
    k = int(next(iterator))

    total_sum = 0
    max_p = 0

    # Đọc n số dân số của n quốc gia
    for _ in range(n):
      val = int(next(iterator))
      total_sum += val
      if val > max_p:
        max_p = val

    # Giới hạn 1: Tổng dân số chia cho kích thước nhóm k
    ans1 = total_sum // k

    # Giới hạn 2: Loại bỏ nước lớn nhất, các nước còn lại kết hợp với nước lớn nhất (cần k-1 thành viên)
    ans2 = (total_sum - max_p) // (k - 1)

    # In kết quả của test case hiện tại
    print(min(ans1, ans2))


if __name__ == "__main__":
  solve()