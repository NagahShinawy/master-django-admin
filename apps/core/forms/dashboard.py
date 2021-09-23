from django import forms
from apps.materadmin.models import Developer, DeveloperLevels


class DeveloperModelForm(forms.ModelForm):
    dev_name = forms.CharField(max_length=256, label="DeveloperForm Name", required=False, min_length=9)
    dev_level = forms.ChoiceField(
        choices=DeveloperLevels.choices,
        label="ExpForm Level",
        required=False,
    )
    dev_salary = forms.IntegerField(label="DevForm Salary", required=False)

    class Meta:
        model = Developer
        fields = "__all__"
