min_size = 40

with open('anno_store/wider_origin_anno_landmark.txt') as f:
    with open('anno_store/wider_landmark_anno.txt', 'w') as out_f:
        for line in f:
            if line.startswith('#'):
                filename = line[1:].strip()
            else:
                fields = line.strip().split(' ')

                if '-1.0' in fields:
                    # ignore this line
                    continue

                fields = list(map(lambda x: round(float(x)), fields))

                if fields[2] < min_size or fields[3] < min_size:
                    continue

                x = [filename, fields[0], fields[1], fields[0] + fields[2] - 1, fields[1] + fields[3] - 1]
                x.extend(fields[4:6])
                x.extend(fields[7:9])
                x.extend(fields[10:12])
                x.extend(fields[13:15])
                x.extend(fields[16:18])

                out_f.write(' '.join(map(str, x)) + '\n')
