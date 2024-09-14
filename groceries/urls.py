from django.urls import path

from groceries.views import (
    ShopSectionList,

    Items,
    ItemDetail,

    ShoppingLists,
    ShoppingListDetail,
)


app_name = 'groceries'


urlpatterns = [
    path('shop_sections/', ShopSectionList.as_view()),

    path('items/', Items.as_view()),
    path('items/<int:pk>', ItemDetail.as_view()),

    path('shopping_lists/', ShoppingLists.as_view()),
    path('shopping_lists/<int:pk>', ShoppingListDetail.as_view()),
]