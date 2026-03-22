with open("test.txt", "r") as rf:
    with open("test_copy.txt", "w") as wf:
        chunk_size = 5;
        data = rf.read(chunk_size);
        while len(data)>0:
            wf.write(f"{data}");
            data = rf.read(chunk_size);
    print("File copied successfully ");