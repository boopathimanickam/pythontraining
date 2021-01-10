#!/usr/bin/env python
# coding: utf-8

# In[3]:


print("hello boopathi")


# In[5]:


print('welcome boopathi')


# In[6]:


print("Hello Boopathi")


# In[7]:


print("a String", 1, 2.1, 3+10, b'\x06 \x41 \x42')


# In[11]:


print('welcome'+'boopathi')


# In[12]:


print(welcome+boopathi)


# In[13]:


x='welcome raja'
y=4
z=4
globals ()
y is z 


# In[14]:


x='welcome raja'
y=4
z=4
globals ()
y is x


# In[15]:


type(1)


# In[16]:


type('hello')


# In[18]:


x="hello"
type(x)


# In[1]:


type(1)



# In[2]:


print ("hello"+"Boopathi")


# In[4]:


type('hello')


# In[5]:


x='hello'
type(x)


# In[6]:


some_value=10
some_value=some_value+10
print(some_value)


# In[7]:


a=100
str(a)


# In[11]:


a=float(100)
a


# In[12]:


type(a)


# In[13]:


int(100.09)


# In[14]:


5+int(5)


# In[16]:


str(6)+"5"


# In[18]:


x=10
x=x+5
x


# In[19]:


x=x-5
x


# In[20]:


x=x*5
x


# In[21]:


x=x/2
x


# In[22]:


x=x//2
x


# In[23]:


x=x%12
x


# In[24]:


x=2
x=x%2
x


# In[25]:


x=5
x=x%2
x


# In[26]:


x=5
x=x**2
x


# In[27]:


(1+2)*3


# In[28]:


1+2*3


# In[30]:


a=0xff00
a


# In[31]:


hex(a)


# In[33]:


b=0b11000101
b=int("11000101",2)
b


# In[34]:


bin(b)


# In[35]:


a="this is a test"
print(a)


# In[44]:


a="this is a \"test\""
print(a)


# In[46]:


num=3
astr="First{} Second{} Third{}".format('X',2,num)
astr


# In[47]:


astr="First{0} Second{0} Third{0}".format('X',2,num)
astr


# In[48]:


astr="First{2} Second{0} Third{1}".format('X',2,num)
astr


# In[51]:


astr="First{item1} Second{item2} Third{item3}".format(item1='X',item2=2,item3=5)
astr


# In[52]:


"Center 20 wide [{0: ^20}]".format("centered")


# In[53]:


"Center 20 wide [{0: <20}]".format("centered")


# In[56]:


"Center 20 wide [{0:<20}]".format("3.14")


# In[65]:


"Center 20 wide {0:0<8.3f}".format(3.14)


# In[69]:


"Center 20 wide {0:>8.3f}".format(3.14)


# In[70]:


"Center 20 wide {0:+8.3f}".format(3.14)


# In[73]:


"Center 20 wide {0:-8.3f}".format(255)


# In[72]:


"Center 20 wide {0:8.3f}".format(3.14)


# In[77]:


"Center 20 wide {0:0>10X}".format(255)


# In[78]:


"Center 20 wide {0:0>8b}".format(85)


# In[79]:


"String %s Decimal %d" % ("HI!",100)


# In[82]:


"String Decimal %10f" % (100)


# In[84]:


"String Decimal [%10s]" % ("Hi".center(10))


# In[ ]:




