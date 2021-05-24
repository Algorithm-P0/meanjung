def solution(msg):
    alphabet = [0]
    alphabet.extend([chr(i) for i in range(65, 91)])
    result = []
    i = 0
    while i < len(msg):
        j = i+1
        while True:
            if j>len(msg):
                result.append(alphabet.index(msg[i:j]))
                i = j+1
                break
            if msg[i:j] not in alphabet:
                result.append(alphabet.index(msg[i:j-1]))
                alphabet.append(msg[i:j])
                i = j-1
                break
            j+=1
    return result


solution("ABABABABABABABAB")