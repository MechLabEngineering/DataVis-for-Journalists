# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

import numpy as np
%matplotlib inline
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style("whitegrid")

# <codecell>

wieoft = np.arange(1, 11, 0.1)
manuell = np.arange(1,11, 0.1)
algorithm = 10./wieoft**3.0

# <headingcell level=3>

# Plot it

# <codecell>

plt.figure(figsize=(5,3))
plt.plot(wieoft, manuell, label='per Hand', linewidth=10)
plt.plot(wieoft, algorithm, label='Algorithmus', linewidth=10)
plt.xlabel('Wie oft muss etwas gemacht werden?')
plt.ylabel('Zeitbedarf')
plt.legend(loc=5)
plt.xlim(1,10)
plt.ylim(0,10)
plt.title('Wann es sich lohnt einen Algorithmus zu schreiben')

plt.tight_layout()
plt.savefig('WhenToWriteAnAlgorithm.png', dpi=150)

# <codecell>


