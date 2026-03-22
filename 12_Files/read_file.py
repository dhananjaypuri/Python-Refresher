import time
with open("test.txt", "r") as f:

    chunk_size = 10;
    data = f.read(chunk_size);
    while len(data) > 0:
        print(data, end='**');
        data = f.read(chunk_size);
        time.sleep(0.1);


