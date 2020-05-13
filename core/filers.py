import django_filters
from .models import Book
from django import forms


# class BookFilter(django_filters.FilterSet):

#     title = django_filters.CharFilter(lookup_expr='icontains')
      
#     def __init__(self, data=None, queryset=None, *, request=None, prefix=None):
#         super(BookFilter, self).__init__(data=data, queryset=queryset, request=request, prefix=prefix)
#         self.filters['genre'].field.widget.attrs.update({
#         'class':"custom-select mr-sm-2"
#         })
#         self.filters['tradeType'].field.widget.attrs.update({
#         'class':"custom-select mr-2"
#         }) 
#         self.filters['title'].field.widget.attrs.update({
#         'class':"form-control mr-sm-2",
#         'type':"text",
#         'name':"TorA",
#         'placeholder':"Cherchez par titre",
#         'id':"formGroupExampleInputMD"
#         })  

#     class Meta:
#         model = Book
#         fields = ('tile', 'genre', 'tradeType')


class BFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = Book
        fields = {
            'title', 'genre', 'tradeType',
        }
    def __init__(self, data, *args, **kwargs):
        data = data.copy()
        data.setdefault('format', 'paperback')
        data.setdefault('order', '-added')
        super(BFilter, self).__init__(data, *args, **kwargs)
        self.filters['genre'].field.widget.attrs.update({
        'class':"custom-select mr-sm-2"
        })
        self.filters['tradeType'].field.widget.attrs.update({
        'class':"custom-select mr-2"
        }) 
        self.filters['title'].field.widget.attrs.update({
        'class':"form-control mr-sm-2",
        'type':"text",
        'name':"TorA",
        'placeholder':"Cherchez par titre",
        'id':"formGroupExampleInputMD"
        })  