def plot_line_graph(file_name):
    data = {
        'labels': [],
        'datasets': [
            {
                'data': [

                ]
            }
        ]

    }
    # Read data from the text file
    with open(file_name, 'r') as file:
        for line in file:
            line2 = line[1:len(line) - 2]
            spl = line2.split(',')
        for i in spl:
            x, y = i.split(':')
            data['labels'].append(x)
            data['datasets'][0]['data'].append(y)

    print(data)






