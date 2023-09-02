from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets, filters

from .models import Video, Tag, Performer, Maker, Label, Series, Kyounuki, Contents, ContentsTag
from .serializers import VideoSerializer, ThumbnailSerializer, TagSerializer, SeriesSerializer, LabelSerializer, MakerSerializer, PerformerSerializer, KyounukiSerializer, ContentsSerializer, ContentsTagSerializer
from .serializers import GetVideoSerializer, GetThumbnailSerializer, GetTagSerializer, GetSeriesSerializer, GetLabelSerializer, GetMakerSerializer, GetPerformerSerializer, GetKyounukiSerializer, GetContentsSerializer, GetContentsTagSerializer

from django.db import models

from .models import Test
from .serializers import TestSerializer, GetUrlSerializer, PerformerSerializer

from rest_framework.generics import UpdateAPIView
from rest_framework.mixins import UpdateModelMixin
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from rest_framework.viewsets import ViewSetMixin

from .serializers import UrlPerformerSerializer, UrlTagSerializer, UrlMakerSerializer, UrlLabelSerializer, UrlSeriesSerializer, UrlKyounukiSerializer, UrlVideoSerializer, UpdateVideoSerializer
from .serializers import CreateVideoSerializer, CreatePerformerSerializer


from rest_framework import status
from rest_framework import filters
from rest_framework import generics


class DefaultAIPView(viewsets.ModelViewSet):
    queryset = None
    serializer_class = None
    # def create(self, request):
    #     serializer = VideoSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=201)
    #     return Response(serializer.errors, status=400)






class TestAPIView(DefaultAIPView):
    queryset = Test.objects.all()
    serializer_class = TestSerializer

class GetUrlAPIView(viewsets.ViewSet):
    def list(self, request):
        videos = Video.objects.all()
        performers = Performer.objects.all()
        tags = Tag.objects.all()
        makers = Maker.objects.all()
        labels = Label.objects.all()
        seriess = Series.objects.all()
        kyounukis = Kyounuki.objects.all()
        print("■■■■■■■■■■■■■■")
        video_serializer = UrlVideoSerializer(videos, many=True)
        performer_serializer = UrlPerformerSerializer(performers, many=True)
        tag_serializer = UrlTagSerializer(tags, many=True)
        maker_serializer = UrlMakerSerializer(makers, many=True)
        label_serializer = UrlLabelSerializer(labels, many=True)
        series_serializer = UrlSeriesSerializer(seriess, many=True)
        kyounuki_serializer = UrlKyounukiSerializer(kyounukis, many=True)

        data = {
            'video': video_serializer.data,
            'performer': performer_serializer.data,
            'tag': tag_serializer.data,
            'maker': maker_serializer.data,
            'label': label_serializer.data,
            'series': series_serializer.data,
            'kyounuki': kyounuki_serializer.data,
        }
        return Response(data)
    

class Video2APIView(DefaultAIPView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    filterset_fields = ['productnumber']
class VideoAPIView(viewsets.ViewSet):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    filterset_fields = ['productnumber']
    # def list(self, request):
    #     print("■■■■■■■■2")
    #     video_productnumber = request.GET.get('productnumber')
    #     try:
    #         get_video = Video.objects.get(productnumber=video_productnumber)
    #         print("■■■■", get_video.performers)
    #         if get_video.pk:pk = get_video.pk
    #         else: pk = ""
    #         if get_video.performers.exists():
    #             performers = list(get_video.performers.all())
    #             performers_name = performers[0].name
    #             for performer in performers[1:]:
    #                 performers_name = f"{performers_name}, {performer.name}"
    #             print("■■■■", get_video.performers)
    #         else: performers_name=""
    #         if get_video.maker:maker = get_video.maker.name
    #         else: maker = ""
    #         if get_video.label:label = get_video.label.name
    #         else: label = ""
    #         if get_video.series:series = get_video.series.name
    #         else: series=""
    #         if get_video.tags.exists():
    #             tags = list(get_video.tags.all())
    #             tags_name = tags[0].name
    #             if len(tags) > 1:
    #                 for tag in tags[1:]:
    #                     tags_name = f"{tags_name}, {tag.name}"
    #                 print("■■■■", get_video.tags)
    #         else: tags_name=""
    #         if get_video.duration:duration = get_video.duration
    #         else: duration=""
    #         if get_video.producturl:producturl = get_video.producturl
    #         else: producturl = ""
    #         if get_video.productimage:productimage = get_video.productimage
    #         else: productimage = ""
    #         if get_video.productsumple:productsumple = get_video.productsumple
    #         else: productsumple = ""
    #         if get_video.productthumbnail:productthumbnail = get_video.productthumbnail
    #         else: productthumbnail = ""
    #         if get_video.images:
    #             images = get_video.images
    #             # 文字列内の不要なスペースを削除
    #             images = images.replace(" ", "")
    #             # 文字列内のシングルクオートを削除
    #             images = images.replace("'", "")
    #             # []を削除
    #             images = images.replace("[","")
    #             images = images.replace("]","")
    #             # カンマを置き換えて、要素ごとに区切る
    #             images = images.replace(",",", ")
    #             print(images)
    #         else:images=""
    #         if get_video.title:title = get_video.title
    #         else: title=""
    #         if get_video.description:description = get_video.description
    #         else: description="00:00:00"
    #         if get_video.views:views = get_video.views
    #         else: views=0
    #         if get_video.kyounuki_post_day:kyounuki_post_day = get_video.kyounuki_post_day
    #         else: kyounuki_post_day="1999-01-01"
    #         if get_video.active:active = get_video.active
    #         else:active=False






    #         data = {
    #             "id": pk,
    #             # "performers": None,
    #             # "maker": maker,
    #             # "label": label,
    #             # "series": series,
    #             # "tags": None,
    #             # "duration": duration,
    #             # "producturl": producturl,
    #             # "productimage": productimage,
    #             # "productsumple": productsumple,
    #             # "productthumbnail": productthumbnail,
    #             # "images": images,
    #             # "title": title,
    #             # "description": description,
    #             # "views": views,
    #             # "kyounuki_post_day": kyounuki_post_day,
    #             # "active": active,
    #             # "thumbnails": []
    #         }
    #         return Response(data)
    #     except Video.DoesNotExist:
    #         return Response(status=status.HTTP_404_NOT_FOUND)
    def list(self, request):
        serializer = self.serializer_class(self.queryset, many=True)
        return Response(serializer.data)

    
class UpdateVideoAPIView(viewsets.ModelViewSet):
    queryset = Video.objects.all()
    serializer_class = UpdateVideoSerializer
    filterset_fields = ['productnumber']

    def update(self, request, *args, **kwargs):
        instance = self.get_object()  # 現在のオブジェクトを取得
        print("■■■■■■■■■■■")
        print(instance)
        # リクエストデータをシリアライザでデシリアライズし、更新します
        serializer = self.get_serializer(instance, data=request.data, partial=True)

        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        print("■■■■■■■■■■■■■■■■■■■■■■■■")
        #todo anything
        instance = self.get_object()
        serializer = self.get_serializer(instance)

        # Performersフィールドの値を変更する
        performers_list = [performer.name for performer in instance.performers.all()]
        tags_list = [tag.name for tag in instance.tags.all()]

        serializer_data = serializer.data
        serializer_data["performers"] = performers_list
        serializer_data["tags"] = tags_list
        return Response(serializer_data)

    # def list(self, request, *args, **kwargs):
    #     videos = Video.objects.all()
    #     performers = Performer.objects.all()
    #     tags = Tag.objects.all()
    #     makers = Maker.objects.all()
    #     labels = Label.objects.all()
    #     seriess = Series.objects.all()
    #     kyounukis = Kyounuki.objects.all()
    #     print("■■■■■■■■■■■■■■")
    #     video_serializer = UrlVideoSerializer(videos, many=True)
    #     performer_serializer = UrlPerformerSerializer(performers, many=True)
    #     tag_serializer = UrlTagSerializer(tags, many=True)
    #     maker_serializer = UrlMakerSerializer(makers, many=True)
    #     label_serializer = UrlLabelSerializer(labels, many=True)
    #     series_serializer = UrlSeriesSerializer(seriess, many=True)
    #     kyounuki_serializer = UrlKyounukiSerializer(kyounukis, many=True)

    #     data = {
    #         'video': video_serializer.data,
    #         'performer': performer_serializer.data,
    #         'tag': tag_serializer.data,
    #         'maker': maker_serializer.data,
    #         'label': label_serializer.data,
    #         'series': series_serializer.data,
    #         'kyounuki': kyounuki_serializer.data,
    #     }
    #     return Response(data)


    



    
    # def get_serializer_class(self):
    #     if self.action == 'retrieve':
    #         return PerformerSerializer  # Performersをカスタマイズしたシリアライザ
    #     return TestVideoSerializer    # 通常のシリアライザ

        
    # filterset_fields = ['productnumber']
    # def list(self, request):
    #     print("■■■■■■■■")
    #     video_productnumber = request.GET.get('productnumber')
    #     try:

    #         # get_video = Video.objects.get(productnumber=video_productnumber)
    #         get_video = Video.objects.get(id=1)

    #         if get_video.pk:pk = get_video.pk
    #         else: pk = ""
    #         if get_video.performers.exists():
    #             performers = list(get_video.performers.all())
    #             performers_name = performers[0].name
    #             for performer in performers[1:]:
    #                 performers_name = f"{performers_name}, {performer.name}"
    #         else: performers_name=""
    #         if get_video.maker:maker = get_video.maker.name
    #         else: maker = ""
    #         if get_video.label:label = get_video.label.name
    #         else: label = ""
    #         if get_video.series:series = get_video.series.name
    #         else: series=""
    #         if get_video.tags.exists():
    #             tags = list(get_video.tags.all())
    #             tags_name = tags[0].name
    #             if len(tags) > 1:
    #                 for tag in tags[1:]:
    #                     tags_name = f"{tags_name}, {tag.name}"
    #                 print("■■■■", get_video.tags)
    #         else: tags_name=""
    #         if get_video.duration:duration = get_video.duration
    #         else: duration=""
    #         if get_video.producturl:producturl = get_video.producturl
    #         else: producturl = ""
    #         if get_video.productimage:productimage = get_video.productimage
    #         else: productimage = ""
    #         if get_video.productsumple:productsumple = get_video.productsumple
    #         else: productsumple = ""
    #         if get_video.productthumbnail:productthumbnail = get_video.productthumbnail
    #         else: productthumbnail = ""
    #         print("■■■■■■■■")

    #         if get_video.images:
    #             images = get_video.images
    #             # 文字列内の不要なスペースを削除
    #             images = images.replace(" ", "")
    #             # 文字列内のシングルクオートを削除
    #             images = images.replace("'", "")
    #             # []を削除
    #             images = images.replace("[","")
    #             images = images.replace("]","")
    #             # カンマを置き換えて、要素ごとに区切る
    #             images = images.replace(",",", ")
    #             print(images)
    #         else:images=""
    #         if get_video.title:title = get_video.title
    #         else: title=""
    #         if get_video.description:description = get_video.description
    #         else: description="00:00:00"
    #         if get_video.views:views = get_video.views
    #         else: views=0
    #         if get_video.kyounuki_post_day:kyounuki_post_day = get_video.kyounuki_post_day
    #         else: kyounuki_post_day="1999-01-01"
    #         if get_video.active:active = get_video.active
    #         else:active=False



    #         data = {
    #             "id": pk,
    #             "performers": performers_name,
    #             "maker": maker,
    #             "label": label,
    #             "series": series,
    #             "tags": tags_name,
    #             "duration": duration,
    #             "producturl": producturl,
    #             "productimage": productimage,
    #             "productsumple": productsumple,
    #             "productthumbnail": productthumbnail,
    #             "images": images,
    #             "title": title,
    #             "description": description,
    #             "views": views,
    #             "kyounuki_post_day": kyounuki_post_day,
    #             "active": active,
    #             "thumbnails": []
    #         }
    #         return Response(data)
    #     except Video.DoesNotExist:
    #         return Response(status=status.HTTP_404_NOT_FOUND)

    # def update(self, request):

    #     return
    
# class TestVideoAPIView(generics.RetrieveUpdateAPIView):
#     queryset = Video.objects.all()
#     serializer_class = TestVideoSerializer
#     # lookup_field = 'productnumber'
#     def list(self, request):
#         return

#     def update(self, request, *args, **kwargs):
#         instance = self.get_object()  # 現在のデータを取得
#         # 更新ロジックを実装
#         # ...

# #         return super().update(request, *args, **kwargs)
class CreateVideoAPIView(viewsets.ModelViewSet):
    queryset = Video.objects.all()
    serializer_class = CreateVideoSerializer
    filterset_fields = ['productnumber']

    def update(self, request, *args, **kwargs):
        instance = self.get_object()  # 現在のオブジェクトを取得
        print("■■■■■■■■■■■")
        print(instance)
        # リクエストデータをシリアライザでデシリアライズし、更新します
        serializer = self.get_serializer(instance, data=request.data, partial=True)

        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        print("■■■■■■■■■■■■■■■■■■■■■■■■")
        #todo anything
        instance = self.get_object()
        serializer = self.get_serializer(instance)

        # Performersフィールドの値を変更する
        performers_list = [performer.name for performer in instance.performers.all()]
        tags_list = [tag.name for tag in instance.tags.all()]

        serializer_data = serializer.data
        serializer_data["performers"] = performers_list
        serializer_data["tags"] = tags_list
        return Response(serializer_data)
    





class GetVideoAPIView(DefaultAIPView):
    queryset = Video.objects.all()
    serializer_class = GetVideoSerializer

class PerformerAPIView(DefaultAIPView):
    queryset = Performer.objects.all()
    serializer_class = PerformerSerializer
class GetPerformerAPIView(DefaultAIPView):
    queryset = Performer.objects.all()
    serializer_class = GetPerformerSerializer
class CreatePerformerAPIView(DefaultAIPView):
    queryset = Performer.objects.all()
    serializer_class = CreatePerformerSerializer

class TagAPIView(DefaultAIPView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
class GetTagAPIView(DefaultAIPView):
    queryset = Tag.objects.all()
    serializer_class = GetTagSerializer

class MakerAPIView(DefaultAIPView):
    queryset = Maker.objects.all()
    serializer_class = MakerSerializer
class GetMakerAPIView(DefaultAIPView):
    queryset = Maker.objects.all()
    serializer_class = GetMakerSerializer

class LabelAPIView(DefaultAIPView):
    queryset = Label.objects.all()
    serializer_class = LabelSerializer
class GetLabelAPIView(DefaultAIPView):
    queryset = Label.objects.all()
    serializer_class = GetLabelSerializer

class SeriesAPIView(DefaultAIPView):
    queryset = Series.objects.all()
    serializer_class = SeriesSerializer
class GetSeriesAPIView(DefaultAIPView):
    queryset = Series.objects.all()
    serializer_class = GetSeriesSerializer

class KyounukiAPIView(DefaultAIPView):
    queryset = Kyounuki.objects.all()
    serializer_class = KyounukiSerializer
class GetKyounukiAPIView(DefaultAIPView):
    queryset = Kyounuki.objects.all()
    serializer_class = GetKyounukiSerializer

class ContentsAPIView(DefaultAIPView):
    queryset = Contents.objects.all()
    serializer_class = ContentsSerializer
class GetContentsAPIView(DefaultAIPView):
    queryset = Contents.objects.all()
    serializer_class = GetContentsSerializer

class ContentsTagAPIView(DefaultAIPView):
    queryset = ContentsTag.objects.all()
    serializer_class = ContentsTagSerializer
class GetContentsTagAPIView(DefaultAIPView):
    queryset = ContentsTag.objects.all()
    serializer_class = GetContentsTagSerializer



# VideoSerializer, ThumbnailSerializer, TagSerializer, SeriesSerializer, LabelSerializer, MakerSerializer, PerformerSerializer
