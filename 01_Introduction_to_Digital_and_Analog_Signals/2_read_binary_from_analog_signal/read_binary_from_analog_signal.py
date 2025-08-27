import d2l
import random
import matplotlib.pyplot as plt
import numpy as np
import re
import os


pool = d2l.QuestionPool( "Read binary bits in analog signal", "pool.csv" )

for i in range(5):

    voltage = random.choice( [3.3,5] )
    thresholds = { 3.3:[1,1.5,2], 5:[2,2.5,3] }
    threshold = random.choice( thresholds[voltage] )
    plt.figure(figsize=[3,6])
    x = np.arange(0,5,1)
    y = [ random.choice([0,1]) for i in x]
    sig = [ threshold+random.uniform(0,voltage-threshold) if y[int(i)] else
            threshold-random.uniform(0,threshold) for i in np.arange(0,5,.2) ]
    #sig = [np.round(s, 1) for s in sig]
    fig = plt.figure().gca().set_xticks(np.arange(0,5,1))
    plt.plot(np.arange(0,5,.2),sig,color='k')
    plt.grid()
    plt.rcParams['svg.fonttype'] = 'none'
    plt.savefig(f"digital_waveform_module1_{i}.png",transparent=True)

    qtext = \
f"""<p>In practical applications, engineers use <b>analog signals</b>
to describe <b>digital signals</b>, since electricity is an analog
phenomena. The waveform depicts an <i>analog signal</i> 
which is being used to transmit <i>binary digital information</i></p>
<p>If the system considers any voltage greater than {threshold}V
to be a '1', and any lesser value a '0', what information is being 
expressed at each of time index shown in the figure?
"""
    question = d2l.SAQuestion(qtext)
    question.add_image(f"imagepools/deadbeef/digital_waveform_module1_{i}.png")
    question.add_answer("[, ]*".join([str(s) for s in y]), is_regex=True)
    pool.add_question(question)
pool.dump()
pool.package()
