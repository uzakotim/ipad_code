import random
def generate_ip():
    output = []
    for _ in range(4):
        output.append(str(random.choice(list(range(256)))))
    return ".".join(output)

print(generate_ip())


"""
192.168.5.250 
"""