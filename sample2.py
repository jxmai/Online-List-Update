import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_subplot(111)

# the data
N = 5
menMeans = [18, 35, 30, 35, 27]
womenMeans = [25, 32, 34, 20, 25]

# necessary variables
ind = np.arange(N)                # the x locations for the groups
width = 0.12                      # the width of the bars

# the bars
rects1 = ax.bar(ind, menMeans, width, color='black')

rects2 = ax.bar(ind+width, womenMeans, width, color='red')

rects3 = ax.bar(ind+width*2, womenMeans, width,
                color='pink')

# axes and labels
ax.set_xlim(-width, len(ind)+width)
ax.set_ylim(0, 45)
ax.set_ylabel('Scores')
ax.set_title('Scores by group and gender')
xTickMarks = ['Group'+str(i) for i in range(1,6)]
ax.set_xticks(ind+width)
xtickNames = ax.set_xticklabels(xTickMarks)
plt.setp(xtickNames, rotation=45, fontsize=10)

## add a legend
ax.legend((rects1[0], rects2[0]), ('Men', 'Women'))

plt.show()