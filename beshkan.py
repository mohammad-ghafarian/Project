import matplotlib.pyplot as plt
import random
random.seed()

#aray
people = []
for i in range(0,50):
    people.append(100)

# halghe & shart
for beshkan in range (0,10000):
    for persion1 in range(0,50):
        persion2 = random.randrange(0,50)
        while people[persion2]==0:
            persion2=random.randrange(0,50)

        if people[persion1] !=0:
            people[persion1]=people[persion1]-1
            people[persion2]=people[persion2]+1


plt.bar(range(0,50),sorted(people))
plt.show()
