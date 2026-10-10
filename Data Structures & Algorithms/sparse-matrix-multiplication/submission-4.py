class Solution:
    def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
        def split_matrix(M):
            """Splits a square matrix into four equal quadrants."""
            n = len(M)
            mid = n // 2
            m11 = [row[:mid] for row in M[:mid]]
            m12 = [row[mid:] for row in M[:mid]]
            m21 = [row[:mid] for row in M[mid:]]
            m22 = [row[mid:] for row in M[mid:]]
            return m11, m12, m21, m22

        def add(A, B):
            """Adds two matrices."""
            return [[A[i][j] + B[i][j] for j in range(len(A))] for i in range(len(A))]

        def sub(A, B):
            """Subtracts matrix B from matrix A."""
            return [[A[i][j] - B[i][j] for j in range(len(A))] for i in range(len(A))]

        def merge(c11, c12, c21, c22):
            """Combines four quadrants back into a single matrix."""
            top = [c11[i] + c12[i] for i in range(len(c11))]
            bottom = [c21[i] + c22[i] for i in range(len(c21))]
            return top + bottom

        def strassen_core(A, B):
            """Internal recursive Strassen logic for perfect 2^k square matrices."""
            n = len(A)
            
            # Base case: switch to standard multiplication for tiny matrices
            if n <= 32:
                res = [[0] * n for _ in range(n)]
                for i in range(n):
                    for j in range(n):
                        for k in range(n):
                            res[i][j] += A[i][k] * B[k][j]
                return res
            
            # Divide into quadrants
            a11, a12, a21, a22 = split_matrix(A)
            b11, b12, b21, b22 = split_matrix(B)
            
            # Compute the 7 Strassen products
            m1 = strassen_core(add(a11, a22), add(b11, b22))
            m2 = strassen_core(add(a21, a22), b11)
            m3 = strassen_core(a11, sub(b12, b22))
            m4 = strassen_core(a22, sub(b21, b11))
            m5 = strassen_core(add(a11, a12), b22)
            m6 = strassen_core(sub(a21, a11), add(b11, b12))
            m7 = strassen_core(sub(a12, a22), add(b21, b22))
            
            # Reconstruct result quadrants
            c11 = add(sub(add(m1, m4), m5), m7)
            c12 = add(m3, m5)
            c21 = add(m2, m4)
            c22 = add(sub(add(m1, m3), m2), m6)
            
            return merge(c11, c12, c21, c22)

        def strassen(A, B):
            """Wrapper function to handle arbitrary matrix dimensions via zero-padding."""
            rA, cA = len(A), len(A[0])
            rB, cB = len(B), len(B[0])
            
            if cA != rB:
                raise ValueError("Incompatible matrix dimensions for multiplication.")
                
            # Find the next power of 2 that can comfortably fit all dimensions
            max_dim = max(rA, cA, rB, cB)
            n = 1
            while n < max_dim:
                n *= 2
                
            # Pad matrix A to size n x n
            A_pad = [[0] * n for _ in range(n)]
            for i in range(rA):
                for j in range(cA):
                    A_pad[i][j] = A[i][j]
                    
            # Pad matrix B to size n x n
            B_pad = [[0] * n for _ in range(n)]
            for i in range(rB):
                for j in range(cB):
                    B_pad[i][j] = B[i][j]
                    
            # Run the core Strassen algorithm on the square, padded matrices
            C_pad = strassen_core(A_pad, B_pad)
            
            # Strip away the zero-padding to return the correct dimensions (rA x cB)
            return [row[:cB] for row in C_pad[:rA]]

        return strassen(mat1, mat2)