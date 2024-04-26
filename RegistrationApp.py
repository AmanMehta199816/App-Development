#!/usr/bin/env python
# coding: utf-8


import kivy


# In[3]:


from kivy.app import App


# In[4]:


from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import textinput
from kivy.uix.button import Button
from kivy.uix.popup import Popup


# In[ ]:


class RegistrationApp(App):
    def build(self):
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

    def register(self, instance):
        #Collect Information
        name=self.name_input.text
        email=self.email_input.text
        password= self.password_input.text
        confirm_password=self.confirm_input.text
        #Validation
        if name.strip()=='' pr email.strip()=='' or password.strip=='' or confirm_password.strip=='':message="Please fill in all fields"
        elif password !=confirm_password:
            message="Passwords do not match"

        else:
            filename=name+'.txt'
            with open(filename,'w') as file:
                file.write('Name'{}\n'.format(name))
                file.write('Email'{}\n'.format(email))
                file.write('Password'{}\n'.format(password))
            message="Registration successfull\nName: {}\Email: {}".format(name, email)

        #Popup
        popup=Popup(title= "Registration Status", content=Label(text=message), size_hint=(None, None),size=(400, 200))
        popup.open()


# In[ ]:


if __name__=='__main__':
    RegistrationApp().run()


# In[ ]:





# In[ ]:




