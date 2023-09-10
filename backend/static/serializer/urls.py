from django.urls import path
# from .views import VideoViewSet


from django.urls import include, path

# from .rest_framework_api import router



from rest_framework import routers
# from .views import VideoCreateView, VideoAPIView
from .views import VideoAPIView ,MakerAPIView ,LabelAPIView ,SeriesAPIView ,PerformerAPIView ,KyounukiAPIView, TagAPIView, UpdateVideoAPIView, ContentsAPIView, ContentsTagAPIView
from .views import GetVideoAPIView ,GetMakerAPIView ,GetLabelAPIView ,GetSeriesAPIView ,GetPerformerAPIView ,GetKyounukiAPIView, GetTagAPIView, GetContentsAPIView, GetContentsTagAPIView
from .views import TestAPIView, GetUrlAPIView, Video2APIView
from .views import CreateVideoAPIView, CreatePerformerAPIView

router = routers.DefaultRouter()
# router.register('videos_list', VideoAPIView, basename='video')
router.register('performer_list', PerformerAPIView, basename='performer_list')
router.register('kyounuki_list', KyounukiAPIView, basename='kyounuki_list')
router.register('maker_list', MakerAPIView, basename='maker_list')
router.register('label_list', LabelAPIView, basename='label_list')
router.register('series_list', SeriesAPIView, basename='series_list')
router.register('tag_list', TagAPIView, basename='tag_list')
router.register('test_list', TestAPIView, basename='test_list')
router.register('contents_list', ContentsAPIView, basename='contents_list')
router.register('contentstag_list', ContentsTagAPIView, basename='contentstag_list')


router.register('videos_view', GetVideoAPIView, basename='videos_view')
router.register('performer_list_view', GetPerformerAPIView, basename='performer_list_view')
router.register('kyounuki_list_view', GetKyounukiAPIView, basename='kyounuki_list_view')
router.register('maker_list_view', GetMakerAPIView, basename='maker_list_view')
router.register('label_list_view', GetLabelAPIView, basename='label_list_view')
router.register('series_list_view', GetSeriesAPIView, basename='series_list_view')
router.register('tag_list_view', GetTagAPIView, basename='tag_list_view')
router.register('contents_list_view', ContentsAPIView, basename='contents_list_view')
router.register('contentstag_list_view', ContentsTagAPIView, basename='contentstag_list_view')


router.register('videos_update', UpdateVideoAPIView, basename='videos_update')
    
router.register('videos_create', CreateVideoAPIView, basename='videos_create')
router.register('performer_create', CreatePerformerAPIView, basename='performer_create')



# router.register('url_list_view', GetUrlAPIView.as_view({'get': 'list'}), basename='url_list_view')
# router.register('url_list_view', GetUrlAPIView, basename='url_list_view')



# router.register('test_list_view', GetTestAPIView, basename='test_list_view')






# router.register(r'entries', VideoAPIView)


urlpatterns = [
    path('api/', include(router.urls) ),
    path('api/url_list_view/', GetUrlAPIView.as_view({'get': 'list'}), name='url_list_view'),
    path('api/videos/', VideoAPIView.as_view({'get': 'list'}), name='video3'),




    # 他のURLパターンを追加する
    # ...
]