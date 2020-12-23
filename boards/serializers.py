from rest_framework import serializers
from .models import StaffProfile,CollectStar,CollectStaff

class StaffProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = StaffProfile
        fields = ['StaffID', 'Nickname', 'Position', 'DepartmentName', 'DepartmentCode', 'WorkAge', 'Status', 'CreateDate']


class CollectStarSerializer(serializers.ModelSerializer):

     class Meta:
        model = CollectStar
        fields = ['StarID', 'Comment', 'StarAmount', 'YellowCard', 'Status', 'CreateDate']

class CollectStaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = CollectStaff
        fields = ['StaffID','StarID', 'CreateDate']