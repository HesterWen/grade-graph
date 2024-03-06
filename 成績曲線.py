import matplotlib.pyplot as plt

data = []
with open('scores.csv') as infile:
    text = infile.read().split()
    captions = text[0].split(',')
    for e in text[1:]:
        stu = e.split(',')
        scores = [float(sc) for sc in stu[1:]]
        data.append([stu[0]] + scores)
avg = []
for i in range(1, len(data[0])):
    all_scores = [data[stu][i] for stu in range(len(data))]
    avg.append(sum(all_scores)/len(all_scores))
for stu in data:
    name = stu[0]
    scores = stu[1:]
    plt.clf()
    plt.plot(scores, marker='o', label='Your Score')
    plt.title(name)
    plt.xticks(range(len(scores)), captions[1:])
    plt.xlabel('Items')
    plt.ylabel('Scores')
    plt.ylim(0, 110)
    plt.tight_layout()
    plt.plot(avg, marker='o', label='Class Average')
    plt.legend()
    plt.show()
    