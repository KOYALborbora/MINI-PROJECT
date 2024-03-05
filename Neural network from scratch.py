#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd


# In[8]:


# 3 neurons with 4 inputs


# In[21]:


inputs = [1,2,3,2.5]


# In[22]:


weights21 = [0.2,0.8,-0.5,1.0]


# In[23]:


weights22 = [0.5,-0.91,0.26,-0.5]


# In[24]:


weights23 = [-0.26,-0.27,0.17,0.07]


# In[25]:


bias21 = 2


# In[26]:


bias22 = 3


# In[15]:


bias23 = 0.5


# In[27]:


output =[inputs[0]*weights21[0]+inputs[1]*weights21[1]+inputs[2]*weights21[2]+inputs[3]*weights21[3]+bias21 , inputs[0]*weights22[0]+inputs[1]*weights22[1]+inputs[2]*weights22[2]+inputs[3]*weights22[3]+bias22 ,inputs[0]*weights23[0]+inputs[1]*weights23[1]+inputs[2]*weights23[2]+inputs[3]*weights23[3]+ bias23]


# In[28]:


print(output)


# In[29]:


#standard way


# In[30]:


weights = [ [0.2,0.8,-0.5,1.0], [0.5,-0.91,0.26,-0.5],[-0.26,-0.27,0.17,0.07]]


# In[31]:


biases = [2,3,0.5]


# In[32]:


layer_outputs =[] #output of current layer
for neuron_weights, neuron_bias in zip(weights,biases):
    neuron_output = 0 3 #output of given neuron
    for n_inputs, weights in zip(inputs, neuron_weights):
        neuron_output += n_input*weight
    neuron_output += neuron_bias
    layer_outputs.append(neuron_output)
print(layer_outputs)


# In[ ]:




