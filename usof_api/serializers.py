import copy

from rest_framework import serializers


class NotNullSerializer(serializers.ModelSerializer):

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        not_null_ret = copy.deepcopy(ret)
        for key in ret.keys():
            if ret[key] is None:
                not_null_ret.pop(key)
        return not_null_ret

