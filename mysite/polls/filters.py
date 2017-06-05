import django_filters
from .models import Expense
from django import forms





class DateInput(forms.DateInput):
    input_type = 'date'


class ExpenseFilter(django_filters.FilterSet):

    shift_date = django_filters.DateTimeFromToRangeFilter(label='Date Range: YYYY-MM-DD')


    class Meta:
        model = Expense

        fields = ['company', 'shift_date']

        exclude = ['additional_cost', 'total_hours', 'description', 'pay_rate']
