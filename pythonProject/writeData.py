with open("test.txt", 'r') as reader:
    content = reader.readlines()  # content = reader.read().splitlines() (this will split each line)
    reversed(content)
    with open("test.txt", 'w') as writer:
        for line in reversed(content):
            writer.write(line)
        #  writer.write(line+"\n")
