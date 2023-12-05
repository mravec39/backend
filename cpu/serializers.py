from rest_framework import serializers
from .models import CPU


class CPUSerializer(serializers.ModelSerializer):
    class Meta:
        model = CPU
        fields = '__all__'

    def validate_cores(self, value):
        if value <= 0:
            raise serializers.ValidationError("Number of cores must be greater than 0")
        return value

    def validate_threads(self, value):
        if value <= 0:
            raise serializers.ValidationError("Number of threads must be greater than 0")
        return value

    def validate_base_clock(self, value):
        if value <= 0:
            raise serializers.ValidationError("Base clock must be greater than 0")
        return value

    def validate_boost_clock(self, value):
        if value <= 0:
            raise serializers.ValidationError("Clock boost must be greater than 0")
        return value

    def validate_power_draw(self, value):
        if value <= 0:
            raise serializers.ValidationError("Power draw must be greater than 0")
        return value

    def validate_price(self, value):
        if value <= 0:
            raise serializers.ValidationError("Price must be greater than or equal to 0")
        return value
