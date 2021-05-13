N, K = map(int, input().split())

res = ''

img = [list(input().split()) for _ in range(N)]
up_sampled_img = [[] for i in range(K * N)]

for i in range(N):
    for k_i in range(K):
        for j in range(N):
            for k_j in range(K):
                up_sampled_img[i * K + k_i] += [img[i][j]]
    
up_sampled_img = '\n'.join([' '.join(line) for line in up_sampled_img])
print(up_sampled_img)