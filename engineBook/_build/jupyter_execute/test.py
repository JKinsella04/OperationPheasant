{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "import chart_studio.plotly as py\n",
    "import numpy as np\n",
    "\n",
    "data = [dict(\n",
    "        visible = False,\n",
    "        line=dict(color='#00CED1', width=6),\n",
    "        name = '𝜈 = '+str(step),\n",
    "        x = np.arange(0,10,0.01),\n",
    "        y = np.sin(step*np.arange(0,10,0.01))) for step in np.arange(0,5,0.1)]\n",
    "data[10]['visible'] = True\n",
    "\n",
    "steps = []\n",
    "for i in range(len(data)):\n",
    "    step = dict(\n",
    "        method = 'restyle',\n",
    "        args = ['visible', [False] * len(data)],\n",
    "    )\n",
    "    step['args'][1][i] = True # Toggle i'th trace to \"visible\"\n",
    "    steps.append(step)\n",
    "\n",
    "sliders = [dict(\n",
    "    active = 10,\n",
    "    currentvalue = {\"prefix\": \"Frequency: \"},\n",
    "    pad = {\"t\": 50},\n",
    "    steps = steps\n",
    ")]\n",
    "\n",
    "layout = dict(sliders=sliders)\n",
    "fig = dict(data=data, layout=layout)\n",
    "\n",
    "py.iplot(fig, filename='Sine Wave Slider')"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}