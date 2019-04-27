import numpy as np

encrypt = [8930,15006,8930,10302,11772,13806,13340,11556,12432,13340,10712,10100,11556,12432,9312,10712,10100,10100,8930,10920,8930,5256,9312,9702,8930,10712,15500,9312]
reorder = [19,4,14,3,10,17,24,22,8,2,5,11,7,26,0,25,18,6,21,23,9,13,16,1,12,15,27,20]

def decrypt():
    m = list(np.zeros(len(encrypt)))
    ans = ''
    for i in range(len(encrypt)):
        m[reorder[i]] = int(np.sqrt(encrypt[i])) + 1
    for i in range(len(encrypt)):
        ans += chr(m[i])
    return ans

def main():
    print(decrypt())

if __name__ == '__main__':
    main()
