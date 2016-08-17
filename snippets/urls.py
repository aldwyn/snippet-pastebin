from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
# from rest_framework.urlpatterns import format_suffix_patterns
# from rest_framework import renderers
# from .views import UserViewSet, SnippetViewSet, api_root
from .views import UserViewSet, SnippetViewSet


router = DefaultRouter(schema_title='Pastebin API')
router.register(r'snippets', SnippetViewSet)
router.register(r'users', UserViewSet)

# snippet_list = SnippetViewSet.as_view({
#     'get': 'list',
#     'post': 'create'
# })
# snippet_detail = SnippetViewSet.as_view({
#     'get': 'retrieve',
#     'put': 'updated',
#     'patch': 'partial_update',
#     'delete': 'destroy'
# })
# snippet_highlight = SnippetViewSet.as_view({
#     'get': 'highlight'
# }, renderer_classes=[renderers.StaticHTMLRenderer])
# user_list = UserViewSet.as_view({
#     'get': 'list'
# })
# user_detail = UserViewSet.as_view({
#     'get': 'retrieve'
# })

# urlpatterns = format_suffix_patterns([
#     url(r'^$', api_root),
#     url(r'^users/$', user_detail, name='user-detail'),
#     url(r'^users/(?P<pk>[0-9]+)/$', user_list, name='user-list'),
#     url(r'^snippets/$', snippet_list, name='snippet-list'),
#     url(r'^snippets/(?P<pk>[0-9]+)/$', snippet_detail, name='snippet-detail'),
#     url(r'^snippets/(?P<pk>[0-9]+)/highlight/$', snippet_highlight, name='snippet-highlight'),
# ])

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls')),
]