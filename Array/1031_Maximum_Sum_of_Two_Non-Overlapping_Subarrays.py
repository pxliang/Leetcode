class Solution:
    def maxSumTwoNoOverlap(self, A: List[int], L: int, M: int) -> int:

        L_sum = [0 for _ in range(len(A))]
        M_max_left = [0 for _ in range(len(A))]
        M_max_right = [0 for _ in range(len(A))]
        M_sum_left = 0
        M_sum_right = 0

        for i, num in enumerate(A):
            if i > 0:
                L_sum[i] = L_sum[i - 1] + num
            else:
                L_sum[i] = num

            if i >= M:
                M_sum_left = M_sum_left - A[i - M]
            M_sum_left += num
            M_max_left[i] = max(M_max_left[max(i - 1, 0)], M_sum_left)

            t = len(A) - i - 1
            if t < len(A) - M:
                M_sum_right = M_sum_right - A[t + M]
            M_sum_right += A[t]
            M_max_right[t] = max(M_max_right[min(t + 1, len(A) - 1)], M_sum_right)

        max_sum = 0
        for j in range(len(A) - L + 1):
            if j == 0:
                max_sum = max(max_sum, M_max_right[j + L] + L_sum[j + L - 1])
            elif j == len(A) - L:
                max_sum = max(max_sum, M_max_left[j - 1] + L_sum[-1] - L_sum[j - 1])
            else:
                max_sum = max(max_sum, max(M_max_left[j - 1], M_max_right[j + L]) + (L_sum[j + L - 1] - L_sum[j - 1]))

        return max_sum