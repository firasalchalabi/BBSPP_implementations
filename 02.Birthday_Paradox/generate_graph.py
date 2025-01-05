from matplotlib import pyplot as plt
from main import generate_birthdays, matching_birthday

# x = [i for i in range(101)]
y_experiment = []
y_true = []
num_trials = 100000
for n_bdays in range(101):
    matching_trials = 0
    for t in range(num_trials):
        if matching_birthday(generate_birthdays(n_bdays)):
            matching_trials += 1
    y_experiment.append(matching_trials*100/num_trials)

plt.plot(y_experiment, label="Experimental Probability")
plt.savefig("graph.png")
plt.show()
