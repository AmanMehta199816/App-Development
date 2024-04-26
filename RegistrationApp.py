#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install kivy


# In[2]:


import kivy


# In[3]:


from kivy.app import App


# In[4]:


from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import textinput
from kivy.uix.button import Button


# In[ ]:


class RegistrationApp(App):
    def buid(self):
        self.title="Registration Form"
        layout = BoxLayout(orientation='vertical', padding=30, spacing=10)
        head_label=Label(text="Python user Registration App", font_size=26, bold=True,height=40)
        
        #Adding label 
        name_label=Label(text="Name", font_size=18)
        self.name_input=TextInput(multilines=false,font_size=18)
        
        email_label=Label(text="Email", font_size=18)
        self.email_input=TextInput()
       
        password_label=Label(text="Password", font_size=18, password=True)
        self.password_input=TextInput()
        
        confirm_label=Label(text="Confirm", font_size=18, password= True)
        self.confirm_input=TextInput()
        
        #button
        submit_button=Button(text='Register', fornt_size=18,)
        layout.add_widget(head_label)
        layout.add_widget(name_label)
        layout.add_widget(self.name_input)
        layout.add_widget(email_label)
        layout.add_widget(self.email_label)
        layout.add_widget(password_label)
        layout.add_widget(self.password_label)
        layout.add_widget(confirm_label)
        layout.add_widget(self.confirm_label)
        layout.add_widget(submit button)
           
        
        return layout


# In[ ]:


if __name__=='__main__':
    RegistrationApp().run()


# In[ ]:





# In[ ]:




