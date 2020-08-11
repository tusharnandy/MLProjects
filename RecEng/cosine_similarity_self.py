import numpy as np

text = ["London Paris London", "Paris Paris London"]

def vectorize_words(text):
    text_split = [i.split(" ") for i in text]

    unique = []

    for sentence in text_split:
        for word in sentence:
            if word not in unique:
                unique.append(word)

    vec_dim = len(unique)

    vectors = []

    for sentence in text_split:
        coordinates = [0]*vec_dim
        for word in sentence:
            for i in range(len(unique)):
                if word == unique[i]:
                    coordinates[i] += 1
        vectors.append(coordinates)

    return vectors

def dot(a, b):
    if len(a) == len(b):
        sum = 0
        for i in range(len(a)):
            sum += a[i]*b[i]
        return sum

    else:
        raise IndexError(f"Vector dimension {len(a)} not equal to {len(b)}")

def modulus(a):
    sum = 0
    for x in a:
        sum += x ** 2

    return sum ** 0.5

def cos(vec1, vec2):
    val = dot(vec1, vec2) / (modulus(vec1) * modulus(vec2))

    return val * 100

dimensions = vectorize_words(text)
print(dimensions)
rounded_ans = np.round(cos(dimensions[0], dimensions[1]))
print(rounded_ans)
