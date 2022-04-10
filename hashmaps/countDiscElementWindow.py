class Solution:
    def countDistinct(self, A, N, K):
        # Code here

        answer = []
        discElement = 0
        cache = {}

        for i in range(N):

            if i < K:
                if A[i] in cache:
                    cache[A[i]] += 1
                else:
                    cache[A[i]] = 1
                    discElement += 1
            else:
                answer.append(discElement)
                cache[A[i - k]] -= 1
                if cache[A[i - k]] == 0:
                    del cache[A[i - k]]
                    discElement -= 1

                if A[i] in cache:
                    cache[A[i]] += 1
                else:
                    cache[A[i]] = 1
                    discElement += 1

            if i == N - 1:
                answer.append(discElement)

        return answer
