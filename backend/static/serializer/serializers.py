from rest_framework import serializers
from .models import Video, Performer, Maker, Label, Series, Tag, Thumbnail, Kyounuki, Test, Contents, ContentsTag
from django.core.exceptions import ObjectDoesNotExist
from django.apps import apps
import datetime
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError
from django.db.models import Q


import re
import json
import requests
from bs4 import BeautifulSoup

import pykakasi

def convert_to_romaji(text):
    kakasi = pykakasi.kakasi()
    kakasi.setMode("H", "a")        # Hiragana to ascii
    kakasi.setMode("K", "a")        # Katakana to ascii
    kakasi.setMode("J", "a")        # Japanese to ascii
    kakasi.setMode("r", "Hepburn")  # use Hepburn Roman table
    kakasi.setMode("s", True)       # add space
    kakasi.setMode("C", False)      # no capitalize
    conv = kakasi.getConverter()
    result = conv.do(text)
    return result

def get_duration_info(text):
    duration_info = int(re.search(r'\d+', text).group())
    hours = str(duration_info // 60)
    remaining_minutes = str(duration_info % 60)
    duration_info = f"{hours}:{remaining_minutes}:00"
    return duration_info

def calculate_age(birth_date):
    today = datetime.datetime.now()
    birth_year = birth_date.year
    birth_month = birth_date.month
    birth_day = birth_date.day

    age = today.year - birth_year

    if (today.month < birth_month) or (today.month == birth_month and today.day < birth_day):
        age -= 1

    return age


# ■■■■■■■■■■■■■■■■■■
# ■■■　Performer　■■■
# ■■■■■■■■■■■■■■■■■■
class PerformerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Performer
        fields = '__all__'
class GetPerformerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Performer
        fields = ["name", "name_eng", "birth", "age"]
    def create(self, validated_data):
        # レコード作成を禁止するため、何も処理せずに例外を発生させます
        raise serializers.ValidationError("Creating records is not allowed.")
class CreatePerformerSerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=False, read_only=True)
    birth = serializers.CharField(required=False, read_only=True)
    age = serializers.CharField(required=False, read_only=True)
    name_eng = serializers.CharField(required=False, read_only=True)
    def create(self, validated_data):
        birth_info = validated_data.get('birth')
        age = calculate_age(birth_info)
        validated_data["age"] = age
        performer = Performer.objects.create(**validated_data)
        return performer
    class Meta:
        model = Performer
        fields = '__all__'



# ■■■■■■■■■■■■■■■■■■
# ■■■　Tag　■■■
# ■■■■■■■■■■■■■■■■■■
class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'
class GetTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ["name", "name_eng"]
    def create(self, validated_data):
        # レコード作成を禁止するため、何も処理せずに例外を発生させます
        raise serializers.ValidationError("Creating records is not allowed.")
    
# ■■■■■■■■■■■■■■■■■■
# ■■■　Maker　■■■
# ■■■■■■■■■■■■■■■■■■
class MakerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Maker
        fields = '__all__'
    def create(self, validated_data):
        name_data = validated_data.pop('name', None)
        name_eng_data = validated_data.pop('name_eng', None)
        if name_eng_data != "": 
            validated_data["name_eng"] = name_eng_data
        else:
            name_eng_data = convert_to_romaji(name_data).lower()
            validated_data["name_eng"] = name_eng_data
            validated_data["name"] = name_data
        create_obj = Maker.objects.create(**validated_data)
        return create_obj
class GetMakerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Maker
        fields = ["name", "name_eng"]
    def create(self, validated_data):
        # レコード作成を禁止するため、何も処理せずに例外を発生させます
        raise serializers.ValidationError("Creating records is not allowed.")

# ■■■■■■■■■■■■■■■■■■
# ■■■　Label　■■■
# ■■■■■■■■■■■■■■■■■■
class LabelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Label
        fields = '__all__'
    def create(self, validated_data):
        name_data = validated_data.pop('name', None)
        name_eng_data = validated_data.pop('name_eng', None)
        if name_eng_data != "": 
            validated_data["name_eng"] = name_eng_data
        else:
            name_eng_data = convert_to_romaji(name_data).lower()
            validated_data["name_eng"] = name_eng_data
            validated_data["name"] = name_data
        create_obj = Maker.objects.create(**validated_data)
        return create_obj
class GetLabelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Label
        fields = ["name", "name_eng"]
    def create(self, validated_data):
        # レコード作成を禁止するため、何も処理せずに例外を発生させます
        raise serializers.ValidationError("Creating records is not allowed.")

# ■■■■■■■■■■■■■■■■■■
# ■■■　Series　■■■
# ■■■■■■■■■■■■■■■■■■
class SeriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Series
        fields = '__all__'
    def create(self, validated_data):
        name_data = validated_data.pop('name', None)
        name_eng_data = validated_data.pop('name_eng', None)
        if name_eng_data != "": 
            validated_data["name_eng"] = name_eng_data
        else:
            name_eng_data = convert_to_romaji(name_data).lower()
            validated_data["name_eng"] = name_eng_data
            validated_data["name"] = name_data
        create_obj = Maker.objects.create(**validated_data)
        return create_obj
class GetSeriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Series
        fields = ["name", "name_eng"]
    def create(self, validated_data):
        # レコード作成を禁止するため、何も処理せずに例外を発生させます
        raise serializers.ValidationError("Creating records is not allowed.")

# ■■■■■■■■■■■■■■■■■■
# ■■■　Thumnails　■■■
# ■■■■■■■■■■■■■■■■■■
class ThumbnailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Thumbnail
        fields = '__all__'
class GetThumbnailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Thumbnail
        fields = '__all__'
    def create(self, validated_data):
        # レコード作成を禁止するため、何も処理せずに例外を発生させます
        raise serializers.ValidationError("Creating records is not allowed.")


class TestSerializer(serializers.ModelSerializer):
    # maker = MakerSerializer()
    maker = serializers.CharField(max_length=255)
    def create(self, validated_data):
        print("validated_data", validated_data)


        maker_data = validated_data.pop('maker', None)
        if maker_data:
            try:
                maker = Maker.objects.get(name=maker_data)
            except Maker.DoesNotExist:
                raise serializers.ValidationError('Maker does not exist.')
            validated_data['maker'] = maker
        

        return Test.objects.create(**validated_data)
 
    class Meta:
        model = Test
        fields = '__all__'




# ■■■■■■■■■■■■■■■■■■
# ■■■　URL　■■■
# ■■■■■■■■■■■■■■■■■■
class UrlPerformerSerializer(serializers.ModelSerializer):
    class Meta: model = Performer; fields = ["name", "name_eng"]
    def create(self, validated_data): raise serializers.ValidationError("Creating records is not allowed.")
class UrlTagSerializer(serializers.ModelSerializer):
    class Meta: model = Tag; fields = ["name", "name_eng"]
    def create(self, validated_data): raise serializers.ValidationError("Creating records is not allowed.")
class UrlMakerSerializer(serializers.ModelSerializer):
    class Meta: model = Maker; fields = ["name", "name_eng"]
    def create(self, validated_data): raise serializers.ValidationError("Creating records is not allowed.")
class UrlLabelSerializer(serializers.ModelSerializer):
    class Meta: model = Label; fields = ["name", "name_eng"]
    def create(self, validated_data): raise serializers.ValidationError("Creating records is not allowed.")
class UrlSeriesSerializer(serializers.ModelSerializer):
    class Meta: model = Series; fields = ["name", "name_eng"]
    def create(self, validated_data): raise serializers.ValidationError("Creating records is not allowed.")
class UrlKyounukiSerializer(serializers.ModelSerializer):
    class Meta: model = Kyounuki; fields = ['post_day']
    def create(self, validated_data): raise serializers.ValidationError("Creating records is not allowed.")
class UrlVideoSerializer(serializers.ModelSerializer):
    class Meta: model = Video; fields = ['productnumber']
    def create(self, validated_data): raise serializers.ValidationError("Creating records is not allowed.")
class GetUrlSerializer(serializers.Serializer):
    video = UrlVideoSerializer(many=True)
    performer = UrlPerformerSerializer(many=True)
    tag = UrlTagSerializer(many=True)
    maker = UrlMakerSerializer(many=True)
    label = UrlLabelSerializer(many=True)
    series = UrlSeriesSerializer(many=True)
    kyounuki = UrlKyounukiSerializer(many=True)
    class Meta:
        fields = '__all__'
    def create(self, validated_data):
        # レコード作成を禁止するため、何も処理せずに例外を発生させます
        raise serializers.ValidationError("Creating records is not allowed.")



# ■■■■■■■■■■■■■■■■■■
# ■■■　Video　■■■
# ■■■■■■■■■■■■■■■■■■
class VideoSerializer(serializers.ModelSerializer):
    performers = serializers.CharField(max_length=255)
    # performers = PerformerSerializer()
    # thumbnails = ThumbnailSerializer()
    maker = serializers.CharField(max_length=255, allow_null=True)
    label = serializers.CharField(max_length=255, allow_null=True)
    series = serializers.CharField(max_length=255, allow_null=True)
    tags = serializers.CharField(max_length=255, allow_null=True)
    duration = serializers.TimeField(format='%H:%M:%S', input_formats=['%H:%M:%S', '%H:%M'], default=datetime.time(0, 0, 0), allow_null=True)
    producturl = serializers.URLField(max_length=200, allow_null=True)
    images = serializers.CharField(max_length=1023)


    def create(self, validated_data):
        # ネストされたフィールドの作成手順を指定
        # performers_data = validated_data.pop('performers', [])

        thumbnails_data = validated_data.pop('thumbnails', [])
        # tags_data = validated_data.pop('tags', [])
        # maker_data = validated_data.pop('maker', None)
        # label_data = validated_data.pop('label', None)
        # series_data = validated_data.pop('series', None)

        # maker_name = maker_data.get('name') if maker_data else None
        # maker = Maker.objects.filter(name=maker_name).first()

        maker_data = validated_data.pop('maker', None)
        obj = self.duplicate_check("maker", maker_data)
        validated_data["maker"] = obj

        label_data = validated_data.pop('label', None)
        obj = self.duplicate_check("label", label_data)
        validated_data["label"] = obj

        series_data = validated_data.pop('series', None)
        obj = self.duplicate_check("series", series_data)
        validated_data["series"] = obj

        tags_data = validated_data.pop('tags', [])
        objs_tags = self.duplicate_check_loop("tag", tags_data)
        # validated_data["tags"] = objs

        performers_data = validated_data.pop('performers', [])
        objs_performers = self.duplicate_check_loop("performer", performers_data)
        # validated_data["performers"] = objs


        images_data = validated_data.pop('images', None)
        print(images_data)
        urls = images_data.split(",")
        objs_images = []
        for url in urls:
            objs_images.append(url)
        validated_data["images"] = objs_images

    

        video = Video.objects.create(**validated_data)

        video.tags.set(objs_tags)
        video.performers.set(objs_performers)


            

        return video


    # # Check for duplicate data 
    def duplicate_check(self, item, data):
        obj = None
        if data:
            ModelClass = apps.get_model(app_label="serializer", model_name=item)

            if ModelClass.objects.filter(name=data).exists():
                obj = ModelClass.objects.get(name=data)

                print(f"{item}: OK")
            else:
                raise serializers.ValidationError(f"{item.capitalize()} does not exist.")
                print("err")
        return obj
    
    def duplicate_check_loop(self, item, data):
        if ".None" in data:
            raise serializers.ValidationError(f"That {data} value does not exist in the {item.capitalize()} model.")
        objs = []
        obj = None
        err_flag = 0
        err_items = []
        ModelClass = apps.get_model(app_label="serializer", model_name=item)

        for data_item in data.split(","):
            data_item = data_item.strip()
            if data_item:
                ModelClass = apps.get_model(app_label="serializer", model_name=item)
                if ModelClass.objects.filter(name=data_item).exists():
                    obj = ModelClass.objects.get(name=data_item).id
                    print(f"{data_item}: OK")
                    objs.append(obj)
                else:
                    err_items.append(data_item)
                    err_flag=1
        if err_flag == 1:
            raise serializers.ValidationError(f"That {err_items} value does not exist in the {item.capitalize()} model.")
        return objs
    
    # # VALIDATE
    def validate_def(self, attrs, item):
        print("item_data", item, attrs)
        ModelClass = apps.get_model(app_label="serializer", model_name=item)

        # item_name = attrs.get("name", None)
        # print("attrs", item, attrs)
        # print("item_data", item, item_name)
        if attrs:
            # item_name = item_data.get('name')
            if ModelClass.objects.filter(name=attrs).exists():
                print(f"{item}: OK")
            else:
                raise serializers.ValidationError(f"That {attrs} value does not exist in the {item.capitalize()} model.")
        return attrs
    
    def validate_def_loop(self, attrs, item):
        if ".None" in attrs:
            return attrs

        print("item_data", item, attrs)
        ModelClass = apps.get_model(app_label="serializer", model_name=item)
        err_flag=0
        err_items = []
        for attrs_item in attrs.split(","):
            attrs_item = attrs_item.strip()
            if attrs_item:
                # item_name = item_data.get('name')
                print("■", attrs_item)
                if ModelClass.objects.filter(name=attrs_item).exists():
                    print(f"{attrs_item}: OK")
                else:
                    err_items.append(attrs_item)
                    err_flag=1
        if err_flag == 1:
            raise serializers.ValidationError(f"That {err_items} value does not exist in the {item.capitalize()} model.")
        return attrs

    def validate_maker(self, attrs):
        return self.validate_def(attrs, "maker")
    
    def validate_label(self, attrs):
        return self.validate_def(attrs, "label")
    
    def validate_series(self, attrs):
        return self.validate_def(attrs, "series")
    
    def validate_tags(self, attrs):
        return self.validate_def_loop(attrs, "tag")
    
    def validate_performers(self, attrs):
        return self.validate_def_loop(attrs, "performer")
    
    def validate_images(self, attrs):
        urls = attrs.split(",")
        url_validator = URLValidator()
        for url in urls:
            try:
                url_validator(url.strip())
            except ValidationError:
                # URLの形式が正しくない場合の処理
                print("■URL", url)
                raise serializers.ValidationError("Invalid URL format")
            
        return attrs
    
    def update(self, instance, validated_data):
        # バリデーション済みデータでインスタンスを更新します
        maker_data = validated_data.pop('maker', None)
        obj = self.duplicate_check("maker", maker_data)
        validated_data["maker"] = obj

        label_data = validated_data.pop('label', None)
        obj = self.duplicate_check("label", label_data)
        validated_data["label"] = obj

        series_data = validated_data.pop('series', None)
        obj = self.duplicate_check("series", series_data)
        validated_data["series"] = obj

        # tags_data = validated_data.pop('tags', [])
        # objs_tags = self.duplicate_check_loop("tag", tags_data)
        # validated_data["tags"] = objs

        # performers_data = validated_data.pop('performers', [])
        # objs_performers = self.duplicate_check_loop("performer", performers_data)
        # validated_data["performers"] = objs

        # print("instance.performers", instance.performers)
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        # instance.performers = validated_data.get('performers', instance.performers)
        instance.maker = validated_data.get('maker', instance.maker)
        instance.label = validated_data.get('label', instance.label)
        instance.series = validated_data.get('series', instance.series)
        # instance.tags = validated_data.get('tags', instance.tags)
        instance.duration = validated_data.get('duration', instance.duration)
        instance.producturl = validated_data.get('producturl', instance.producturl)

        images_data = validated_data.pop('images', [])
        urls = images_data.split(",")
        
        objs_images = []
        for url in urls:
            objs_images.append(url)
            print("objs_images", objs_images)
        # validated_data["images"] = objs_images
        # instance.images = validated_data.get('images', instance.images)
        instance.images = objs_images

        tags_data = validated_data.pop('tags', [])
        tags_data_result = self.duplicate_check_loop("tag", tags_data)
        # validated_data["tags"] = objs

        performers_data = validated_data.pop('performers', [])
        performers_data_result = self.duplicate_check_loop("performer", performers_data)

        instance.tags.set(tags_data_result)
        instance.performers.set(performers_data_result)


        print("instance.tags", instance.tags)
        print("instance.performers", instance.performers)
        # productnumber = validated_data.pop('productnumber', None)
        # videos = Video.objects.filter(productnumber=productnumber)
        # print("aaaaaaaaaaaaaaaaa")
        # if (videos):
        #     get_video, _ = Video.objects.get_or_create(productnumber=productnumber)
        #     if (validated_data["title"] != None) or (validated_data["title"] != []) or (validated_data["title"] != ""):get_video.title = validated_data["title"]
        #     if (validated_data["performers"] != None) or (validated_data["performers"] != []) or (validated_data["performers"] != "") :get_video.performers = validated_data["performers"] 
        #     if (validated_data["productnumber"] != None) or (validated_data["productnumber"] != []) or (validated_data["productnumber"] != "") :get_video.productnumber = validated_data["productnumber"] 
        #     # if (validated_data["maker"] != None) or (validated_data["maker"] != []) or (validated_data["maker"] != "") :get_video.maker = validated_data["maker"] 
        #     if (validated_data["label"] != None) or (validated_data["label"] != []) or (validated_data["label"] != "") :get_video.label = validated_data["label"] 
        #     if (validated_data["series"] != None) or (validated_data["series"] != []) or (validated_data["series"] != "") :get_video.series = validated_data["series"] 
        #     if (validated_data["description"] != None) or (validated_data["description"] != []) or (validated_data["description"] != "") :get_video.description = validated_data["description"] 
        #     if (validated_data["duration"] != None) or (validated_data["duration"] != []) or (validated_data["duration"] != "") :get_video.duration = validated_data["duration"] 
        #     if (validated_data["views"] != None) or (validated_data["views"] != []) or (validated_data["views"] != "") :get_video.views = validated_data["views"] 
        #     if (validated_data["thumbnails"] != None) or (validated_data["thumbnails"] != []) or (validated_data["thumbnails"] != "") :get_video.thumbnails = validated_data["thumbnails"] 
        #     if (validated_data["kyounuki_post_day"] != None) or (validated_data["kyounuki_post_day"] != []) or (validated_data["kyounuki_post_day"] != "") :get_video.kyounuki_post_day = validated_data["kyounuki_post_day"] 
        #     if (validated_data["producturl"] != None) or (validated_data["producturl"] != []) or (validated_data["producturl"] != "") :get_video.producturl = validated_data["producturl"] 
        #     if (validated_data["tags"] != None) or (validated_data["tags"] != []) or (validated_data["tags"] != "") :get_video.tags = validated_data["tags"] 
        #     if (validated_data["active"] != None) or (validated_data["active"] != []) or (validated_data["active"] != "") :get_video.active = validated_data["active"] 
        #     if (validated_data["images"] != None) or (validated_data["images"] != []) or (validated_data["images"] != "") :get_video.images = validated_data["images"] 
        #     get_video.save()
        #     return



        # video.tags.set(objs_tags)
        # video.performers.set(objs_performers)

        # ネストされた関係を更新します
        # self.update_thumbnails(instance, validated_data)

        # 更新したインスタンスを保存します
        instance.save()

        return instance

    class Meta:
        model = Video
        fields = '__all__'






# class UpdateVideoSerializer(serializers.ModelSerializer):
#     # performers = serializers.CharField(max_length=255)
#     performers = GetPerformerSerializer(many=True)
#     # thumbnails = ThumbnailSerializer()
#     maker = GetMakerSerializer()
#     label = GetLabelSerializer()
#     series = GetSeriesSerializer()
#     tags = GetTagSerializer(many=True)
#     duration = serializers.TimeField(format='%H:%M:%S', input_formats=['%H:%M:%S', '%H:%M'], default=datetime.time(0, 0, 0))
#     producturl = serializers.URLField(max_length=200, allow_blank=True)

#     class Meta:
#         model = Video
#         fields = '__all__'
#     def create(self, validated_data):
#         # レコード作成を禁止するため、何も処理せずに例外を発生させます
#         raise serializers.ValidationError("Creating records is not allowed.")

class GetVideoSerializer(serializers.ModelSerializer):
    # performers = serializers.CharField(max_length=255)
    performers = GetPerformerSerializer(many=True)
    # thumbnails = ThumbnailSerializer()
    maker = GetMakerSerializer()
    label = GetLabelSerializer()
    series = GetSeriesSerializer()
    tags = GetTagSerializer(many=True)
    duration = serializers.TimeField(format='%H:%M:%S', input_formats=['%H:%M:%S', '%H:%M'], default=datetime.time(0, 0, 0))
    producturl = serializers.URLField(max_length=200, allow_blank=True)

    class Meta:
        model = Video
        fields = '__all__'
    def create(self, validated_data):
        # レコード作成を禁止するため、何も処理せずに例外を発生させます
        raise serializers.ValidationError("Creating records is not allowed.")
    




# ■■■■■■■■■■■■■■■■■■
# ■■■　KNK　■■■
# ■■■■■■■■■■■■■■■■■■
class KyounukiSerializer(serializers.ModelSerializer):
    post_day = serializers.DateField(format='%Y-%m-%d')
    class Meta:
        model = Kyounuki
        fields = '__all__'

    def create(self, validated_data):
        # kyounuki_post_days = validated_data.get('post_day', [])
        # if not isinstance(kyounuki_post_days, list):
        #     kyounuki_post_days = [kyounuki_post_days]
        article = validated_data.get('article')
        # productnumbers = validated_data.get('productnumbers', [])

        # videos = Video.objects.filter(kyounuki_post_day=kyounuki_post_day)


        # kyounukis = []

        # kyounuki_post_days = Video.objects.values_list('kyounuki_post_day', flat=True).distinct()
        # for kyounuki_post_day in kyounuki_post_days:
        #     print("■■■■■■１")

        #     # Videoモデルをフィルターしてデータを取得
        #     videos = Video.objects.filter(kyounuki_post_day=kyounuki_post_day)

        #     # フィルター結果からproductnumberを取得してリストに格納
        #     if len(videos) > 5:
        #         raise serializers.ValidationError(f"Creating videos records is not length ({len(videos)}).")

        #     productnumbers = [video.pk for video in videos]
        #     # date_str = date_obj.strftime("%Y-%m-%d")


        #     # Kyounukiモデルを作成してリストに追加
        #     kyounuki, _ = Kyounuki.objects.get_or_create(
        #         post_day=kyounuki_post_day, 
        #         defaults={'article': article})
        #     kyounuki.article = article
        #     kyounuki.productnumbers.set(productnumbers)
        #     kyounuki.save()

        #     # kyounuki = Kyounuki.objects.create(
        #     #     post_day=kyounuki_post_day,
        #     #     article=article
        #     # )

        #     kyounukis.append(kyounuki)

        article = validated_data.get('article')
        post_day = validated_data.get('post_day')

        # Videoモデルをフィルターしてデータを取得
        videos = Video.objects.filter(kyounuki_post_day=post_day)

        # フィルター結果からproductnumberを取得してリストに格納
        if len(videos) > 5:
            raise serializers.ValidationError(f"Creating videos records is not length ({len(videos)}).")

        productnumbers = [video.pk for video in videos]
        # date_str = date_obj.strftime("%Y-%m-%d")

        # Kyounukiモデルを作成してリストに追加
        kyounuki, _ = Kyounuki.objects.get_or_create(
            post_day=post_day, 
            defaults={'article': article})
        kyounuki.article = article
        kyounuki.productnumbers.set(productnumbers)
        kyounuki.save()

        return kyounuki



class GetKyounukiSerializer(serializers.ModelSerializer):
    productnumbers = GetVideoSerializer(many=True, read_only=True)
    class Meta:
        model = Kyounuki
        fields = '__all__'
    def create(self, validated_data):
        # レコード作成を禁止するため、何も処理せずに例外を発生させます
        raise serializers.ValidationError("Creating records is not allowed.")


class UpdateVideoSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        # レコード作成を禁止するため、何も処理せずに例外を発生させます
        raise serializers.ValidationError("Creating records is not allowed.")
    class Meta:
        model = Video
        fields = '__all__'

class CreateVideoSerializer(serializers.ModelSerializer):
    title = serializers.CharField(required=False, read_only=True)
    performers = serializers.CharField(required=False, read_only=True)
    productnumber = serializers.CharField()
    maker = serializers.CharField(required=False, read_only=True)
    label = serializers.CharField(required=False, read_only=True)
    series = serializers.CharField(required=False, read_only=True)
    description = serializers.CharField(required=False, read_only=True)
    duration = serializers.CharField(required=False, read_only=True)
    views = serializers.CharField(required=False, read_only=True)
    thumbnails = serializers.CharField(required=False, read_only=True)
    kyounuki_post_day = serializers.CharField(required=False, read_only=True)
    producturl = serializers.CharField(required=False, read_only=True)
    productimage = serializers.CharField(required=False, read_only=True)
    productsumple = serializers.CharField(required=False, read_only=True)
    productthumbnail = serializers.CharField(required=False, read_only=True)
    tags = serializers.CharField(required=False, read_only=True)
    active = serializers.CharField(required=False, read_only=True)
    images = serializers.CharField(required=False, read_only=True)
    issue = serializers.CharField(required=False, read_only=True)
    def create(self, validated_data):
        productnumber_info = validated_data.get('productnumber')
        try:
            # データベースから指定のproductnumberでVideoを取得
            existing_video = Video.objects.get(productnumber=productnumber_info)
            raise serializers.ValidationError(f"Duplicate data for productnumber='{productnumber_info}'.")
        except Video.DoesNotExist:
            pass

        url = f"https://www.dmm.co.jp/digital/videoa/-/detail/=/cid={productnumber_info}/"

        session = requests.Session()
        session.cookies.set("age_check_done", "1") 

        response = session.get(url)
        content = response.content
        soup = BeautifulSoup(content, "html.parser")

        # ■■■■■■■■■１■■■■■■■■
        id_info = None
        performers_info = soup.find(attrs={"data-i3pst": "info_actress"}).get_text()
        maker_info = soup.find(attrs={"data-i3pst": "info_maker"}).get_text()
        label_info = soup.find(attrs={"data-i3pst": "info_label"}).get_text()
        series_info = None
        # tags_info = soup.find(attrs={"data-i3pst": "info_genre"}).get_text() 　※複数あり、処理が必要
        tags_info = None
        duration_info = get_duration_info(soup.find(text='収録時間：').find_parent('td').find_next_sibling().get_text().strip())
        producturl_info = f"https://www.dmm.co.jp/digital/videoa/-/detail/=/cid={productnumber_info}/"
        productimage_info = None
        images_ifno = "a,b,c,d"
        title_info = soup.title.get_text().strip().split(" - []")[0]
        productnumber_info = productnumber_info
        description_info = "記事"
        views_info = "0"
        kyounuki_post_day_info = datetime.datetime.today().date().strftime("%Y-%m-%d")
        active_ifno ="true"
        thumbnails = []
        issue_info = soup.find(text='商品発売日：').find_parent('td').find_next_sibling().get_text().strip().replace(r'/', '-')

        # ■■■■■■■■■２■■■■■■■■■
        # type属性が"application/ld+json"の<script>タグを見つける
        script_tag = soup.find('script', attrs={'type': 'application/ld+json'})

        # <script>タグの中のJSONデータを抽出する
        json_str = script_tag.string.strip()
        json_data = json.loads(json_str)

        # 取得したいキーを指定して値を取得
        product_name = json_data["name"]
        product_image = json_data["image"]
        product_sumple = json_data["subjectOf"]["contentUrl"]
        product_thumbnail = json_data["subjectOf"]["thumbnailUrl"]
        product_description = json_data["description"]
        product_sku = json_data["sku"]
        product_brand_name = json_data["brand"]["name"]
        product_actor_name = json_data["subjectOf"]["actor"]["name"]
        product_actor_name_eng = json_data["subjectOf"]["actor"]["alternateName"]
        product_actor_name_eng = convert_to_romaji(product_actor_name_eng)
        product_actor_genre = json_data["subjectOf"]["genre"]


        from asgiref.sync import sync_to_async
        from django.forms.models import model_to_dict

        # 非同期関数を呼び出す
        maker_instance = None
        label_instance = None
        series_instance = None
        if maker_info:
            try:
                maker_instance = Maker.objects.get(name=maker_info)
    #             maker_instance = maker_instance.id
            except:pass

        if label_info:
            try:
                label_instance = Label.objects.get(name=label_info)
    #             label_instance = label_instance.id
            except:pass

        if series_info:
            try:
                series_instance = Series.objects.get(name=series_info)
    #             series_instance = series_instance.id
            except:pass

        print("performers_info", performers_info)
        performers_instance_list = []
        performers_instance = Performer.objects.filter(name=performers_info)
        
    #     print("performers_info", performers_info)
    #     performer_instance_list = []
    #     for item in product_actor_genre:
    #         try:
    #             tag_instance = await sync_to_async(Tag.objects.get)(name=item)
    #             tag_instance_list.append(tag_instance)
    #         except:pass
    #     print("tag_instance_list", tag_instance_list)
        
        print("tags_info", product_actor_genre)
        tag_instance_list = []
        for item in product_actor_genre:
            try:
                tag_instance = Tag.objects.get(name=item)
                tag_instance_list.append(tag_instance)
            except:pass
        print("tag_instance_list", tag_instance_list)

            
    #     maker_instance = Maker.objects.get(name=maker_info)
    #     label_instance = Maker.objects.get(name=label_info)
    #     series_instance = Maker.objects.get(name=series_info)
    #     maker_instance = Maker.objects.get(name=maker_info)

    #     maker_dict = {"id": maker_instance.id}
    #     label_dict = {"id": label_instance.id}
    #     series_dict = {"id": series_instance.id}



        json_str = json.dumps({
        #     "id": 1,
    #         "performers": None,
            "maker": None,
            "label": None,
            "series": None,
    #         "tags": None,
            "duration": duration_info,
            "producturl": producturl_info,
            "productimage": product_image,
            "productsumple": product_sumple,
            "productthumbnail": product_thumbnail,
            "images": "['https://picsum.photos/200/300', 'https://picsum.photos/200/300', 'https://picsum.photos/200/300', 'https://picsum.photos/200/300']",
            "title": product_name,
            "productnumber": productnumber_info,
            "description": description_info,
            "views": views_info,
            "kyounuki_post_day": kyounuki_post_day_info,
            "active": True,
    #         "thumbnails": [],
            "issue": issue_info
        }, indent=4, ensure_ascii=False)

        # JSON形式の文字列に変換
        # json_str = json.dumps(data, indent=4, ensure_ascii=False)

        # データを表示
        print(json_str)
        
        # JSON文字列を辞書に変換
        data_dict = json.loads(json_str)

        if maker_instance != None:
            data_dict["maker"] = maker_instance
        if label_instance != None:
            data_dict["label"] = label_instance
        if series_instance != None:
            data_dict["series"] = series_instance
        video = create_video(data_dict, performers_instance)

        return video


    class Meta:
        model = Video
        fields = '__all__'

def create_video(data_dict, performers_instance):
    video = Video.objects.create(**data_dict)
    video.performers.set([x.id for x in performers_instance])
    return video






class ContentsSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        contents_info = validated_data.get('contents')
        contents_info = """
        <title>あいうえお
        <subtitle>かきくけこ
        <text>text
        <blockquote>blockquote<bookpage>2
        <title>2
        """

        lines = contents_info.split("\n")
        contents_ = []
        contents = []
        current_page = None
        count = 1
        count_title = 0
        count_subtitle = 0
        count_page = 0

        for line in lines:
            line = line.strip()
            if not line:
                continue
            if line == "":
                continue

            tag, *content = line.split(">")
            tag = tag[1:].lower()
            content = ">".join(content).strip()

            if tag == "title":
                count_title += 1
            elif tag == "subtitle":
                count_subtitle += 1
            elif tag == "page":
                if count_page != 0:
                    count_page = int(content) - 1
                    contents_.append(
                        {"page": count_page, "contents": contents})
                    contents = []
                continue


            if "<bookpage>" in content:
                content, page = content.split("<bookpage>")
                page = int(page)
                obj = {
                    "tag": tag,
                    "text": content,
                    "count": count,
                    "title": count_title,
                    "subtitle": count_subtitle,
                    "blockquotepage": page
                }
            else:
                obj = {
                    "tag": tag,
                    "text": content,
                    "count": count,
                    "title": count_title,
                    "subtitle": count_subtitle
                }
            contents.append(obj)
            count += 1
        
        # ManyToManyField の関連オブジェクトを新しいセットに置き換えます

        contents_tags_info = validated_data.pop('tags', [])
        validated_data["contents"] = contents
        contents = Contents.objects.create(**validated_data)

        contents.tags.set([x.id for x in contents_tags_info])

  
        return contents
    
    class Meta:
        model = Contents
        fields = '__all__'



class GetContentsSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        # レコード作成を禁止するため、何も処理せずに例外を発生させます
        raise serializers.ValidationError("Creating records is not allowed.")
    class Meta:
        model = Contents
        fields = '__all__'




class ContentsTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContentsTag
        fields = '__all__'
class GetContentsTagSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        # レコード作成を禁止するため、何も処理せずに例外を発生させます
        raise serializers.ValidationError("Creating records is not allowed.")
    class Meta:
        model = ContentsTag
        fields = '__all__'