import time
with open("photo.jpg", "rb") as rb:
    with open("photo_copy.jpg", "wb") as wb:
        chunk_size=4096;
        data = rb.read(chunk_size);
        
        while len(data)>0:
            wb.write(data);
            data = rb.read(chunk_size);
            time.sleep(0.1);

    print("File Copied");