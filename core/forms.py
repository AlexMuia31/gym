from django import forms
    
class Subscribe(forms.Form):
    Name= forms.CharField(max_length=20)
    Email = forms.EmailField()
    Message = forms.Textarea()



    def __str__(self):
        return self.Email