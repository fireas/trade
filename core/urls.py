from django.urls import path
from django.conf.urls.static import static
from .views import *


app_name = 'core'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('checkout', checkout_view, name='checkout'),
    path('mybooks/addbook', addBook_view, name='addbook'),
    path('mybooks', MyBooksView.as_view(), name='mybooks'),
    path('book/<pk>/', BookDetailView.as_view(), name='book'),
    path('mybooks/<pk>/modify', BookModifyView.as_view(), name='modifybook')
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)